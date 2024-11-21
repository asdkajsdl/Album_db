CREATE TABLE Albums (
    id_album INT PRIMARY KEY,
    id_artista INT,
    titulo VARCHAR(255) NOT NULL,
    Año_lanzamiento INT,
    genero VARCHAR(100),
    FOREIGN KEY (id_artista) REFERENCES Artistas(id_artista)
);

--Eliminar una columna
ALTER TABLE Albums
DROP COLUMN genero;

--Agrgar una columna
ALTER TABLE Albums
ADD nombre_productor VARCHAR(255);

--Modificar una columna (cambiar tipo o restricción)
ALTER TABLE Albums
MODIFY Año_lanzamiento YEAR;


INSERT INTO Albums (id_album, id_artista, titulo, Año_lanzamiento, genero)
VALUES
(1, 1, 'Alan Sutton y las Criaturitas de la Anciedad', 2018, 'Rock Alternativo'),
(2, 1, 'Hombrecito con los pies en la Tierra', 2020, 'Rock Alternativo'),
(3, 1, 'Algo tiene que cambiar', 2023, 'Rock Alternativo'),
(4, 1, 'Tomate 5', 2021, 'Rock Alternativo'),
(5, 2, 'Homerun', 2019, 'Musica Urbana'),
(6, 3, 'Donde quiero estar', 2023,'Reggaeton'),
(7, 4, 'Un verano sin ti', 2022, 'Musica urbana'),
(8, 5, 'Easy money baby', 2020,'Reggaeton'),
(9, 6, 'Partyson', 2023,'Reggaeton'),
(10, 7, 'FERXXOCALIPSIS', 2023, 'Reggaeton'),
(11, 8, 'Exodo', 2024,'Corrido tumbado'),
(12, 9, 'Radical Optimism', 2024,'Pop'),
(13, 10, 'Unorthodox judebox', 2012,'Pop'),
(14, 11, 'Formula', 2014,'Bachata');

  