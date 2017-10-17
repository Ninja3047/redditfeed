""" Test malformed JSON from Reddit """
import json
import os
from unittest.mock import patch, MagicMock
import redis
from nose.tools import assert_equal

from redditfeed import redditfeed


app = redditfeed.app.test_client()
test_dir = os.path.dirname(os.path.abspath(__file__))

redis.Redis.get.return_value = None
redis.Redis.set = MagicMock()


@patch('redditfeed.redditfeed.requests.get')
def test_malformed_json(mock_req):
    """ Tests malformed JSON from Reddit """
    mock_req.return_value.status_code = 200
    mock_req.return_value.json.return_value = '"{}"'
    ret = app.get('/api/v1/top_article/friends')
    api_response = json.loads(ret.data)
    assert_equal(api_response['message'], "Reddit didn't give us json :(")
    assert_equal(api_response['error'], 500)
