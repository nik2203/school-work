var http = require('http');
var fs = require('fs');
var url = require('url');
var qs = require('querystring')

http.createServer(function(request,response){
    if(request.method=='GET'){
        response.writeHead(200,{"Content-type":"text/html"})
        var myurl = url.parse(request.url)
        var filename = myurl.pathname

        fs.readFile(filename.substring(1), 'utf-8', function(err,data){
            if(err){
                response.writeHead(404,{"Coontent-type":"text/html"})
            }
            else{
                response.writeHead(200,{"Content-type":"text/html"})
                response.write(data)
                response.end()
            }
        });
    }
    if(request.method=='POST'){
        
    }
}).listen(8080)
console.log("Server is running");