# API REST service of salary viewing.  
#
## Description:  

The service takes:
+ Get-request on URN /login with login and password in body and return an authorization token (jwt-kind);
+ POST-request on URN /salary and return salary info (json-kind) if there is token in header;
#
Note: There is a demo-database with fake-users: *db.sqlite3*. It is created by using file *create_demo_db.py*.
# 
## Install and run:

* Clone the application from Gitlab or Github:
  ```bash
  git clone https://gitlab.com/mephit24/salary_service.git
  git clone https://github.com/mephit24/salary_service.git
  ```
  Or download archive:  
  https://gitlab.com/mephit24/salary_service/-/archive/master/salary_service-master.zip
  https://github.com/mephit24/salary_service/archive/refs/heads/master.zip

* Go to application directory:
  ```bash
  cd /path/to/app
* If necessary, edit config.ini.
* If you want to use Poetry (https://python-poetry.org/docs/basic-usage/):  
    - Install Poetry if it isn't:
    ```bash
    python3 -m pip install poetry
    ```
    - Run:
    ```bash
    poetry install
    poetry shell
* If you want to use Pip:
    - If you need to create virtual environment https://docs.python.org/3/library/venv.html
    - Run only for first time:
    ```bash
    python3 -m pip install -r requirements.txt

* Run application:
  ```bash
  python3 run.py
  ```

* Open url http://localhost:8080/ in your internet browser.


## For start the application in Docker:  
Note: the application starts on 8080 port.
* Install Docker:  
  + https://docs.docker.com/engine/install  

* Run:
  ```bash
  docker run -d -p 8080:8080 mephit/salary_service
* Open url http://localhost:8080 in your internet browser.

#
## Use:
For get salary information you can use built-in FastApi docs in your browser:  
http://localhost:8080/docs   
or use simple demonstration client:  
```bash
python3 ./client.py --help
```
A start with positional arguments (login and password) will get authorization token and allow start client without parameters (until token lifetime don't expire) for getting salary information.

Also you can use utilites like curl https://curl.se/docs/manpage.html for interaction to service.

Use testing data from create_demo_db.py, example:
```bash
python3 ./client test 12345
# You got auth token: eyJ...K0E
python3 ./client
# {"salary":500.0,"date up":"01.01.2000"}
```
#  
### **Attention**:  
The client is only for demonstration and it keep token plainly!

#
Note: Because this application doesn't write to DB, demo-db is used to testing with data from create_demo_db.py.
