CREATE TABLE Criaturitas (
    member_id INT AUTO_INCREMENT PRIMARY KEY,   -- Identificador único del miembro (Clave primaria)
    artist_id INT,                              -- Identificador del artista/banda (Clave foránea)
    name VARCHAR(100) NOT NULL,                  -- Nombre del miembro
    role VARCHAR(100),                          -- Rol o instrumento que toca el miembro (guitarra, batería, etc.)
    bio TEXT,                                   -- Biografía del miembro (opcional)
    FOREIGN KEY (artist_id) REFERENCES Artistas(artist_id)  -- Relación con la tabla Artistas
);


INSERT INTO Criaturitas (artist_id, name, role, bio)
VALUES 
(1, 'Alansutton', 'Vocalista y Guitarrista', 'Alansutton es el líder y vocalista principal de la banda. Su estilo único combina lo experimental con lo introspectivo.'),
(1, 'Felipe Luna', 'Bajista', 'Felipe Luna es el bajista de la banda, conocido por su estilo único de tocar que aporta una base sólida y melódica.'),
(1, 'Carlos López', 'Baterista', 'Carlos López es el baterista de la banda, su estilo experimental le da un toque especial a las composiciones de la banda.');
