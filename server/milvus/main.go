package main

import (
	"fmt"
	"message-broker/server/milvus/conf"
)

func main() {
	conf := conf.InitConfig("/home/xge/go/src/message-broker/server/milvus/conf/message_broker.conf")
	fmt.Println(conf)
}