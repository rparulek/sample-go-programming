package main

import "fmt"

type VM struct {
    name string
    ip  string
    uuid string
}

func (vm_obj VM) init_vm_by_value() VM {

    vm_obj.name = "Test-VM-1"
    vm_obj.ip = "192.168.10.2"
    vm_obj.uuid = "xxxxx-91264-9807"
    
    return vm_obj
}

func (vm_obj *VM) init_vm_by_ref() {

    vm_obj.name = "Test-VM-2"
    vm_obj.ip = "192.168.10.3"
    vm_obj.uuid = "xxxxx-91264-9000"

}

func main() {
    var header string = "Structures in GO programming"
    fmt.Println(header)
    vm_1 := VM{}
    //Passing and returning an entire struct by value
    vm_1 = vm_1.init_vm_by_value()
    fmt.Println("Structs passed by value")
    fmt.Println("VM details are")
    fmt.Println("VM Name: ", vm_1.name)
    fmt.Println("VM IP: ", vm_1.ip)
    fmt.Println("VM UUID: ", vm_1.uuid)

    //Passing and returning an entire struct by reference
    vm_2 := VM{}
    vm_ref_ptr := &vm_2
    vm_ref_ptr.init_vm_by_ref()
    fmt.Println("Structs passed by reference")
    fmt.Println("VM details are")
    fmt.Println("VM Name: ", vm_ref_ptr.name)
    fmt.Println("VM IP: ", vm_ref_ptr.ip)
    fmt.Println("VM UUID: ", vm_ref_ptr.uuid)
}
