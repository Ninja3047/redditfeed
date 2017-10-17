import json
import os
import redis
from unittest.mock import patch, MagicMock
from nose.tools import assert_equal

from redditfeed import redditfeed


app = redditfeed.app.test_client()
test_dir = os.path.dirname(os.path.abspath(__file__))

redis.Redis.get.return_value = None
redis.Redis.set = MagicMock()

@patch('redditfeed.redditfeed.requests.get')
def test_not_found(mock_req):
    with open(test_dir + '/error.json', 'r') as f:
        mock_req.return_value.status_code = 404
        mock_req.return_value.json.return_value = json.loads(f.read())
    ret = app.get('/api/v1/top_article/hello%20world')
    api_response = json.loads(ret.data)
    assert_equal(api_response['message'], "Not found")
    assert_equal(api_response['error'], 404)
