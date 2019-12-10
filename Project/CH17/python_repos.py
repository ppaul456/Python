# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341


import requests
#import the requests module

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

# Processing an API Response
# Make an API call and store the response.
# Visualizing repositories using Pygal
 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  
r = requests.get(url)   #call get() and pass it the URL, and store the response into r
print("Status code:", r.status_code)
# Store API response in a variable. 
response_dict = r.json()   
#The API returns the information in JSON format, so we use the json() method to convert the information to dictionary
print("Total repositories:", response_dict['total_count'])
# 'total_count', represents the total number of Python repositories on GitHub. 
# Explore information about the repositories. 
repo_dicts = response_dict['items'] 

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Get the project description, if one is available.
    # first pull the description from the dictionary repo_dict. 
    # Then we make sure a description was provided. 
    # If a description was not returned from the API call, set a description ourselves. 
    # the project Shadowsocks is missing a description, and will see No description provided.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
 
# names, stars = [], [] 
# for repo_dict in repo_dicts: 
#     names.append(repo_dict['name'])    
#     stars.append(repo_dict['stargazers_count'])

# Make visualization. 
my_style = LS('#333366', base_style=LCS) 
# Refining Pygal Charts
my_config = pygal.Config()   # my_config will customize the appearance of the chart
my_config.x_label_rotation = 45 
my_config.show_legend = False 
my_config.title_font_size = 24 
my_config.label_font_size = 14 
my_config.major_label_font_size = 18 
my_config.truncate_label = 15     # use truncate_label to shorten the longer project names to 15 characters
my_config.show_y_guides = False 
my_config.width = 1000        # set a custom width so the chart will use more space
chart = pygal.Bar(my_config, style=my_style)  
# pass my_config as the first argument, and it sends all of configuration settings in one argument

chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names
# chart.add('', stars) 
chart.add('', plot_dicts)  # pass the list plot_dicts to add()
chart.render_to_file('python_repos.svg')

# Process results. 
# print(response_dict.keys())

print("Repositories returned:", len(repo_dicts))
# print the length of repo_dicts to see how many repositories

# Examine the first repository. 
repo_dict = repo_dicts[0] # pull out the first item from repo_dicts

# pull out the values for some of the keys in repo_dict
print("\nSelected information about first repository:")  
print('Name:', repo_dict['name'])  
print('Owner:', repo_dict['owner']['login']) # key owner to access the dictionary owner and key login to get the owner’s login name
print('Stars:', repo_dict['stargazers_count']) 
print('Repository:', repo_dict['html_url']) 
print('Created:', repo_dict['created_at']) 
print('Updated:', repo_dict['updated_at']) 
print('Description:', repo_dict['description'])

print("\nKeys:", len(repo_dict)) 
for key in sorted(repo_dict.keys()):    
    print(key)
# get a sense of what kind of information to extract about a project

# loop through all the dictionaries in repo_dicts
# print the name of each project, its owner, stars it has, URL on GitHub, and the project’s description:
print("\nSelected information about each repository:")  
for repo_dict in repo_dicts:    
    print('\nName:', repo_dict['name'])    
    print('Owner:', repo_dict['owner']['login'])    
    print('Stars:', repo_dict['stargazers_count'])    
    print('Repository:', repo_dict['html_url'])    
    print('Description:', repo_dict['description'])