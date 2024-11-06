CREATE TABLE Artistas (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,  -- Identificador único del artista (Clave primaria)
    name VARCHAR(100) NOT NULL,                -- Nombre del artista o banda
    genre VARCHAR(50),                         -- Género musical del artista
    country VARCHAR(100),                      -- País de origen del artista
    bio TEXT                                    -- Biografía del artista (opcional)
);


INSERT INTO Artistas (name, genre, country, bio)
VALUES ('Alansutton y las Criaturitas de la Anciedad', 'Indie/Experimental', 'Argentina', 'Proyecto musical de Alansutton con una banda experimental. Música introspectiva y filosófica.');
