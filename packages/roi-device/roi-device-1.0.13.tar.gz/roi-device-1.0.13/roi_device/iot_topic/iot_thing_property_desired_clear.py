import json
from .iot_topic_thing import IoTopicThing


class IoThingPropertyDesiredClear(IoTopicThing):

    """
    设备属性期望值-设备侧实现
    """

    def get_post_topic(self):
        """
        属性期望值-请求 Topic
        """
        return "/sys/%s/%s/thing/property/desired/delete" % (self.product_key, self.device_name)

    def get_post_payload_data(self, prop, prop_vision=-1):
        """
        属性期望值-请求参数，见开发文档
        只实现了单个属性删除，多个多次调用
        """
        params = {
            "version": prop_vision
        }
        payload = {
            "sys": {
                "ack": 1
            },
            "params": {},
            "method": "thing.property.desired.delete"
        }
        if prop_vision == -1:
            payload["params"] = {
                prop: {}
            }
        else:
            payload["params"] = {
                prop: params
            }
        payload = json.dumps(payload)
        # print(payload)
        return payload

    def get_subscribe_topic(self):
        """
        属性期望值-应答回复
        """
        return "/sys/%s/%s/thing/property/desired/delete_reply" % (self.product_key, self.device_name)
