package main

import "fmt"

//geometry is of interface type that includes 
// area and perimeter functions of Rect
// and Circle structures

type geometry interface {
    area() float64
    perimeter() float64
}

type Rect struct {
    length float64
    breadth float64
}

type Circle struct {
    radius float64
}

//Implementing "area" and "perimeter" functions of
//geometry interface defined above using Rect and 
//Circle structures

func (r Rect) area() float64 {

    return r.length * r.breadth
}

func (c Circle) area() float64 {

    return 3.1425 * c.radius * c.radius
}

func (r Rect) perimeter() float64 {

    return 2 * (r.length + r.breadth)
}

func (c Circle) perimeter() float64 {

    return 2 * 3.1425 * c.radius
}

func measure(g geometry) {

    fmt.Println("Area:")
    fmt.Println(g.area())
    fmt.Println("Perimeter:")
    fmt.Println(g.perimeter())

}

func main() {

    rect_obj := Rect{length : 10.0, breadth : 11.0}
    circle_obj := Circle{radius : 5.0}

    fmt.Println("Area and Perimeter calculations for Rectangle structure")

    //Function measure() called with arguments as Rect and Circle struct
    //objects. This is possible since we have implemented "geometry" interface's
    // functions "area" and "perimeter" using these structs
    measure(rect_obj)

    fmt.Println("Area and Perimeter calculations for Circle structure")
    measure(circle_obj)

}
