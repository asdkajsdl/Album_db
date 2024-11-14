CREATE TABLE Canciones (
    id_cancion INT PRIMARY KEY AUTO_INCREMENT,
    id_album INT,
    titulo VARCHAR(255) NOT NULL,
    duracion TIME,
    numero_pista INT,
    fecha_lanzamiento DATE,
    FOREIGN KEY (id_album) REFERENCES Albums(id_album)
);


----
SELECT * FROM Canciones;


----
SELECT * FROM Canciones
WHERE titulo = 'La canción de ejemplo';

----
SELECT * FROM Canciones
WHERE id_album = 1;

----Actualizar Información de una Canción
UPDATE Canciones
SET titulo = 'Nuevo título de la canción'
WHERE id_cancion = 1;

---DELETE FROM Canciones
WHERE id_cancion = 1;




INSERT INTO Canciones (id_album, titulo, duracion, numero_pista, fecha_lanzamiento)
VALUES
(1, 'Principio a fin', '00:04:46', 1, '2018-04-24'),
(1, 'Vamo a bailar a tribunales', '00:03:12', 2, '2018-04-24'),
(1, 'Anita', '00:03:09', 3, '2018-04-24'),
(1, 'El juglar', '00:04:08', 4, '2018-04-24'),
(1, 'Vertigo', '00:03:05', 5, '2018-04-24'),
(1, 'Que karma', '00:04:02', 6, '2018-04-24'),
(1, 'Titero', '00:03:56', 7, '2018-04-24'),
(1, 'Con cinta scotch', '00:03:48', 8, '2018-04-24'),
(1, 'Entre los dedos se va', '00:02:46', 9, '2018-04-24'),
(1, 'Mi lugar', '00:02:35', 10, '2018-04-24'),
(2, 'Por Casualidad', '00:03:27', 1, '2020-09-04'),
(2, 'La Era del Rivotril', '00:03:41', 2, '2020-09-04'),
(2, 'El Héroe de Constitución', '00:03:29', 3, '2020-09-04'),
(2, 'La Manera', '00:03:51', 4, '2020-09-04'),
(2, 'Las Vacas, Pereyra y la Elite', '00:03:39', 5, '2020-09-04'),
(2, 'Sr. Cabeza de Reloj', '00:04:35', 6, '2020-09-04'),
(2, 'Cacique', '00:03:53', 7, '2020-09-04'),
(2, 'Peter Pan', '00:03:27', 8, '2020-09-04'),
(2, 'Astronautas', '00:02:48', 9, '2020-09-04'),
(2, 'Un Limón', '00:02:32', 10, '2020-09-04'),
(2, 'Mono de Ciudad', '00:03:26', 11, '2020-09-04'),
(2, 'Criaturita de la Ansiedad', '00:03:40', 12, '2020-09-04'),
(3, 'Algo Tiene Que Cambiar', '00:03:32', 1, '2023-05-19'),
(3, 'Tutank´mon', '00:02:32', 2, '2023-05-19'),
(3, 'El Monstruo del Sofá', '00:02:38', 3, '2023-05-19'),
(3, 'Bonsai', '00:03:08', 4, '2023-05-19'),
(3, 'Más Sencillo', '00:04:25', 5, '2023-05-19'),
(3, 'El Mundo Siempre Estuvo Dividido en Dos', '00:02:05', 6, '2023-05-19'),
(3, 'Casi 30', '00:00:50', 7, '2023-05-19'),
(3, 'Cultura Porno Disney', '00:02:34', 8, '2023-05-19'),
(3, 'No Tengo Hambre, Tengo Ansiedad', '00:02:14', 9, '2023-05-19'),
(3, 'La Mochila del Mundo', '00:03:06', 10, '2023-05-19'),
(3, 'Sigo Intentando', '00:03:19', 11, '2023-05-19'),
(3, 'Canción de Julia', '00:03:19', 12, '2023-05-19'),
(3, 'Un Día a la Vez + 135', '00:03:13', 13, '2023-05-19'),
(3, 'Algo Nuevo', '00:03:07', 14, '2023-05-19'),
(4, 'Omatopopih', '00:01:00', 1, '2021-12-17'),
(4, 'Canción Tortuga', '00:01:00', 2, '2021-12-17'),
(4, 'Dejando de Fumar', '00:00:59', 3, '2021-12-17'),
(4, 'No Es Cualquier Bebida Cola', '00:01:00', 4, '2021-12-17'),
(4, 'París Es Buen Lugar para Morir', '00:01:00', 5, '2021-12-17');
