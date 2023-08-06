import json
from .iot_topic_thing import IoTopicThing


class IoThingPropertyDesired(IoTopicThing):

    """
    设备属性期望值-设备侧实现
    """

    def get_post_topic(self):
        """
        属性期望值-请求 Topic
        """
        return "/sys/%s/%s/thing/property/desired/get" % (self.product_key, self.device_name)

    def get_post_payload_data(self, prop):
        """
        属性期望值-请求参数
        {
            "id" : "123",
            "version":"1.0",
            "sys":{
                "ack":0
            },
            "params" : [
                "power",
                "temperature"
            ],
            "method":"thing.property.desired.get"
        }
        """
        payload = {
            "sys": {
                "ack": 1
            },
            "params": prop,
            "method": "thing.property.desired.get"
        }
        payload =  json.dumps(payload)
        # print(payload)
        return payload

    def get_subscribe_topic(self):
        """
        属性期望值-应答回复
        """
        return "/sys/%s/%s/thing/property/desired/get_reply" % (self.product_key, self.device_name)
