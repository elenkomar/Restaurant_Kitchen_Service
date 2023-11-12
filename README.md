**Kitchen Service Project**
------------------------------------
A Django project to oversee restaurant operations and enhance chef communication in the kitchen. Every chef at your establishment has a personal profile that includes details about them and the food they create.

**Check it out!**
-----------------------------------
Your user:

test_user - Login

test1422 - password

**Setup:**
----------------------------------
1. Clone the project:

`* git clone https://github.com/elenkomar/Restaurant_Kitchen_Service.git`

2. Create virtual environment and activate it

**for Windows**

`* python -m venv venv`

`* venv\Scripts\activate`

3. Install dependencies

`* pip install -r requirements.txt`

4. Run migrations

`* python manage.py migrate`

5. Create superuser

`* python manage.py createsuperuser (enter your username and password)`

6. Run server on local host

* you must create .env file with your data (look at exemple in .env.sample)

* python manage.py runserver

**Demo:**
-----------------------------
![all_cooks.jpg](static%2Fscreenshots%2Fall_cooks.jpg)
![all_dish_type.jpg](static%2Fscreenshots%2Fall_dish_type.jpg)
![all_dishes.jpg](static%2Fscreenshots%2Fall_dishes.jpg)
![create_cook.jpg](static%2Fscreenshots%2Fcreate_cook.jpg)
![create_dish.jpg](static%2Fscreenshots%2Fcreate_dish.jpg)
![create_dish_type.jpg](static%2Fscreenshots%2Fcreate_dish_type.jpg)
![home_page.jpg](static%2Fscreenshots%2Fhome_page.jpg)
![login.jpg](static%2Fscreenshots%2Flogin.jpg)
