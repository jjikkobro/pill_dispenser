## Automatic Dosing Machine Management Web Application

Welcome to the Automatic Dosing Machine Management Web Application! This Django-based web application allows users to manage the operation and schedule of their automatic dosing machines.

### Features

1. **User Registration**
   - Secure and user-friendly registration process for new users.
   - User authentication and authorization.

2. **User-Specific Dosing Schedule Management**
   - Each user can manage their own dosing schedule independently.
   - Personalized schedules to ensure accurate and timely dosing.

3. **Dosing Schedule Reservation System**
   - Set up and manage dosing schedules with the following parameters:
     - **Medicine Name:** Specify the name of the medicine to be dosed.
     - **Machine Container:** Assign a specific container in the dosing machine for the medicine.
     - **Time:** Schedule the exact time for the dosing.
     - **Repetition:** Configure the repeat frequency (daily, weekly, etc.).

### Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

- Python 3.x
- Django 3.x
다음은 각 목차의 내용을 간단한 설명과 함께 포함한 "How to start" 목차의 마크다운입니다.

#### 1. 가상환경 설정 및 의존성 설치
##### 1.1 가상환경 생성 및 활성화
프로젝트 디렉토리에서 가상환경을 생성하고 활성화합니다.
```bash
cd /path/to/destination
virtualenv venv
source venv/bin/activate
```
##### 1.2 의존성 설치
프로젝트의 요구사항 파일을 사용하여 필요한 패키지를 설치합니다.
```bash
pip install -r requirements.txt
```

#### 2. 데이터베이스 설정
##### 2.1 데이터베이스 설치 및 설정
데이터베이스를 설치하고 설정합니다.
##### 2.2 데이터베이스 마이그레이션
Django의 마이그레이션 명령어를 실행하여 데이터베이스를 설정합니다.
```bash
python manage.py migrate
```

#### 3. Gunicorn 설정
##### 3.1 Gunicorn 설치
Gunicorn을 설치하여 Django 애플리케이션을 서비스할 준비를 합니다.
```bash
pip install gunicorn
```
##### 3.2 Gunicorn 서비스 파일 생성
Systemd 서비스 파일을 생성하여 Gunicorn을 관리합니다.
```ini
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=your_user
Group=www-data
WorkingDirectory=/path/to/your/project
Environment="PATH=/path/to/your/project/venv/bin"
ExecStart=/path/to/your/project/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/project.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```
##### 3.3 서비스 시작 및 활성화
Gunicorn 서비스를 시작하고 시스템 시작 시 자동으로 시작되도록 설정합니다.
```bash
sudo systemctl start pill.service
sudo systemctl enable pill.service
```

#### 4. Nginx 설정
##### 4.1 Nginx 설정 파일 생성
Nginx 설정 파일을 생성하여 Gunicorn과 통합합니다.
```nginx
server {
    listen 80;
    server_name your_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /path/to/your/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/path/to/your/project.sock;
    }
}
```
##### 4.2 Nginx 설정 활성화
Nginx 설정을 활성화하고 재시작합니다.
```bash
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Usage

1. **Register a New Account**
   - Navigate to the registration page and create a new account.

2. **Login**
   - Login with your registered credentials.

3. **Set Up Dosing Schedule**
   - Navigate to the dosing schedule management page.
   - Add a new schedule by specifying the medicine name, selecting the machine container, setting the time, and configuring the repetition pattern.

4. **Manage Schedules**
   - View, edit, or delete existing dosing schedules.


### Contributing

We welcome contributions to improve this project! If you have suggestions for improvements, please fork the repository and create a pull request. Alternatively, you can open an issue with the tag "enhancement".

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the Django community for their excellent documentation and tutorials.
- Special thanks to all the contributors who helped in developing this project.

---
