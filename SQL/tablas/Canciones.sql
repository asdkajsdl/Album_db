CREATE TABLE Canciones (
    id_cancion INT PRIMARY KEY AUTO_INCREMENT,
    id_album INT,
    titulo VARCHAR(255) NOT NULL,
    duracion TIME,
    numero_pista INT,
    fecha_lanzamiento DATE,
    FOREIGN KEY (id_album) REFERENCES Albumes(id_album)
);



