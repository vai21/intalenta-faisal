My name is Faisal, and this is repository for test in Intalenta

to run this project first create virtual environment

cd ./app
python -m venv env
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

filled with your username, email and password

cd ..

docker-compose up -d --build

Docker compose will install and run all the dependencies like redis, django web, postgresql, celery, flower.

change the AI21 secret key with your secret key for sentiment analysis
