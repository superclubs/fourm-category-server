# custom_admin/admin.py
from functools import update_wrapper

from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.contenttypes import views as contenttype_views
from django.http import HttpResponseRedirect, Http404
from django.template.response import TemplateResponse
from django.urls import path, include
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


class CustomAdminSite(admin.AdminSite):
    site_header = "[SUPERCLUB] 포럼 카테고리 관리"
    site_title = "[SUPERCLUB] 포럼 카테고리 관리"
    index_title = "[SUPERCLUB] 포럼 카테고리 관리"

    @method_decorator(csrf_protect)
    @never_cache
    def login(self, request, extra_context=None):
        if request.method == 'GET' and self.has_permission(request):
            # 이미 로그인한 경우 관리 페이지로 리디렉션합니다.
            index_path = reverse('admin:index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        # 로그인 폼을 표시합니다.
        from django.contrib.admin.forms import AdminAuthenticationForm
        from django.contrib.auth.views import LoginView

        context = {
            **self.each_context(request),
            'title': _('Log in'),
            'app_path': request.get_full_path(),
            'username': request.user.get_username(),
        }
        if (REDIRECT_FIELD_NAME not in request.GET and
            REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('admin:index', current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'admin/login.html',
        }
        request.current_app = self.name
        return LoginView.as_view(**defaults)(request)

    def get_urls(self):
        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)

            wrapper.admin_site = self
            return update_wrapper(wrapper, view)

        urlpatterns = [
            path('', wrap(self.index), name='index'),
            path('login/', self.login, name='login'),
            path('logout/', wrap(self.logout), name='logout'),
            path('password_change/', wrap(self.password_change, cacheable=True), name='password_change'),
            path(
                'password_change/done/',
                wrap(self.password_change_done, cacheable=True),
                name='password_change_done',
            ),
            path('autocomplete/', wrap(self.autocomplete_view), name='autocomplete'),
            path('jsi18n/', wrap(self.i18n_javascript, cacheable=True), name='jsi18n'),
            path(
                'r/<int:content_type_id>/<path:object_id>/',
                wrap(contenttype_views.shortcut),
                name='view_on_site',
            ),
            # 추가된 app_list URL 패턴
            path('<str:app_label>/', wrap(self.app_index), name='app_list'),
        ]

        # ModelAdmin URL 패턴 추가
        for model, model_admin in self._registry.items():
            urlpatterns += [
                path('%s/%s/' % (model._meta.app_label, model._meta.model_name), include(model_admin.urls)),
            ]

        return urlpatterns

    def app_index(self, request, app_label, extra_context=None):
        app_dict = self._build_app_dict(request, app_label)
        if not app_dict:
            raise Http404('The requested admin page does not exist.')
        app_dict['models'].sort(key=lambda x: x['name'])
        context = {
            **self.each_context(request),
            'title': _('%(app)s administration') % {'app': app_dict['name']},
            'subtitle': None,
            'app_list': [app_dict],
            'app_label': app_label,
            **(extra_context or {}),
        }
        request.current_app = self.name
        return TemplateResponse(request, self.app_index_template or [
            'admin/%s/app_index.html' % app_label,
            'admin/app_index.html'
        ], context)

    @property
    def urls(self):
        return self.get_urls(), 'admin', self.name


custom_admin_site = CustomAdminSite(name='custom_admin')
