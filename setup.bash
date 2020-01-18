#!/bin/bash
# this is presuming that the machine has latest virtualenv installed as older version of virtula env causes issue while running through bash
#virtualenv -p /usr/bin/python3 plateiq_env
#source ./plateiq_env/bin/activate
#pip install -Ur requirements.txt

echo "Initial Setup Done"
echo ""
echo "- Make sure you are in plateid_env"
echo "- Copy Paste Following command to complete the setup"
echo ""
echo "python manage.py makemigrations"
echo "python manage.py migrate --run-syncdb"
echo "python manage.py createsuperuser"
echo ""
echo "There are two different API Endpoint sets, one is for Consumer and other is for PlateIQ Admins"
echo "i.e. localhost:8000/consumer & localhost:8000/admin"
echo ""
echo "If no error occurred you are good to start server with following command"
echo "python manage.py runserver"


