from flask import Flask, render_template
import os
import random
from memelib.api import DankMemeClient

import statsd

# dzięki użyciu Docker Compose, możemy w kodzie odwoływać się do nazw kontenerów zamiast adresów IP - Docker rozwiąże adresy sam za nas

stats = statsd.StatsClient('graphite', 8125)

app = Flask(__name__)
myclient = DankMemeClient()

# mierzymy czas wykonania tej funkcji
@stats.timer('random_reddit_memes.request_times')
@app.route("/")
async def index():
    # mierzymy ilość wywołań tej funkcji
    stats.incr('random_reddit_memes.requests')
    meme_dict = await myclient.async_meme(subreddit="dankmemes")
    return render_template("index.html", url=meme_dict['img_url'])


if __name__ == "__main__":
    stats.incr('random_reddit_memes.spawned')
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
