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

# Instructions

1. Install docker + docker compose
2. Navigate to the directory
3. Run `docker-compose up`
4. You should now be able to query the API locally

```
http://127.0.0.1/api/v1/top_articles/<subreddit>
```

# Running Tests

```
nosetests
````

# Demo

https://redditfeed.foobar.network/api/v1/top_articles/<subreddit>
