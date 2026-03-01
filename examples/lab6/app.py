from flask import Flask, render_template
import os
import praw
import tomllib
import statsd


with open("client_config.toml", "rb") as f:
   config = tomllib.load(f)

# dzięki użyciu Docker Compose, możemy w kodzie odwoływać się do nazw kontenerów zamiast adresów IP - Docker rozwiąże adresy sam za nas

stats = statsd.StatsClient('graphite', 8125)

app = Flask(__name__)
reddit = praw.Reddit(client_id=config["reddit"]["client_id"],
                     client_secret=config["reddit"]["client_secret"], 
                     password=config["reddit"]["password"],
                     user_agent=config["reddit"]["user_agent"],
                     username=config["reddit"]["username"])

@stats.timer('rising_reddit_memes.request_times')
@app.route("/")
def index():
    # mierzymy ilość wywołań tej funkcji
    stats.incr('rising_reddit_memes.requests')
    subreddit = reddit.subreddit("aww")
    meme = next(subreddit.rising(limit=1))
    return render_template("index.html", url=meme.url)


if __name__ == "__main__":
    stats.incr('rising_reddit_memes.spawned')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
