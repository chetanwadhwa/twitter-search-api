from flask import Flask
from flask_restful import Api
from twitter_endpoint import TwitterEndpoint
from flask_admin import Admin

APP = Flask(__name__)
APP.secret_key = "Test"
admin = Admin(APP, name='twitter', template_mode='bootstrap3')

api = Api(APP)


args = [TwitterEndpoint,'/twitter']
api.add_resource(*args)




APP.run(port=2312, debug=True, host='127.0.0.1')