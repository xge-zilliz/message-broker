import pulsar
from pulsar import ConsumerType

# TODO: use a common function in project
def get_result_topic_name(client_id: int):
    topic = "result-topic" + str(client_id)
    return topic

class Consumer:
    def __init__(self, client: pulsar.Client, client_id: int):
        self._client = client
        self._client_id = client_id

    def subscribe_result(self, num_of_result: int):
        assert num_of_result >= 0
        topic = get_result_topic_name(self._client_id)

        consumer = self._client.subscribe(topic=topic,
                                          subscription_name=topic,
                                          consumer_type=ConsumerType.Shared)

        result = []
        i = 0

        while True:
            msg = consumer.receive()
            ex = msg.value()
            try:
                print("Received result {}".format(ex))
                # Acknowledge successful processing of the message
                consumer.acknowledge(msg)
                result.append(ex)
                i = i + 1
            except:
                # Message failed to be processed
                consumer.negative_acknowledge(msg)

            # TODO: use a better way to break consuming
            if i >= num_of_result:
                break

        return result
