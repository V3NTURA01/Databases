"""Base de datos para sensores y ubicaciones"""
import sqlite3

db_name = "Proyecto.db"

table_schema = """
    drop table if exists Ubicaciones;
    
    create table Ubicaciones(
        UbicacionID integer not null primary key autoincrement,
        Ubicacion nvarchar(10) not null
    );
    
    drop table if exists Sensores;
    
    create table Sensores(
        SensorID integer not null primary key autoincrement, 
        NombreSensor nvarchar(10) not null,
        UbicacionID integer not null,
        foreign key(UbicacionID) references Ubicaciones(UbicacionID)
    );

    drop table if exists Alertas;

    create table Alertas(
        alertaID integer not null primary key autoincrement,
        tipoAlerta nvarchar(10) not null,
        sensorID integer not null,
        foreign key(sensorID) references Sensores(SensorID)
    );

    drop table if exists Lecturas;

    create table Lecturas(
        lecturaID integer not null primary key autoincrement,
        lecturaValor real not null
    );
"""

con = sqlite3.connect(db_name)
cursor = con.cursor()

sqlite3.complete_statement(table_schema)
cursor.executescript(table_schema)

cursor.close()
con.close()
