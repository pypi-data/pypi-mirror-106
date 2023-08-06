from easi_py_common.id.id_generator import RedisIdGenerator


class IdGenerator:
    @classmethod
    def install(cls, provider: str):
        """
        安装IdGenerator
        :param provider: 当前可取值redis
        :return:
        """
        assert provider in ["redis"]
        if provider == "redis":
            cls.instance = RedisIdGenerator()

    @classmethod
    def next_id(cls, *args, **kwargs):
        return cls.instance.next_id(*args, **kwargs)
