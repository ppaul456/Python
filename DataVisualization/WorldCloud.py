## Word Clouds
from wordcloud import WordCloud, STOPWORDS
import urllib.request
import matplotlib as mpl
import matplotlib.pyplot as plt

print ('Wordcloud is installed and imported!')

# download file and save as alice_novel.txt, using urllib.request
urllib.request.urlretrieve("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/alice_novel.txt", "alice_novel.txt")

# open the file and read it into a variable alice_novel
alice_novel = open('alice_novel.txt', 'r').read()   
print ('File downloaded and saved!')

#use the function set to remove any redundant stopwords(停用词such as “the”, “a”, “an”, “in”)
stopwords = set(STOPWORDS) 

# Create a word cloud object and generate a word cloud. 
# Let's generate a word cloud using only the first 2000 words in the novel.
# instantiate a word cloud object
alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)
# generate the word cloud
alice_wc.generate(alice_novel)
# display the word cloud
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()
# The most common words are Alice, said, little, Queen

# Customize the size of figure
fig = plt.figure()
fig.set_figwidth(14) # set width
fig.set_figheight(18) # set height

# display the cloud
plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
plt.show()