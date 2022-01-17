from flask import Flask, send_file, abort
import os

app = Flask(__name__)

path = os.getcwd()

@app.route('/api/v1/images/pokemons/<int:image_id>')
def image(image_id):
    if image_id > 0 and image_id <= 898:
        return send_file(f'{path}/images/{image_id}.png', mimetype='image/png')
    else:
        abort(404)