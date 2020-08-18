package conf

import "message-broker/server/milvus/tool"

type Op int
const (
	insert Op =0
	delete Op =1
	update Op =2
	query  Op =3
)

type Message struct {
	clientId  int64
	id        int64
	operation Op
	vector    tool.Vector
}