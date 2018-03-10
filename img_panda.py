from flask import request
from flask import send_from_directory
import glob
import os
import random
from flask import Flask

app = Flask(__name__)

#On each GET request return different Panda image.
@app.route('/panda', methods=['GET'])
def download():
    uploads = 'resources'
    panda_files = glob.glob(os.path.join(uploads,'*.jpg'))
    rnd_panda_file = os.path.basename(random.choice(panda_files))
    return send_from_directory(directory=uploads, filename=rnd_panda_file)


if __name__ == '__main__':
    app.run()

