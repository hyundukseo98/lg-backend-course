#!/bin/bash
cd /home/ec2-user/rcmd_practice
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart fastapi
echo "배포 완료!"