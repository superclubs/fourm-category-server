#!/usr/bin/env bash

# Create the celery systemd service file
echo "[Unit]
Description=Celery Beat Service for SUPERCLUB's CLUB
After=network.target

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory=/var/app/current
EnvironmentFile=/opt/elasticbeanstalk/deployment/env
ExecStart=/var/app/venv/staging-LQM1lest/bin/celery -A community beat --logfile=/var/log/celery/beat.log --pidfile=/var/run/celery/beat.pid --loglevel=INFO

[Install]
WantedBy=multi-user.target
" | tee /etc/systemd/system/celery-beat.service

echo "[celery-beat.sh] Reset failed"
systemctl reset-failed celery-beat.service
systemctl daemon-reload

echo "[celery-beat.sh] Start celery service"
systemctl restart celery-beat.service

echo "[celery-beat.sh] Enable celery service to load on system start"
systemctl enable celery-beat.service

echo "[celery-beat.sh] Check status"
systemctl status celery-beat.service
