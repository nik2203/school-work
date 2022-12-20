const { prototype } = require("events");

function vehicle(){
    this.name = "Hyundai"
    this.year = 2019;
}

let car = new vehicle();

console.log(car.name,car.year);

vehicle.prototype.year=2020;vehicle.prototype.color = "blue";
