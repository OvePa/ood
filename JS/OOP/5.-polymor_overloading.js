class Sum {
    addition(a, b, c = 0){
        return a + b + c;
    }
}

const sum = new Sum;
console.log(sum.addition(14, 35));
console.log(sum.addition(31, 34, 43));

/* ---------------------- */
class Area {
    calculateArea(length, breadth = -1) {
        if (breadth != -1)
            return length * breadth;
        else
            return length * length;
    }

}


let area = new Area;
console.log('Area of rectangle = ' + area.calculateArea(3, 4));
console.log('Area of square = ' + area.calculateArea(6));