package main

import (
    "log"
    "io"
    "net/http"
    "io/ioutil"
    "fmt"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

       body, err := ioutil.ReadAll(r.Body)
       if err == nil {
           io.WriteString(w, string(body))
           fmt.Println(string(body))
       }
    })

    log.Fatal(http.ListenAndServe(":8085", nil))
}
