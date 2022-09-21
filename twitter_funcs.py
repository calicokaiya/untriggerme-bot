# Gets user tweets
def get_user_tweets(api, id, last_seen, username = None):
    if username != None:
        print("Getting tweets for {}...".format(str(username)))
    else:
        print("Getting tweets for {}...".format(str(id)))

    tweets = api.user_timeline(id, since_id = int(last_seen))
    tweets.reverse()
    return tweets

# Filters tweets
def tweet_filters(tweet, filter = 0):
    filter = int(filter)
    # Filter explained:
    # 0 - Send all tweets
    # 1 - Send all tweets only with images / gifs / videos
    # 2 - Send all tweets only with text

    # Checks if tweet is valid
    if tweet.retweeted == False and tweet.in_reply_to_status_id == None and not tweet.text.startswith('RT @'):

        # Checks if tweet passes Filters
        if filter == 0:
            return True

        if filter == 1:
            if 'media' in tweet.entities:
                print(tweet.text)
                return True

        if filter == 2:
            if 'media' not in tweet.entities:
                return True
        else:
            print("No correct filter detected")
            return False

    return False
