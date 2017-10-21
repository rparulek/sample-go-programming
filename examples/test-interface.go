package main

import "fmt"

type Student struct {
	Name string
	Marks int
}

func testInterface(data map[string]interface{}) {

	firstObj := data["rohan"].(Student)
	secondObj := data["aditi"].(Student)
	fmt.Println(firstObj.Name)
	fmt.Println(firstObj.Marks)
        fmt.Println(secondObj.Name)
        fmt.Println(secondObj.Marks)
}

func main() {

	data := make(map[string]interface{})
	
	s1 := Student{"Rohan", 100}
	s2 := Student{"Aditi", 200}

	data["rohan"] = s1
	data["aditi"] = s2
	testInterface(data)
}
