#simple twitter bot to post a tweet
#requires twitter api for developers to run!
#fill in the :pseudo
#!/usr/bin/python3

#twitterbot.py

#Authentificate to twitter
import tweepy
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret") 
auth.set_access_token("access_token", "access_token_secret")

#api obj
#pass auth as :param
api_onj = tweepy.API(aut)

#create a tweet
api.update_status("hello!")
