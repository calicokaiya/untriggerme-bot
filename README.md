# What is this?
This is a twitter and discord bot that will grab tweets from a user-defined list of accounts and send them to your discord DMs. You must have Twitter API keys and a Discord bot in order for this to work.

# Is the project still being updated?
The project was actually created around 2019, and ever since then I have very rarely touched it. **This project has been pretty much abandoned.** You are, however, free to create forks of it and update it to your liking, as I understand that there is a lot of improvement to be made here.

# How can I set it up?
1. Sign up for a [Twitter API key](https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)
2. Create a [Discord Bot](https://discord.com/developers/applications)
3. Clone the repository with `git clone https://github.com/calicokaiya/untriggerme-bot.git`
4. Go into untriggerme-bot and install requirements with `pip install -r requirements.txt`. You may have to change the command in order to invoke pip. Some common ways to do this are `python -m pip`, `python3 -m pip` and `pip3`.
5. Fill credentials in file vars.py (more info below)
6. Run the bot with `python main.py`, or however else you use python

# About vars.py
## Discord ##
Settings in this section are related to your Discord bot.

- The line `TOKEN=` is expecting a string with your Discord bot token, which you can get in the discord developer portal.
- The line `DM_CHANNEL` is expecting an int that represents your [DM channel with the bot](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-)

## Tweepy ##
Settings in this section are related to your Twitter bot, and how it integrates with Tweepy. All of these fields can be filled by copy pasting info from the twitter developer portal.

- `API_KEY = ''` expects a string of your Twitter API Key
- `API_SECRET_KEY = ''` expects a string of your API Secret Key
- `BEARER_TOKEN = ''` expects a string of your Bearer Token
- `ACCESS_TOKEN = ''` expeccts a string of your Access Token
- `ACCESS_SECRET = ''` expects a string of your Access Secret
