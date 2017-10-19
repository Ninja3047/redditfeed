# Reddit Feed

# Overview
When my application receives a request through the API endpoint,
it first checks if the data is already cached in Redis. If so, it
will return the information it has in the cache. The information
from Reddit is only cached for a minute in order to make the application
respond to requests more quickly and to not repeatedly make the same calls
to Reddit to avoid rate limiting. If the information is not already cached,
then my application makes a call to Reddit and then sanitizes the input it
receives.

# Instructions for Running

1. Install docker + docker compose
2. Clone this repository
3. Run `docker-compose up`
4. You should now be able to query the API locally
5. You can optionall set up an nginx reverse proxy to forward the requests
   to the correct port

# Example Usage

```
http://127.0.0.1/api/v1/top_articles/<subreddit>
```

# Instructions for Development

1. Clone this repository
2. Set up a python3 virtual environment
3. `pip install -r requirements.txt`

# Running Tests

1. Set up development environment
2. Run `nosetests`

# Demo

https://redditfeed.foobar.network/api/v1/top_article/news
