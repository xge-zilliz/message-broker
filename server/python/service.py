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
   service_client = ServerClient(url=config_param["brokerServiceUrl"],
                                 topics=config_param["topics"].split(','),
                                 token=config_param["token"],
                                 subscription_name=config_param["subscriptionName"])
   service_client.redeliver_message()
