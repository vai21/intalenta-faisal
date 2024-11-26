# Intalenta Test
My name is Faisal, and this is repository for test in Intalenta

## Installation
to run this project first create virtual environment

```bash
cd ./app
python -m venv env
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

filled with your username, email and password

``` bash
cd ..
docker-compose up -d --build
```

## Description
Docker compose will install and run all the dependencies like redis, django web, postgresql, celery, flower.
Change the AI21 secret key with your secret key for sentiment analysis.
## Documentation
[Documentation](https://spectacular-rest-ab6.notion.site/Intalenta-Test-14a17c6f2af280eb946ce0f349024955)

## License

[MIT](https://choosealicense.com/licenses/mit/)
