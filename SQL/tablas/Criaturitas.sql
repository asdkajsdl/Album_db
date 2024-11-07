CREATE TABLE Miembros (
    id_miembro INT PRIMARY KEY AUTO_INCREMENT,
    id_artista INT,
    nombre VARCHAR(255) NOT NULL,
    rol VARCHAR(100),
    FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista)
);

INSERT INTO Miembros (id_artista, nombre, rol,) 
VALUES 
(1, 'Alan Sutton', 'Voz y guitarra')
(1, 'Tomas Caso', 'Bajo'),
(1, 'Ignacio Bennatti', 'Batería'),
(1, 'Lautaro Rodriguez Alvares', 'Teclado'),
(1, 'Jeronimo Romero', 'Guitarra'),
(1, 'Agustin Ruiz Panelo', 'Percucion');

