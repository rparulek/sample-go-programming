package main

import "fmt"

func main() {
    var header string = "Channel synchronization usage in GO programming"
    fmt.Println(header)
    job_channel := make(chan int, 5)
    status_channel := make(chan bool)

    go func() {

        for {
            //Check status of the job channel if it has been closed
            job_id, status := <- job_channel
            if status {
                fmt.Println("Processing job id", job_id)
            } else {
                //This code will execute when the status of channel is closed
                fmt.Println("Job submission channel has been closed")
                status_channel <- true
                return
            }
        }
    }()

    for j := 1; j < 6; j++ {

        //Submitting job ids to job channel
        job_channel <- j
        fmt.Println("Submitted for processing job id", j)
    }

    close(job_channel)
    fmt.Println("Submitted all jobs for processing")

    <-status_channel
}
