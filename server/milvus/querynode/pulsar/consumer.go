package pulsar

import (
	"context"
	"fmt"
	"github.com/apache/pulsar-client-go/pulsar"
	"github.com/prometheus/common/log"
	"time"
)

func consumer() {
	client, err := pulsar.NewClient(pulsar.ClientOptions{
		URL:               "pulsar://localhost:6650",
	})

	defer client.Close()

	if err != nil {
		log.Fatal("Could not instantiate Pulsar client: %v", err)
	}

	topic1 := "topic_insert"
	topic2 := "topic_delete"
	topic3 := "topic_info"

	topics := []string{topic1, topic2, topic3}
	options := pulsar.ConsumerOptions{
		Topics:           topics,
		SubscriptionName: "multi-topic-sub",
		Type:             pulsar.KeyShared,
	}

	consumer, err := client.Subscribe(options)
	defer consumer.Close()
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel()
	for {                                                   // for recieve
		msg, err := consumer.Receive(ctx)
		fmt.Println("msg: ", msg)
		if err != nil {
			log.Fatal(err)
			consumer.Nack(msg)  //ack the failure
		}
		consumer.Ack(msg)
	}


	//channel := make(chan pulsar.ConsumerMessage, 100)
	//options.MessageChannel = channel
	//consumer, err := client.Subscribe(options)
	//defer consumer.Close()                     //channel consumer listener
	//for cm := range channel {
	//	msg := cm.Message
	//	fmt.Println("msg: ", msg)
	//	consumer.Ack(msg)
	//}

	if err := consumer.Unsubscribe(); err != nil {
		log.Fatal(err)
	}

	defer client.Close()
}