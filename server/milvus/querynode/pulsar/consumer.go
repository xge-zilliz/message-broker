package pulsar

import (
	"github.com/apache/pulsar-client-go/pulsar"
	"github.com/prometheus/common/log"
	"time"
)

func consumer() {
	client, err := pulsar.NewClient(pulsar.ClientOptions{
		URL:               "pulsar://localhost:6650",
		OperationTimeout:  30 * time.Second,
		ConnectionTimeout: 30 * time.Second,
	})

	if err != nil {
		log.Fatal("Could not instantiate Pulsar client: %v", err)
	}
	defer client.Close()
}