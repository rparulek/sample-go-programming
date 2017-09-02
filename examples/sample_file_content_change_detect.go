package main

import "golang.org/x/exp/inotify"
import "fmt"
import "log"

func fileChangeDetect() {

watcher, err := inotify.NewWatcher()
if err != nil {
    log.Fatal(err)
}
err = watcher.Watch("/root/projects/go/src/changefile.txt")
if err != nil {
    log.Fatal(err)
}
for {
    select {
    case ev := <-watcher.Event:
        fmt.Println(ev)
    case err := <-watcher.Error:
        fmt.Println(err)
    }
}
}

func main() {

    fileChangeDetect()
}
