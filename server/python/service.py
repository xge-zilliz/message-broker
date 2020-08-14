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
   service_client = ServerClient(config_param["brokerServiceUrl"],config_param["topics"].split(','))
   service_client.redeliver_message()
