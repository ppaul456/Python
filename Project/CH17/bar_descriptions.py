# Name: Pohsun Chang
# Student ID: 830911
# Due Date: 12/14/2019
# MSITM 6341


import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

# Adding Custom Tooltips
my_style = LS('#333366', base_style=LCS) 
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects' 
chart.x_labels = ['httpie', 'django', 'flask']
# define a list called plot_dicts that contains three dictionaries: 
# one HTTPie project, one Django project, and one Flask. 
# Each dictionary has two keys: 'value' and 'label'. 
# Pygal uses the number associated with 'value' to figure out how tall each bar, 
# and it uses the string associated with 'label' to create the tooltip for each bar
plot_dicts = [ 
    {'value': 16101, 'label': 'Description of httpie.'},    
    {'value': 15028, 'label': 'Description of django.'},    
    {'value': 14798, 'label': 'Description of flask.'},    
    ]

chart.add('', plot_dicts) 
chart.render_to_file('bar_descriptions.svg')
