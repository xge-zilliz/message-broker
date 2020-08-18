package pulsar

import (
	"context"
	"fmt"
	"github.com/apache/pulsar/pulsar-client-go/pulsar"
	"log"
	"time"
)

type testMessage struct {
	clientId int64
	op string
}

var (
	SchemaDef = "{\"type\":\"record\",\"name\":\"message\",\"namespace\":\"test\"," +
		"\"fields\":[{\"name\":\"clientId\",\"type\":\"int\"},{\"name\":\"op\",\"type\":\"string\"}]}"
)

func Consumer() {
	client, err := pulsar.NewClient(pulsar.ClientOptions{
		URL:               "pulsar://localhost:6650",
	})

	defer client.Close()

	if err != nil {
		//log.Fatal("Could not instantiate Pulsar client: %v", err)
		fmt.Println(err)
	}

	topic1 := "topic_insert"
	//topic2 := "topic_delete"
	//topic3 := "topic_info"
	//
	//topics := []string{topic1, topic2, topic3}
	//options := pulsar.ConsumerOptions{
	//	Topics:           topics,
	//	SubscriptionName: "multi-topic-sub",
	//	Type:             pulsar.KeyShared,
	//}

	options := pulsar.ConsumerOptions{
		Topic:           topic1,
		SubscriptionName: "my-sub",
		Type:             pulsar.KeyShared,
	}

	obj := testMessage{}
	asConsumer := pulsar.NewAvroSchema(SchemaDef, nil)
	consumer, err := client.SubscribeWithSchema(options, asConsumer)

	defer consumer.Close()
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Millisecond)
	defer cancel()
	for {                                                   // for recieve
		msg, err := consumer.Receive(ctx)
		fmt.Println("msg: ", msg)
		if err != nil {
			log.Fatal(err)
			consumer.Nack(msg)  //ack the failure
		}
		err  = msg.GetValue(&obj)
		if err != nil {
			log.Fatal(err)
			consumer.Nack(msg)  //ack the failure
		}
		fmt.Println("client_id: ", obj.clientId)
		fmt.Println("op: ", obj.op)
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
}