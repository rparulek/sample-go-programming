package main

import "fmt"
import "sync"
import "time"

var wg sync.WaitGroup
var counter int
var mutex sync.Mutex

func main() {

        wg.Add(2)
        go incrementCounterTeamOne()
        go incrementCounterTeamTwo()
        wg.Wait()
	fmt.Println("Final value for counter is", counter)
}

func incrementCounterTeamOne() {

        for i := 0; i < 20; i++ {
		incCounter("Team 1")
                fmt.Println("Current value for counter: team 1", counter)
		time.Sleep(time.Duration(2) * time.Second)
        }
        wg.Done()
}

func incrementCounterTeamTwo() {

        for i := 0; i < 20; i++ {
		incCounter("Team 2")
                fmt.Println("Current value for counter: team 2", counter)
		time.Sleep(time.Duration(2) * time.Second)
        }
        wg.Done()
}

func incCounter(team string) {

	mutex.Lock()
	fmt.Println(team, "acquired lock and incrementing counter")
	counter++
	mutex.Unlock()

}
