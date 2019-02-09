#SENTIMENT ANALYSER
import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

#API Authentication
consumer_key='' 
consumer_secret=''

access_token=''
access_token_secret=''

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

#user input
query=input("Enter String:")
no_of_tweets=int(input("No of tweets:"))


#public_tweets= api.search(query)
public_tweets= tweepy.Cursor(api.search,q=query).items(no_of_tweets)

#SAD TO HAPPY(-1  TO  1) POLARITY
a=[]
negative=0.0
nutral=0.0
positive=0.0
for tweet  in public_tweets:
    #print(tweet.text)
    analysis=TextBlob(tweet.text)
    value=analysis.sentiment.polarity
    a.append(value)
    if(value==0):
        nutral+=1
    elif(value<0):
        negative+=1
    else:
        positive+=1
        

total=(positive+negative+nutral)      
negative_percentage=(negative*100)/total
nutral_percentage=(nutral*100)/total
positive_percentage=(positive*100)/total

explode=()
if(max(negative_percentage,positive_percentage,nutral_percentage)==nutral_percentage):
    #print("nutral")   
    explode=(0,0.1,0)
elif(max(negative_percentage,positive_percentage,nutral_percentage)==negative_percentage):
    #print('negative')
    explode=(0,0,0.1)
else:
    #print("positive")
    explode=(0.1,0,0)
 
#################### pie chart ############################
labels=["Positive","Nutral","Negative"]
colors=["green","yellow","red"]
weight=[positive_percentage,nutral_percentage,negative_percentage]
# plotting the pie chart 
plt.pie(weight, labels = labels, colors=colors,  
        startangle=90, shadow = True, explode = explode, 
        radius = 1.2, autopct = '%1.1f%%')
# plotting legend 
plt.legend() 
  
# showing the plot 
plt.show() 

################ bar graph ###############################

# x-coordinates of left sides of bars  
left = [1, 2, 3] 
  
# heights of bars 
height = weight 
  
  
# plotting a bar chart 
plt.bar(left, height, tick_label = labels, 
        width = 0.8, color = colors) 
  
# naming the x-axis 
plt.xlabel('Sentiment') 
# naming the y-axis 
plt.ylabel('Percentage') 
# plot title 
plt.title('Sentiment analysis') 
  
# function to show the plot 
plt.show() 


    
#print(a)
