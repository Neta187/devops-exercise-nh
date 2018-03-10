from flask import request
from flask import send_from_directory
from flask import current_app

import glob
import os
import random


from flask import Flask
app = Flask(__name__)

@app.route('/smart_panda', methods=['GET','POST'])
def smart():
    if request.method == 'POST':
	current_app.post_counter += 1
        return 'OK'
    elif request.method == 'GET':
      return str(current_app.post_counter)


if __name__ == '__main__':
    app.post_counter = 0
    with app.app_context():
    	app.run(port=5001)

