# qa-website
    A Question-Answer site with added features of blogging and Faculty Polling to facilitate interactions between Seniors and Juniors of an institution.

## Instructions
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

> 5. Migrations
```sh
python3 manage.py makemigrations
```

> 6. Server instructions

```sh
python3 manage.py runserver 
```


> 7. Run in the browser
+ open localhost:8000 in your browser 
sqlite3
