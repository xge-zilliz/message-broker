package storage

import "C"
import (
	"fmt"
	"time"
)

type Message struct {
	time time.Time
	value [2]int
	id int
}

var data = make(map[string]Message)

func Find(k string) *Message {
	_, ok := data[k]
	if ok {
		value := data[k]
		return &value
	} else {
		return nil
	}
}

func Add(k string, v Message) bool {
	if k == "" {
		return false
	}
	if Find(k) == nil {
		data[k] = v
		return true
	}
	return false
}

func Delete(k string) bool {
	if Find(k) != nil {
		delete(data,k)
		return true
	}
	return false
}

func Update(k string, v Message) bool {
	//TODO:: if k doesn't exist
	data[k] = v
	return true
}

func PrintMap() {
	for k, v := range data {
		fmt.Println("key: ", k, "value: ", v)
	}
}