import os
import tweepy
import time
from classes.assistant import Assistant

PROMPT = "<PROMPT INSTRUCTIONS HERE>"

class TwitterBot:
    def __init__(self):
        self.api = TwitterBot.authenticate()
    
    # Entry point for the Twitter bot
    # After every 5 minutes, the bot will check for new mentions and respond to them
    def start(self, since_id):        
        since_id = 1
        openai = Assistant(openai_api_key=os.getenv("OPEN_AI_API_KEY")).get_client()
        
        while True:
            since_id = self.respond_to_mentions(since_id, openai)
            time.sleep(300)
 
    def respond_to_mentions(self, since_id, openai):
        new_since_id = since_id
        
        for tweet in tweepy.Cursor(self.api.mentions_timeline, since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            if tweet.in_reply_to_status_id is not None:
                continue
            
            messages = [
                { "role": "system", "content": PROMPT },
                { "role": "user", "content":   tweet.text },
            ]
            
            completion = openai.ChatCompletion.create(
                model="gpt-4-1106-preview",
                messages=messages,
            )
            
            self.api.update_status(
                status=completion.choices[0].message.content,
                in_reply_to_status_id=tweet.id,
            )
            
        return new_since_id
                
    def authenticate() -> tweepy.API:
        auth = tweepy.OAuthHandler(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET'))
        auth.set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN'))
        
        api = tweepy.API(auth)
        
        try:
            api.verify_credentials()
            print("Authentication was successful!")
        except Exception as e:
            print(f"Authentication failed: {e}")
            return None
            
        return api
    
    def post_tweet(self, tweet):
        self.api.update_status(tweet)
        return True
    
    def get_all_mentions(self):
        return self.api.mentions_timeline()