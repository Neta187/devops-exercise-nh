# BigPanda DevOps Exercise
#### INTRO
Hi BigPanda, 

The exercies written in Python. The services are running in ubuntu virtual environment since I couldn't work with the provided Vagrant box.
I used flask module in order to run the http services.

#### Notes:

From the home directory:

My virtual environment:
* source env/bin activate

* samart_panda.py run service on:

http://localhost:5001/smart_panda

* img_panda.py run service on:

http://localhost:5000/img_panda


for example a POST request with the following curl check the counter:

"curl -i -H "Content-Type: application/json" -X POST -d {"Panda":"Panda"} http://localhost:5001/smart_panda"

#### My improvement tasks:

* The counting will be starting from zero on each service reload.
* The ansilble should restart the services in different modes.
* Improve the deployment part







