from flask import Flask, render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

MONGODB_HOST = 'ds053419.mlab.com'
MONGODB_PORT = 53419
DBS_NAME = 'heroku_jmds9x8w'
COLLECTION_NAME = 'opendata_projects_clean'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type':True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}
MONGO_URI = 'mongodb://billyTheDBUser:dexte3@ds053419.mlab.com:53419/heroku_jmds9x8w'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/donorsUSA/projects')
def donor_projects():
    connection = MongoClient(MONGO_URI)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects



if __name__ == '__main__':
    app.run(debug=True)
