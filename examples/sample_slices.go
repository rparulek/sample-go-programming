package main

import "fmt"

func append_employers(employer[]string) []string {

    //Adding contents to employer slice
    employer = append(employer, "Nuage")
    employer = append(employer, "Nutanix")
    employer = append(employer, "Mirantis")
    employer = append(employer, "RedHat")

    return employer
}

func delete_employers(employer[]string) []string {

    //Clearing the employer slice
    employer = nil

    return employer
}

func main() {
    var header string = "Slices in GO programming"
    fmt.Println(header)
    employer_slice := make([]string, 4)
    fmt.Println("Creating employer slice in GO")
    employer_slice = append_employers(employer_slice)
    fmt.Println("Employers:", employer_slice)

    fmt.Println("Deleting employer slice contents in GO")
    employer_slice = delete_employers(employer_slice)
    fmt.Println("Employers:", employer_slice)
}
