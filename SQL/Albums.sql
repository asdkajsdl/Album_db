CREATE TABLE Álbumes (
    album_id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único del álbum (Clave primaria)
    artist_id INT,                           -- Identificador del artista/banda (Clave foránea)
    title VARCHAR(100) NOT NULL,              -- Título del álbum
    release_year INT,                        -- Año de lanzamiento
    genre VARCHAR(50),                       -- Género del álbum (opcional, puede ser diferente del artista)
    cover_image VARCHAR(255),                -- Ruta o URL de la imagen de portada del álbum (opcional)
    FOREIGN KEY (artist_id) REFERENCES Artistas(artist_id)  -- Relación con la tabla Artistas
);

INSERT INTO Álbumes (artist_id, title, release_year, genre, cover_image)
VALUES (1, 'Criaturitas del Tiempo', 2022, 'Indie experimental', '/images/criaturitas_del_tiempo.jpg');
