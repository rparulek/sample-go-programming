package main

import "fmt"
import "time"

type EventType string
const (
	EtcdAddSubnet        EventType = "ETCD_ADD_SUBNET"
	EtcdDelSubnet        EventType = "ETCD_DEL_SUBNET"
	EtcdIncActiveIPCount EventType = "ETCD_INC_IP_COUNT"
	EtcdDecActiveIPCount EventType = "ETCD_DEC_IP_COUNT"
	EtcdAllocSubnetCIDR  EventType = "ETCD_ALLOC_SUBNET_CIDR"
	EtcdFreeSubnetCIDR   EventType = "ETCD_FREE_SUBNET_CIDR"
	EtcdUpdateSubnetID   EventType = "ETCD_UPDATE_SUBNET_ID"
	EtcdGetSubnetID      EventType = "ETCD_GET_SUBNET_ID"
	EtcdAddZone          EventType = "ETCD_ADD_ZONE"
	EtcdDeleteZone       EventType = "ETCD_DELETE_ZONE"
	EtcdUpdateZone       EventType = "ETCD_UPDATE_ZONE"
)

type EtcdRespObject struct {
	EtcdData interface{}
	Error    error
}

type EtcdEvent struct {
	Type               EventType
	EtcdReqObject      interface{}
	EtcdRespObjectChan chan *EtcdRespObject
}

func EtcdChanRequest(receiver chan *EtcdEvent, event EventType, params interface{}) *EtcdRespObject {
	etcdReq := &EtcdEvent{
		Type:          event,
		EtcdReqObject: params,
	}
	etcdReq.EtcdRespObjectChan = make(chan *EtcdRespObject)
	receiver <- etcdReq
	etcdResp := <-etcdReq.EtcdRespObjectChan
	return etcdResp
}

//Run starts the nuage etcd client and listens for events
func Run(etcdChannel chan *EtcdEvent) {
	for {
		select {
		case etcdEvent := <-etcdChannel:
			HandleEtcdEvent(etcdEvent)
		}
	}
}

func HandleEtcdEvent(event *EtcdEvent) {
	var data interface{}
	//var err error
	switch event.Type {
	case EtcdIncActiveIPCount:
                fmt.Println("Received a increment IP count command from client")
		data = "Will increment active IP count"
	case EtcdDecActiveIPCount:
		fmt.Println("Received a decrement IP count command from client")
		data = "Will decrement active IP count"
	case EtcdAddSubnet:
		fmt.Println("Received a add subnet command from client")
		data = "Will add subnet"
	case EtcdDelSubnet:
		fmt.Println("Received a delete subnet command from client")
		data = "Will delete subnet"
	}
	event.EtcdRespObjectChan <- &EtcdRespObject{EtcdData: data, Error: nil}
}

func main() {

	etcdChannel := make(chan *EtcdEvent)
	go Run(etcdChannel)

	for {
		resp := EtcdChanRequest(etcdChannel, EtcdIncActiveIPCount, "test")
		fmt.Println(resp.EtcdData.(string))
		resp = EtcdChanRequest(etcdChannel, EtcdDecActiveIPCount, "test")
		fmt.Println(resp.EtcdData.(string))
		resp = EtcdChanRequest(etcdChannel, EtcdAddSubnet, "test")
		fmt.Println(resp.EtcdData.(string))
		resp = EtcdChanRequest(etcdChannel, EtcdDelSubnet, "test")
		fmt.Println(resp.EtcdData.(string))
		time.Sleep(time.Duration(5) * time.Second)
	}
}
