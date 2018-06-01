# BNav

### Set Up 

clone the repo

```
pip install virtualenv
virtualenv --python=python3.5 venv 
source venv/bin/activate 
pip install -r requirements.txt
python app.py
```

### Deployment

1.install nginx

2.copy the repo to /var/www/

3.copy the nginx.conf to /etc/nginx/sites-enabled/default

```

pip install uwsgi
cd /var/www/BNav
uwsgi --ini 

```

