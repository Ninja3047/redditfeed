""" Reddit Feed API Web Application """
import json
from flask import Flask, jsonify
import requests
import redis

app = Flask(__name__)
cache = redis.Redis("redis", port=6379)


def get_top_article(subreddit, limit=20):
    """ Get top article and cache result into redis """
    params = {'limit': limit}
    headers = {'User-Agent': 'Redditfeed v0.2'}
    req = requests.get("https://reddit.com/r/%s/top.json" % (subreddit),
                       params=params, headers=headers)
    res = req.json()

    try:
        if res.get('data'):
            articles = res.get('data').get('children')
            keys = {'id', 'archived', 'title', 'url', 'score', 'created',
                    'author', 'over_18', 'gilded', 'downs', 'stickied',
                    'is_self', 'spoiler', 'permalink', 'locked', 'created',
                    'url', 'author', 'ups', 'num_comments'}
            return {'results':
                    [{key: entry.get('data').get(key) for key in keys}
                     for entry in articles]}
    except AttributeError:
        return {"message": "Reddit didn't give us json :(", "error": 500}

    return res


@app.route('/api/v1/top_article/<subreddit>')
def top_article(subreddit):
    """ API endpoint to get top article of a given subreddit """
    cached = cache.get(subreddit)
    if not cached:
        cached = get_top_article(subreddit)
        if not cached.get('error'):
            cache.set(subreddit, json.dumps(cached), ex=60)
    else:
        cached = json.loads(cached)
    return jsonify(cached)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
