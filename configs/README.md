# ABOUT users.dat:
\[Alias\] \[ID\] \[Filter Mode\]

- **Alias** is a name given to the user by you
- **ID** is the user's twitter account ID
- **Filter Mode** determines what content the bot should send you

# Filters:
- 0 - Send all tweets
- 1 - Send all tweets only with images / gifs / videos
- 2 - Send all tweets only with text. Tweets with images, gifs and videos will be ignored.

Insert the ID of a user on each line.
Example:
Twitter 783214 0
ScienceShitposts 1217558172929380352 1
PyroCynical 21491779566452490245 2

*If you try to add more content, the bot will cry in the output*

# About last_seen.dat
last_seen.dat is a file that saves the last tweet read by the bot. This prevents the bot from sending you hundreds of tweets at a time.
It gets automatically updated, so please do not touch it.
