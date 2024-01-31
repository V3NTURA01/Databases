var express = require('express')
var server = express()

//SQL
var sqlite3 = require('sqlite3');
var db = new sqlite3.Database('Proyecto.db')

//URLS
var url_body =  require('body-parser');
var url_encode = url_body.urlencoded({extended: false});

server.get('/extract', function (req, res){
    db.all('SELECT * FROM Ubicaciones', function(err, rows){
        if(err){
            console.log("Error: " + err);
        }else {
            console.log(rows);
            res.send(rows);
        }
    });
});

server.post('/miPost', url_encode, function(req, res){
    db.run('INSERT Into Ubicaciones(Ubicacion) VALUES (?)', req.body.Ubicacion,
    function(err, stat){
        if(err){
            console.log("Error: " + err);
        }else {
            console.log("Dato recibido: " + req.body.Ubicacion);
            res.send("Dato registrado correctamente");
        }   
    });
});

//db.run(' INSERT Into Ubicaciones(Ubicacion) VALUES ("Lab Fisica")');
//db.run(' INSERT Into Ubicaciones(Ubicacion) VALUES ("Enfermeria")');

server.get('/', function (req, res) {
    res.send("Hola perrillo");
});

server.get('/mi_pagina.html', function(req,res){
    res.sendFile(__dirname + "/" + "mi_pagina.html");
});

server.listen(5000, function(){
    console.log("Servidor ejecutandose");
});