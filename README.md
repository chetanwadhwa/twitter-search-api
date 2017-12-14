# twitter-search-api

Steps to run the code

Have Mongo installed and running on port 27017

make virtualenv in python3 

virtualenv -p python3 venv3
pip install -r requirements.txt

** To fetch Tweets from Stream API run command **

python search.py

This command will fetch tweets and seed data in mongo

** For Search API **

python run.py

GET request

http://127.0.0.1:2312/twitter?q=l&filter_type=text&limit=10&offset=0

Filter Type

1. Text
2. Created Date
3. User.followers count
