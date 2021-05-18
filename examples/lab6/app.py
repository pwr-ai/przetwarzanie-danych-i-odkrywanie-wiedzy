from flask import Flask, render_template
import os
import random
import praw

import statsd

# dzięki użyciu Docker Compose, możemy w kodzie odwoływać się do nazw kontenerów zamiast adresów IP - Docker rozwiąże adresy sam za nas

stats = statsd.StatsClient('graphite', 8125)

app = Flask(__name__)
reddit = praw.Reddit(client_id='WdgsSyHEDgL8_g',
                     client_secret='Mqs5rCsVze9iNM3QrmqjXDNulCBYxg', 
                     password="aaa111bbb222",
                     user_agent='meme_displayer',
                     username='SecretCauliflower665')

@stats.timer('random_reddit_memes.request_times')
@app.route("/")
def index():
    # mierzymy ilość wywołań tej funkcji
    stats.incr('random_reddit_memes.requests')
    subreddit = reddit.subreddit("aww")
    meme = subreddit.random()
    return render_template("index.html", url=meme.url)


if __name__ == "__main__":
    stats.incr('random_reddit_memes.spawned')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5473)))
