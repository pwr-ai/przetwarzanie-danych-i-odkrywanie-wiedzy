import praw
import streamlit as st
import statsd
import tomllib


# load configuration from file
with open("client_config.toml", "rb") as f:
   config = tomllib.load(f)

# add graphite statsd client
stats = statsd.StatsClient('graphite', 8125)

# count spawns
stats.incr('rising_reddit_memes.spawned')

# make reddit client
reddit = praw.Reddit(client_id=config["reddit"]["client_id"],
                     client_secret=config["reddit"]["client_secret"], 
                     password=config["reddit"]["password"],
                     user_agent=config["reddit"]["user_agent"],
                     username=config["reddit"]["username"])

# make streamlit radio button with subreddit names
subreddit_name = st.radio('What kind of memes do you like?', ['meme', 'aww', 'funny', 'polandball', 'MemesIRL'])
# make streamlit slider with number of memes
memes_count = st.slider("How many memes you want to see?", 1, 10)

# make subreddit object
subreddit = reddit.subreddit(subreddit_name)
# retrieve number of memes + 1 rising posts
retrieved_memes = subreddit.rising(limit=memes_count + 1)

# plot until numer of plots == memes_count
# or until no more memes
plotted_meme_count = 0
for meme in retrieved_memes:
   # count requests
   stats.incr('rising_reddit_memes.requests')
   # check if meme is image
   if (
      meme is not None and
      meme.url.endswith(('jpg', 'jpeg', 'png'))
      ):
         # plot meme and increment counter
         st.image(meme.url)
         plotted_meme_count += 1
   # check if we reached memes_count
   if plotted_meme_count >= memes_count:
      break