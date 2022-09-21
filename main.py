# The bot will, every 10 minutes, read from text list of users,
# get their most recent tweets, sort through the filter mode,
# and send them via Discord DM

# Bot developed by CalicoKaiya

import discord, tweepy
import file_handling as _files
import twitter_funcs as _tweet
from discord.ext import tasks
import vars


### Discord ###
client = discord.Client()
TOKEN = vars.TOKEN
DM_CHANNEL = vars.DM_CHANNEL


### Twitter ###
consumer_key = vars.API_KEY
consumer_secret = vars.API_SECRET_KEY
access_token = vars.ACCESS_TOKEN
access_token_secret = vars.ACCESS_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Generates the embed to be sent as a message with tweet and author information
def generate_embed(api, account, tweet):
    user = api.get_user(account)
    tweet = api.get_status(tweet, tweet_mode = "extended")

    embed_params = {
        "title" : "looksie here!",
        "url" : "https://twitter.com/{}/status/{}".format(user.screen_name, tweet.id_str),
        "description" : tweet.full_text,
        "color" : 0xe680ed
    }

    author_params = {
        "name" : "Tweet from {}:".format(user.name),
        "url" : "https://twitter.com/{}/".format(user.screen_name),
        "icon_url" : user.profile_image_url_https
    }

    footer = str(tweet.created_at) + '\n'
    if user.protected == True:
        footer += "THIS ACCOUNT IS PROTECTED - DO NOT SHOW CONTENT TO PUBLIC!"

    if "media" in tweet.entities:
        thumbnail = tweet.entities["media"][0]["media_url"]
        if len(tweet.entities["media"]) > 1:
            footer += "\nThis status has more than 1 image. View the full tweet on the official website."
    else:
        thumbnail = ""

    embed = discord.Embed(title = embed_params["title"], url = embed_params["url"], description = embed_params["description"], color = embed_params["color"])
    embed.set_author(name = author_params["name"], url = author_params["url"], icon_url = author_params["icon_url"])
    embed.set_footer(text = footer)
    embed.set_thumbnail(url = thumbnail)
    return embed


# Main loop
@tasks.loop(seconds=60*10) # Runs every 10 minutes
async def main(discord):
    try:
        accounts = _files.get_users() # This will return full user data. Must change variable so that it only holds user IDs.
        last_seen = _files.get_last_seen()
        write_last_seen = 0
        for account in accounts:
            filter_mode = account[2]
            username = account[0]
            account = account[1]
            try:
                tweet_user = api.get_user(account)
                last_seen = _files.get_last_seen()
                tweets = _tweet.get_user_tweets(api, account, last_seen, username)
                if len(tweets) > 0:
                    for tweet in tweets:
                        if(_tweet.tweet_filters(tweet, filter_mode)):
                            embed = generate_embed(api, account, tweet.id)
                            await discord.send(embed = embed)
                            print("Sending tweet: {} {}".format(tweet.id, tweet.text))

                            if(tweet.id > write_last_seen):
                                print("NEW WRITE_LAST_SEEN: " + str(write_last_seen))
                                write_last_seen = tweet.id

            except Exception as e:
                print("CAUGHT EXCEPTION: {}".format(e))
            
            if(write_last_seen != 0):
                _files.write_last_seen(write_last_seen)
        
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    print('\n\nConnected to bot: {}\n\n'.format(client.user))
    channel = await client.fetch_channel(DM_CHANNEL)
    main.start(channel)


client.run(TOKEN)
