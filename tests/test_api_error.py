import json
import os
from unittest.mock import patch, MagicMock
from nose.tools import assert_equal

from redditfeed import redditfeed


app = redditfeed.app.test_client()
test_dir = os.path.dirname(os.path.abspath(__file__))


@patch('redditfeed.redditfeed.requests.get', autospec=True)
@patch('redditfeed.redditfeed.redis.Redis.get', autospec=True)
@patch('redditfeed.redditfeed.redis.Redis.set', autospec=True)
def test_not_found(mock_red_set, mock_red_get, mock_req):
    with open(test_dir + '/error.json', 'r') as f:
        mock_req.return_value.status_code = 404
        mock_req.return_value.json.return_value = json.loads(f.read())
    mock_red_get.return_value = None

    ret = app.get('/api/v1/top_article/hearthstone')
    api_response = json.loads(ret.data)
    assert_equal(api_response['message'], "Not found")
    assert_equal(api_response['error'], 404)
