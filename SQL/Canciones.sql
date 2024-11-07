CREATE TABLE Canciones (
    song_id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único de la canción (Clave primaria)
    Album_id INT,                            -- Identificador del álbum (Clave foránea)
    Titulo VARCHAR(100) NOT NULL,              -- Título de la canción
    duration TIME,                           -- Duración de la canción (HH:MM:SS)
    FOREIGN KEY (album_id) REFERENCES Álbumes(album_id)  -- Relación con la tabla Álbumes
);


INSERT INTO Canciones (Album_id,Titulo, Duracion,Año_lanzamiento)
VALUES ('Tuntakmon'),
('Omatopopih'),
('Hijo prodigo'),
('Vamo a bailar a tribunales'),
('Mas sencillo'),
('Dejando de fumar'),
('La mochila del mundo'),
('Sigo intentando'),
('Astronautas'),
('Anita'),
('Casi 30'),
('No tengo hambre tengo ansiedad'),
('Cultura porno disney'),
('El moutros del sofa'),
('Dopamina'),
('Algo nuevo'),
('La era del Rivotril'),
('Un dia a la vez + 135'),
('Las vacas'),
('Vertigo'),
('Entre los dedos se va'),
('No es cualquier bebida'),
('Bonsai'),
('Nicolas cage'),
('El mundo siempre estuvo'),
('Algo tiene que cambiar'),
('El Heroe de constitucion'),
('Paris es buen lugar para'),
('Fin del mundo'),
('Principio a fin'),
('Cancion de julia'),
('El juglar');
