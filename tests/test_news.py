""" Test example from /r/news """
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
@patch('redditfeed.redditfeed.redis.Redis.get')
@patch('redditfeed.redditfeed.redis.Redis.set')
def test_news(mock_red_set, mock_red_get, mock_req):
    """ Test example from /r/news """
    with open(test_dir + '/news_input.json', 'r') as f:
        mock_req.return_value.status_code = 200
        mock_req.return_value.json.return_value = json.loads(f.read())
    with open(test_dir + '/news_output.json', 'r') as f:
        expected = json.loads(f.read())
    mock_red_get.return_value = None

    ret = app.get('/api/v1/top_article/news')
    api_response = json.loads(ret.data)
    for i in range(len(api_response['results'])):
        for key in expected['results'][i]:
            assert_equal(api_response['results'][i][key],
                         expected['results'][i][key])
