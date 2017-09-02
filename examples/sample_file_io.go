package main

import (
  "bufio"
  "fmt"
  "log"
  "os"
  "strings"
)

// readLines reads a whole file into memory
// and returns a slice of its lines.
func readLines(path string) ([]string, error) {
  file, err := os.Open(path)
  if err != nil {
    return nil, err
  }
  defer file.Close()

  var lines []string
  scanner := bufio.NewScanner(file)

  for scanner.Scan() {
    lines = append(lines, scanner.Text())
  }
  return lines, scanner.Err()
}

// writeLines writes the lines to the given file.
func writeLines(lines []string, path string) error {
  file, err := os.Create(path)
  if err != nil {
    return err
  }
  defer file.Close()

  w := bufio.NewWriter(file)
  for _, line := range lines {
    fmt.Fprintln(w, line)
  }

  //Logic to split the contents of file delimited by a space and store them into a new slice element
  var tmp_str string
  tmp_str = lines[0]
  split_slice := strings.Split(tmp_str," ")
  fmt.Println("Forming a new slice with contents from file delimited by a space")
  for x:=1; x<len(lines); x++ {

    split_slice = append(split_slice,lines[x])

  }
  fmt.Println(split_slice)

  return w.Flush()
}

func main() {

  var header string = "File I/O Operations in GO and copying file contents into slices"
  fmt.Println(header)
  
  lines, err := readLines("sample-input.txt")
  if err != nil {
    log.Fatalf("readLines: %s", err)
  }
  for i, line := range lines {
    fmt.Println(i, line)
  }

  if err := writeLines(lines, "sample-output.txt"); err != nil {
    log.Fatalf("writeLines: %s", err)
  }
}
