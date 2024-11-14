CREATE TABLE Artistas (
    id_artista INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    genero VARCHAR(50),
    id_pais INT,
    biografia TEXT,
    FOREIGN KEY (id_pais) REFERENCES Paises(id_pais)
);


-----Script BM
SELECT * FROM Artistas;

-----Script para actualizar
UPDATE Artistas
SET genero = 'Rock Alternativo'
WHERE id_artista = 1;

----eliminar
DELETE FROM Artistas
WHERE id_artista = 1;



INSERT INTO Artistas (nombre, genero, biografia)
VALUES ('Alan Sutton Y Las Criaturitas De La Ansiedad', 'Rock Alternativo', 'Banda argentina de rock alternativo con letras introspectivas y poéticas.');
