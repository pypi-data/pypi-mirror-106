import sys
import re
import csv
import json
from tweepy import OAuthHandler, API, Cursor, TweepError
from .functions import get_entities, item_retrieve

def download(filename):

    if input("Ready to download? (y/n) ") == "n":
        sys.exit()

    r = re.compile(r'(?<=\.)csv') 
    ri = re.compile(r'(?<=\.)json')

    ext = ''
    if (r.search(filename)):
        ext = r.search(filename).group(0)

    if (ext == "csv"):
        print("CSV file found.")
        print(f"The script will now load {filename}.")
    elif (ri.search(filename).group(0) == 'json'):
        print("JSON file found.")
        print(f"The script will now load {filename}.")
        ext = "json"

    if input("Continue? ... y/n ").lower() != 'y':
        sys.exit("Quitting.")


    _id = []
    indexes = []

    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""


    try:
        with open("api_keys.json", "r") as f:

            data = json.load(f)

            consumer_key = data["consumer_key"]
            consumer_secret = data["consumer_secret"]
            access_token = data["access_token"]
            access_token_secret = data["access_token_secret"]

    except FileNotFoundError:
    
        print("Missing API information. Ensure an api_keys.json is created with the appropriate information.")
        sys.exit()

    with open(filename, mode="r", encoding="utf-8") as f:
        if ext == "csv":

            csv_reader = csv.DictReader(f)

            for i, row in enumerate(csv_reader):
                indexes.append(i)
                _id.append(row["_id"])
       
        elif ext == "json":

            data = json.load(f)

            for i, item in enumerate(data):
                indexes.append(i)
                _id.append(item)
        
        print(f'Located {len(indexes)} tweets.')
                
        print('Establishing API . . .')
        
        try:
            auth = OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        except TweepError:
            print('Error establishing API . . .')
            sys.exit("Quitting.")

        print('Checking for media...')
        
        data = []
        for i, t in enumerate(_id):
            try:
                status = api.get_status(t, tweet_mode="extended", include_entities=True)._json
                entities = get_entities(status, t)
                
                if "message" in entities:
                    print(f"No media found, ignoring {t}...")
                    continue
                
                for data_dict in entities:
                    print(f"Found: {t}")
                    data_dict['original_row'] = indexes[i]
                    data_dict['tweet_url'] = f'https://twitter.com/statuses/{str(t)}'
                    data.append(data_dict)
            except TweepError as e:
                data.append({'message':e, 'original_row': i, 'tweet_id': t})
                continue

        num_media = len([x for x in data if 'medium' in x])
        print(f'Retrieved meta-data for {num_media} media items...')

        print("Retrieving media items...")
       
        for row in data:
            if 'medium' in row:
                print(f"Downloading {row} ...")
                item_retrieve(row)
        print(f'Job Complete. Check the "media" folder for your files. Have a nice day!')
