# qa-website
A new quora and stack overflow competitor based on django


## Installation
> 1. Create a development 
```sh
sudo pip install virtualenv
cd qa-website
virtualenv -p python3 env
```
> 2. To activate env
```sh
source env/bin/activate
```
> 3. To deactivate env
```sh
deactivate
```
> 4. Install dependencies
```sh
pip install -r requirements.txt
```
> 5. Configure mysql

+ Debian
```sh
sudo apt-get install python-pip python-dev libmysqlclient-dev
```
+ Mac Os
```sh
brew install mysql
```
> 6. Create a database

```sh
mysql -u {%username%} -p
```

```sql
CREATE DATABASE qa;
```
> 7. Migrations
```sh
./manage.py makemigrations
```

> 8. Server instructions

```sh
./manage.py runserver 0:8000
```

> 9. Run in the browser
+ Run localhost:8000 in your browser 