package conf

import (
	"bufio"
	"io"
	"log"
	"message-broker/server/milvus/tool"
	"os"
	"strings"
)

//读取key=value类型的配置文件
func InitConfig(path string) map[string] tool.Vector{
	config := make(map[string]tool.Vector)

	f, err := os.Open(path)
	defer f.Close()
	if err != nil {
		log.Fatal(err)
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
			topic := tool.New(10)
			config[key] = *topic
		}
		value := strings.TrimSpace(s[index+1:])
		if len(value) == 0 {
			continue
		}
		vector := config[key]

		slicedValue := strings.Split(value, ",")
		for sIndex :=range slicedValue {
			vector.Append(slicedValue[sIndex])
		}
		config[key] = vector
	}
	return config
}