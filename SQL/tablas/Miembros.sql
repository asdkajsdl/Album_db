CREATE TABLE Miembros (
    id_miembro INT PRIMARY KEY AUTO_INCREMENT,
    id_artista INT,
    id_rol INT,
    nombre VARCHAR(255) NOT NULL,
    rol VARCHAR(100),
    FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista),
    FOREIGN KEY (id_rol) REFERENCES Roles(id_rol)
);

-- Actualizar la biografía de un miembro
UPDATE Miembros
SET 
    biografia = 'Nueva biografía del miembro'
WHERE 
    id_miembro = 1; -- Reemplaza el 1 por el id del miembro que deseas actualizar


-- Actualizar el rol de un miembro
UPDATE Miembros
SET 
    id_rol = 2 
WHERE 
    id_miembro = 1; 

-----
DELETE FROM Miembros
WHERE id_miembro = 1;


INSERT INTO Miembros (id_artista, nombre)
VALUES 
(1, 'Alan Sutton'),
(1, 'Tomas Caso'),
(1, 'Ignacio Bennatti'),
(1, 'Lautaro Rodriguez Alvares'),
(1, 'Jeronimo Romero'),
(1, 'Agustin Ruiz Panelo');

