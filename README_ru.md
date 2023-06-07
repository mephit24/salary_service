# API REST сервис просмотра зарплаты.  
#
## Описание:  

Сервис принимает:
+ Get-запрос на URN /login, содержащий логин и пароль и возвращает токен авторизации (jwt-типа);
+ POST-запрос на URN /salary и возвращает информацию о зарплате в json-формате, если в теле запроса есть валидный токен;
#
Заметка: используется тестовая база данных с тестовыми пользователями: *db.sqlite3*, которую можно создать запуском скрипта *create_demo_db.py*.
# 
## Установка и запуск:

* Клонируйте приложение из Gitlab или Github:
  ```bash
  git clone https://gitlab.com/mephit24/salary_service.git
  git clone https://github.com/mephit24/salary_service.git
  ```
  Или скачайте архив:  
  https://gitlab.com/mephit24/salary_service/-/archive/master/salary_service-master.zip
  https://github.com/mephit24/salary_service/archive/refs/heads/master.zip

* Перейдите в директорию приложения:
  ```bash
  cd /path/to/app
* Если необходимо, отредактируйте config.ini.
* Если вы хотите использовать Poetry (https://python-poetry.org/docs/basic-usage/):  
    - Установите Poetry, если он не установлен:
    ```bash
    python3 -m pip install poetry
    ```
    - Запустите:
    ```bash
    poetry install
    poetry shell
* Если вы хотите использовать Pip:
    - Если нужно, создайте виртуальное окружение https://docs.python.org/3/library/venv.html
    - Запустите только один раз:
    ```bash
    python3 -m pip install -r requirements.txt

* Запустите приложение:
  ```bash
  python3 run.py
  ```

* Откройте url http://localhost:8080/ в вашем браузере.


## Для запуска приложения в Docker:  
Заметка: Приложение запускается на порту 8080.
* Установите Docker:  
  + https://docs.docker.com/engine/install  

* Запустите:
  ```bash
  docker run -d -p 8080:8080 mephit/salary_service
* Откройте url http://localhost:8080 в вашем браузере.

#
## Использование:
Для получения информации о зарплате вы можете использовать встроенную FastApi документацию в вашем браузере:  
http://localhost:8080/docs   
или использовать простой демонстрационный клиент:  
```bash
python3 ./client.py --help
```

Запуск с позиционными аргументами (логин и пароль) вернет токен авторизации, что позволит в дальнейшем запускать клиент без параметров (пока не истечет время жизни токена) для получения информации о зарплате.
Так же вы можете использовать утилиты вроде curl https://curl.se/docs/manpage.html для взаимодействия с сервисом.

Используйте тестовые данные из create_demo_db.py, например:
```bash
python3 ./client test 12345
# You got auth token: eyJ...K0E
python3 ./client
# {"salary":500.0,"date up":"01.01.2000"}
```
#  
### **Внимание**:  
Клиент предназначен только для демонстрации и хранит токен в открытом виде!

#
Заметка: Т.к. сервис не производит запись в базу данных, тесты настроены на демонстрационную базу данных в составе приложения, которую можно создать запуском скрипта create_demo_db.py.
