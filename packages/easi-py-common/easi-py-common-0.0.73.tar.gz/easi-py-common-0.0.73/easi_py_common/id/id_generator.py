from redis import StrictRedis


class RedisIdGenerator:
    def __init__(self, redis: StrictRedis, lua_sha: str):
        """
        构造RedisIdGenerator实例
        :param redis: 可以是原生的StrictRedis实例，也可以是FlaskRedis实例，因为FlaskRedis直接继承了所有StrictRedis的属性
        :param lua_sha: lua脚本的sha值
        """
        self.redis = redis
        self.lua_sha = lua_sha
        # 算法时间戳开始时间2021-05-14 00:00:00
        self.epoch = 1620921600000

    def next_id(self, service_name: str) -> int:
        """
        生成分布式唯一ID
        :param service_name: 服务名称，可随意定义
        :return:
        """
        ret = self.redis.evalsha(self.lua_sha, 1, service_name)
        second = ret[0]
        micro_second = ret[1]
        seq = ret[3]
        milli_second = second * 1000 + int(micro_second / 1000)
        return (milli_second - self.epoch) << (12 + 10) + seq
