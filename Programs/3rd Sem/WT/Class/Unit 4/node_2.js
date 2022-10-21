var http = require("http");
var fetch = require("node-fetch");

//GET operation

fetch("http://127.0.0.1:8080",{
    method: "GET",
    headers: {"Content-type":"application/json"}
})
.then((res)=>res.json())
.then(res=>console.log(res))

//POST operation
fetch("http:127.0.0.1:8080/newdb",{
    method: "GET",
    headers: {"Content-type":"application/json"},
    body: JSON.stringify({})
})