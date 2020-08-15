package conf


import (
	"bufio"
	"fmt"
	"io"
	"message-broker/server/milvus/tool"
	"os"
	"strings"
)


type InitConf struct {
	topics tool.Vector
}

//读取key=value类型的配置文件
func InitConfig(path string) map[string] InitConf{
	config := make(map[string]InitConf)

	f, err := os.Open(path)
	defer f.Close()
	if err != nil {
		panic(err)
	}

	r := bufio.NewReader(f)
	for {
		b, _, err := r.ReadLine()
		if err != nil {
			if err == io.EOF {
				break
			}
			panic(err)
		}
		s := strings.TrimSpace(string(b))
		index := strings.Index(s, "=")
		if index < 0 {
			continue
		}
		key := strings.TrimSpace(s[:index])

		if len(key) == 0 {
			continue
		}

		if _, ok := config[key]; !ok {
			topic := *(tool.New(10))
			conf := *(new(InitConf))
			conf.topics = topic
			config[key] = conf
		}
		value := strings.TrimSpace(s[index+1:])
		if len(value) == 0 {
			continue
		}
		topics := config[key].topics
		topics.Append(value)
		fmt.Println(topics)
	}
	fmt.Println(config["topics"])
	return config
}