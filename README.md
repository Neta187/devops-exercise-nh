# BigPanda DevOps Exercise
#### INTRO
Hi, 

The exercies wrriten in Python. The services are running in ubuntu virtual environment since I couldn't work with the provided Vagrant box.
I used flask module in order to run the http services.

#### Notes:

I performed a POST request with the following curl to check the counter:
"curl -i -H "Content-Type: application/json" -X POST -d {"Panda":"2"} http://localhost:5001/smart_panda"

#### My improvement tasks:

* The counting starting from zero on each service reload.
* The ansilble should restart the services.







