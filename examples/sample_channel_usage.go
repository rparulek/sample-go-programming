package main

import "fmt"


func send_call(sender_channel chan<- string, msg string) {

    fmt.Println("Copying message into the sender channel")
    sender_channel<- msg
}

func recv_call(recv_channel chan<- string, sender_channel <-chan string) { 

    fmt.Println("Passing message to the receiver channel")
    msg := <-sender_channel
    recv_channel<- msg
}

func main() {
    var header string = "Channel direction usage in GO programming"
    fmt.Println(header)
    sender_channel := make(chan string, 1)
    recv_channel := make(chan string, 1)
    send_call(sender_channel, "Message passage from sender to receiver channel")
    recv_call(recv_channel,sender_channel)
    fmt.Println(<-recv_channel)
}
