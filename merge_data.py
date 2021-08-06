import json
import pandas as pd

from os import listdir
from os.path import isfile, join

mypath = '/Users/Sumon/Desktop/like-estimation/10k tweets/'
users_meta_info = '/Users/Sumon/Desktop/like-estimation/10k tweets/users_meta_info.jsonl'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
df = pd.DataFrame(columns=['user_id','user_name','location', 'description',\
                           'follower_count','friends_count','verified','tweet_id',\
                           'created_at','num_of_likes','retweet_count','text',\
                           'user_location'])

with open(users_meta_info, 'r') as json_file:
    json_list = list(json_file)
    for json_str in json_list:
        dict = {}
        meta = json.loads(json_str)
        if meta['user_name'].lower()+'.jsonl' in onlyfiles:
            print(meta['user_id'])
            dict['user_id'] = meta['user_id']
            dict['user_name'] = meta['name']
            dict['location'] = meta['location']
            dict['description'] = meta['description']
            dict['follower_count'] = meta['follower_count']
            dict['friends_count'] = meta['friends_count']
            dict['verified'] = meta['verified']
            path = f"{mypath}{meta['user_name'].lower()}.jsonl"
            with open(path, 'r') as json_file:
                user_data = list(json_file)
                for user in user_data:
                    data = json.loads(user)
                    dict['tweet_id'] = data['tweet_id']
                    dict['created_at'] = data['created_at']
                    dict['num_of_likes'] = data['num_of_likes']
                    dict['retweet_count'] = data['retweet_count']
                    dict['text'] = data['text']
                    dict['user_location'] = data['user_location']
                    #print(f"result: {dict}")
                    df = df.append(dict, ignore_index=True)


df.to_csv('data.csv',index=False)






