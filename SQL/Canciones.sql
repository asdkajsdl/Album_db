CREATE TABLE Canciones (
    song_id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único de la canción (Clave primaria)
    album_id INT,                            -- Identificador del álbum (Clave foránea)
    title VARCHAR(100) NOT NULL,              -- Título de la canción
    duration TIME,                           -- Duración de la canción (HH:MM:SS)
    track_number INT,                        -- Número de pista en el álbum
    release_date DATETIME,                   -- Fecha de lanzamiento de la canción
    FOREIGN KEY (album_id) REFERENCES Álbumes(album_id)  -- Relación con la tabla Álbumes
);


INSERT INTO Canciones (album_id, title, duration, track_number, release_date)
VALUES 
(1, 'El Último Sueño', '04:05', 1, '2022-05-15 00:00:00'),
(1, 'El Viento y el Fuego', '03:45', 2, '2022-05-15 00:00:00'),
(2, 'La Noche del Desvelo', '05:10', 1, '2023-06-20 00:00:00'),
(2, 'Despertar de las Sombras', '04:30', 2, '2023-06-20 00:00:00');
 