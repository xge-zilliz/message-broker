package tool

type Vector struct {
	values []interface{}
}

func New(cap int) *Vector {
	this := new(Vector)
	this.values = make([]interface{}, 0, cap)
	return this
}

func (v *Vector) IsEmpty() bool {
	return len(v.values) == 0
}

func (v *Vector) Size() int {
	return len(v.values)
}

func (v *Vector) Append(value interface{}) bool {
	v.values = append(v.values, value)
	return true
}

func (v *Vector) Remove(index int) bool {
	if index < 0 || index >= len(v.values) {
		return false
	}
	v.values[index] = nil
	v.values = append(v.values[:index], v.values[index+1:]...)
	return true
}

func (v *Vector) GetValue(index int) interface{} {
	if index < 0 || index >= len(v.values) {
		return nil
	}
	return v.values[index]
}

func (v *Vector) SetValue(index int, value interface{}) bool {
	if index < 0 || index >= len(v.values) {
		return false
	}
	v.values[index] = value
	return true
}

//func main() {
//	vv := new(Vector)
//	vv.Append("sss")
//	fmt.Print(vv)
//}