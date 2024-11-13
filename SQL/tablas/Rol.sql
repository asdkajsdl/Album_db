CREATE TABLE Roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL
);

INSERT INTO Miembros (rol) 
VALUES 
('Voz y guitarra'),
('Bajo'),
('Batería'),
('Teclado'),
('Guitarra'),
('Percucion');