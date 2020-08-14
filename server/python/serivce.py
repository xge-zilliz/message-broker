import configparser
import sys
from server_client.server_client import ServerClient


def get_config(filepath):
    cf = configparser.ConfigParser()
    cf.read(filepath)
    return cf["TopicConfig"]


if __name__ == "__main__":
   filepath = sys.argv[1]
   config_param = get_config(filepath)
   service_client = ServerClient(config_param["brokerServiceUrl"])
   service_client.redeliver_message(token=config_param["token"],
                                    consumer_topic=config_param["consumerTopic"],
                                    produce_topic=config_param["produceTopic"],
                                    subscription_name=config_param["subscriptionName"])