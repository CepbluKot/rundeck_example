from redis import Redis as Redis_sync
from aioredis import Redis as Redis_async


redis_sync = Redis_sync(host='redis', port=6379)
redis_async = Redis_async(host='redis', port=6379)
