package main

import "fmt"
import "sync"
import "time"

var wg sync.WaitGroup

func main() {

	wg.Add(2)
	go printTeamOne()
	go printTeamTwo()
	wg.Wait()
}

func printTeamOne() {

	for i := 0; i < 20; i++ {
		fmt.Println("Team 1 executing job", i)
		time.Sleep(time.Duration(2) * time.Second)
	}
	wg.Done()
}

func printTeamTwo() {

        for i := 0; i < 20; i++ {
                fmt.Println("Team 2 executing job", i)
		time.Sleep(time.Duration(4) * time.Second)
        }
        wg.Done()
}
