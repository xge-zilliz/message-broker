package main

import (
	"fmt"
	"message-broker/server/milvus/conf"
	"message-broker/server/milvus/querynode/pulsar"
)

func main() {
	conf := conf.InitConfig("/home/xge/go/src/message-broker/server/milvus/conf/message_broker.conf")
	fmt.Println(conf)
	pulsar.Consumer()
}