#!/usr/bin/env bash

# Create the celery systemd service file
echo "[Unit]
Description=Celery Service for SUPERCLUB's CLUBCATEGORY
After=network.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/var/app/current
EnvironmentFile=/opt/elasticbeanstalk/deployment/env
ExecStart=/var/app/venv/staging-LQM1lest/bin/celery -A clubcategory worker --logfile=/var/log/celery/worker.log --pidfile=/var/run/celery/%n.pid --loglevel=INFO -n worker.%%h
ExecReload=/var/app/venv/staging-LQM1lest/bin/celery -A clubcategory worker --logfile=/var/log/celery/worker.log --pidfile=/var/run/celery/%n.pid --loglevel=INFO -n worker.%%h

[Install]
WantedBy=multi-user.target
" | tee /etc/systemd/system/celery.service

echo "[celery.sh] Reset failed"
systemctl reset-failed celery.service
systemctl daemon-reload

echo "[celery.sh] Start celery service"
systemctl restart celery.service

echo "[celery.sh] Enable celery service to load on system start"
systemctl enable celery.service

echo "[celery.sh] Check status"
systemctl status celery.service
