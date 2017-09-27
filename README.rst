Django simple project
===========================
#.G o to the directory of the project

#. Install dependencies::

    pip install -r requirements/req.txt
#. start mysql with
	mysql -u root
#. crete database with name “todo” and exit mysql
	CREATE DATABASE todo;
	exit

Import database with sample data with following command
	
	mysql -u root  todo < todo.sql
#. Run locally
	python manage.py runserver

Then,  go to
 http://127.0.0.1:8000/admin
in here, you can login as “admintest”, “adminstaff” or “customerservice”
		with password: “admin123qwe” for the three users




Tables in mysql:
===========================
Users table from django
Adress table from model with attributes: adress (varchar 250) and an User object
(i know address is spelled “address” )

For users:
I created a 
	“admintest” user who has all accesses to CRUD both tables
	“adminstaff” user who can view both user and adresses views but can only 			CRUD addresses (adress table).
	“customerservice” who can only see adress table 

All the passwords for all users are the same: admin123qwe

