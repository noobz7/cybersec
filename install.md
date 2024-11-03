# Install simple banking software

Prerequirements:
- Windows
- scoop (software installer)
- python version 3

First install the virtual environment

```
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

This creates a new virtual environment and activates it to the current shell.
Then pip command installs the necessary requirements.

To run the software:

```
python manage.py runserver
```

Use browser to access http://localhost:8000 to use the software.

## Enable HTTPS

Without https, the software is vulnerable to OWASP A3:2017-Sensitive Data Exposure.

We fix this vulnerability by activating the https protocal in the backend in the following way.

```
scoop bucket add extras
scoop install mkcert
```

Make the Operating System trust the local certificates. You need to install a local certificate authority (CA) in the system trust store to do this. Run the following command:

```
mkcert -install
```

Generate a certificate for the localhost domain. In the root of this project:

```
mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1
```

Install Django extensions alongwith the Wekzeug server:

```
pip install django-extensions Werkzeug
pip install pyOpenSSL
```

Open the settings.py file in your code editor and add django_extensions to the INSTALLED_APPS list:

```
NSTALLED_APPS = [
    # other apps
    "django_extensions",
]
```

Start the server:

```
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```
