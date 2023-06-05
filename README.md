# API REST service of salary viewing.  

Note: There is a demo-database with fake-users: *db.sqlite3*. It is created by using file *create_demo_db.py*.
# 
## Install and run:

* Clone the application from Gitlab or Github:
  ```bash
  git clone https://
  git clone https://
  ```
  Or download it:
  https://
  https://

* Go to application directory:
  ```bash
  cd /path/to/app
* If necessary, edit config.ini.
* If you want to use Poetry:  
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

* Open url http://127.0.0.1:8080/ in your internet browser.  
Do something.

## For start the application in Docker:
* Install Docker:  
  + https://docs.docker.com/engine/install  

* Run:
  ```bash
  docker run -d -p 8080:8080 mephit/salary_service
* Open url http://127.0.0.1:8080 in your internet browser.

#
## Use:
Do something.






#
Note: Because this application doesn't write to DB, demo-db is used to testing with data from create_demo_db.py.