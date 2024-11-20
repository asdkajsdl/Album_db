CREATE TABLE Roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL
);

--Renombrar una columna
ALTER TABLE Pais
CHANGE nombre_pais nombre VARCHAR(100) NOT NULL;


INSERT INTO Roles (nombre_rol) 
VALUES 
('Voz y guitarra'),
('Bajo'),
('Batería'),
('Teclado'),
('Guitarra'),
('Percucion');