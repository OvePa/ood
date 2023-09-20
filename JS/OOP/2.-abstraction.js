class Circle:{
    #radius;
    #pi;

    constructor(radius=0){
        this.radius = radius;
        this.pi = 3.142
    }

    getArea(){
        return this.pi * Math.pow(this.radius,2);
    }

    getPerimeter(){
        return 2 * this.pi * this.radius;
    }
};

const circle = Circle(5);
console.log('Area: ' + circle.getArea().toFix(2));
console.log('Perimeter: '+ circle.getPerimeter().toFix(2));