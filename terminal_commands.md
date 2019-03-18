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

Add SQLite file to .gitignore
echo '*.sqlite3' >> .gitignore
