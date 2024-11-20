CREATE TABLE Pais (
    id_pais INT PRIMARY KEY AUTO_INCREMENT,
    nombre_pais VARCHAR(100) NOT NULL
);

--Agregar una nueva tabla
ALTER TABLE Pais
ADD codigo_iso VARCHAR(3) NOT NULL;




INSERT INTO Pais (nombre_pais)
VALUES 
('Argentina');
