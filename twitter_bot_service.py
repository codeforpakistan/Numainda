from dotenv import load_dotenv
load_dotenv()

from classes.twitter import TwitterBot

bot = TwitterBot()
if bot.api is None:
    exit(1)
    
bot.start()