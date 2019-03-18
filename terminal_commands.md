Install Django version 1.11
// sudo pip3 install django==1.11

Create a project called "ecommerce"
// django-admin startproject ecommerce .

Add Cloud9 as an allowed host
// ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')]

To run a server
// python3 manage.py runserver $IP:$C9_PORT

Instead of typing out the long string below, now just type "run"
// alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"

Initialise Git repository
// git init
// git status
//git remote add origin https://github.com/jamesahorne/milestone-4.git
// git push -u origin master

Add SQLite file to .gitignore
echo '*.sqlite3' >> .gitignore

Create an app called "accounts"
// django-admin startapp accounts

Add "accounts" to installed apps
// INSTALLED_APPS[... + 'accounts']

Do migrations
// python3 manage.py migrate

Create superuser
// python3 manage.py createsuperuser


