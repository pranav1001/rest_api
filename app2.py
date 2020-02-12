import json                                                     
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo

app = Flask(__name__)                                           
app.config['MONGO_URI']= 'mongodb+srv://pranav:bluebricks@rbadb-39wxq.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
@app.route('/post_api',methods=['POST'])            
def test_api():                                           
    # uploaded_file = request.files['document']
    # data = json.load(request.files['data'])
    # filename = secure_filename(uploaded_file.filename)
    # uploaded_file.save(os.path.join('C:/Users/prana/OneDrive/Desktop/books/data', filename))
    data = request.get_json()
    print(data)
    mongo.db.rba_app.insert(data)
    response = {'error_code':0 , 'message': "success"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)