from easi_py_common.core.redis import redis_store


class RedisIdGenerator:
    lua_script = """
    -- need redis 3.2+
    redis.replicate_commands();

    local prefix = '__idgenerator_';
    local partitionCount = 4096;
    local step = 3;
    local startStep = 0;

    local tag = KEYS[1];
    -- if user do not pass shardId, default partition is 0.
    local partition
    if KEYS[2] == nil then
      partition = 0;
    else
      partition = KEYS[2] % partitionCount;
    end

    local now = redis.call('TIME');

    local miliSecondKey = prefix .. tag ..'_' .. partition .. '_' .. now[1] .. '_' .. math.floor(now[2]/1000);

    local count;
    repeat
      count = tonumber(redis.call('INCRBY', miliSecondKey, step));
      if count > (1024 - step) then
          now = redis.call('TIME');
          miliSecondKey = prefix .. tag ..'_' .. partition .. '_' .. now[1] .. '_' .. math.floor(now[2]/1000);
      end
    until count <= (1024 - step)

    if count == step then
      redis.call('PEXPIRE', miliSecondKey, 5);
    end

    -- second, microSecond, partition, seq
    return {tonumber(now[1]), tonumber(now[2]), partition, count + startStep}
    """
    epoch = 1620921600000

    def __init__(self):
        self.cmd = redis_store.register_script(self.lua_script)

    def next_id(self, service_name: str) -> int:
        """
        生成分布式唯一ID
        :param service_name: 服务名称，可随意定义
        :return:
        """
        ret = self.cmd(keys=["service_name"], args=[service_name])
        second = ret[0]
        micro_second = ret[1]
        seq = ret[3]
        milli_second = second * 1000 + int(micro_second / 1000)
        return (milli_second - self.epoch) << (12 + 10) + seq
