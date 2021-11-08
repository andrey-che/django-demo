# django-demo
django demo project for deployment on AWS App Runner

[Running djnago in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)

Install requirements:

```shell
$ .venv\scripts\activate
(.venv)$ python -m pip install -r requirements.txt
```

App Runner command:

```bash
python django_demo/manage.py runserver 0.0.0.0:8000
or
gunicorn --bind 0.0.0.0:8000 --chdir django_demo django_demo.wsgi:application
```

