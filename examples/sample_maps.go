package main

import "fmt"

func add_map_elements(capital map[string]string) map[string]string {

    capital["NC"] = "Raleigh"
    capital["NJ"] = "Trenton"
    capital["GA"] = "Atlanta"
    capital["MA"] = "Boston"

    return capital
}

func main() {
    var header string = "Maps in GO programming"
    fmt.Println(header)
    capital_map := make(map[string] string)
    fmt.Println("Adding state and capitals in a map")
    capital_map = add_map_elements(capital_map)
    fmt.Println(capital_map)
}
