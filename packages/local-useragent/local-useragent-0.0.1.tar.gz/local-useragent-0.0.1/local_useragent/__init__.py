from fake_useragent import UserAgent
import tempfile
import os
import json

from . import cache

__cache_path = os.path.join(tempfile.gettempdir(), 'fake_useragent_create.json')

with open(__cache_path, 'w') as f:
    json.dump(cache.fake_cache, f)

user_agent = UserAgent(use_cache_server=False, path=__cache_path, verify_ssl=False)
