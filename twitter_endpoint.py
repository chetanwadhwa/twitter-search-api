from flask_restful import Resource
from flask import request
from werkzeug.exceptions import BadRequest
from pymongo import MongoClient
import datetime
import re
# Can move this connection code at a common place
try:
    mongo_client = MongoClient('127.0.0.1', 27017)
except:
    print("Could not connect to mongo")
    mongo_client = None


class TwitterEndpoint(Resource):
    def get(self):
        query_string = request.args.get('q')
        filter_type = request.args.get('filter_type')
        limit = request.args.get('limit')
        limit = int(limit)
        offset = request.args.get('offset')
        offset = int(offset)
        group_by = request.args.get('group_by')

        db = mongo_client.twitter

        searched_tweets = []
        if filter_type not in ['created_date', 'text', 'friends_count']:
            raise BadRequest('Not a valid choice for filter_type')

        if filter_type == 'created_date':
            try:
                datetime.datetime(query_string)
                searched_tweets = db.twitter_search.find({'created_at': re.compile(query_string,)}).limit(limit).skip(offset)
            except:
                raise BadRequest('Invalid Date Timestamp')
        elif filter_type == 'text':
            if type(query_string) is not str:
                pass
            searched_tweets = db.twitter_search.find({'text': query_string}).limit(limit).skip(offset)
        elif filter_type == 'friends_count':
            if type(query_string) is not int:
                raise BadRequest('Invalid integer')
            searched_tweets = db.twitter_search.find({'user.followers_count': query_string}).limit(limit).skip(offset)




        response = []
        for x in searched_tweets:
            del x['_id']
            response.append(x)
        return response
