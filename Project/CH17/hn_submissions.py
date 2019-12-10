# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341

import requests
#import the requests module
from operator import itemgetter

# Make an API call and store the response. 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
r = requests.get(url) 
print("Status code:", r.status_code)
# This API call returns a list containing the IDs of the 500 most popular articles on Hacker News

# Process information about each submission. 
#convert the response text to a Python list 
submission_ids = r.json()
submission_dicts = [] 
for submission_id in submission_ids[:30]:  # loop through the IDs of the top 30 submissions. 
    # Make a new API call for each submission by generating a URL that includes the current value of submission_id   
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')    
    submission_r = requests.get(url)    
    print(submission_r.status_code)    
    response_dict = submission_r.json()

    submission_dict = {        
        'title': response_dict['title'],        
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id), 
        'comments': response_dict.get('descendants', 0)        
        }  
    submission_dicts.append(submission_dict) 

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
# itemgetter() a function from the operator module, pass this function the key 'comments', 
# and it pulls the value associated with that key from each dictionary in the list

for submission_dict in submission_dicts:    
    print("\nTitle:", submission_dict['title'])    
    print("Discussion link:", submission_dict['link'])    
    print("Comments:", submission_dict['comments'])

