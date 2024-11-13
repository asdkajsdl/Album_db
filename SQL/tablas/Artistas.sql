CREATE TABLE Artistas (
    id_artista INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    genero VARCHAR(50),
    pais VARCHAR(50),
);  

INSERT INTO Artistas (nombre, genero, pais, biografia)
VALUES ('Alan Sutton Y Las Criaturitas De La Ansiedad', 'Rock Alternativo', 'Argentina', 'Banda argentina de rock alternativo con letras introspectivas y poéticas.');
