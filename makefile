all:
	make run
env: 
	pip install --upgrade pip 
	pip install -r requirements.txt --no-cache-dir
run:
	python manage.py runserver 8001
migrate:
	python manage.py makemigrations
	python manage.py migrate
rm: 
	rm -rf db.sqlite3
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete 
	pip uninstall django -y
	pip install Django==3.2.5 
	make migrate
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('thiago', 'admin@myproject.com', 'thiago')" | python manage.py shell
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('pixeon', 'pixeon@myproject.com', 'Pixeon@2022')" | python manage.py shell
	make
help:
	@echo  