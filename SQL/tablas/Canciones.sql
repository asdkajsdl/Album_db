CREATE TABLE Canciones (
    id_cancion INT PRIMARY KEY AUTO_INCREMENT,
    id_album INT,
    titulo VARCHAR(255) NOT NULL,
    duracion TIME,
    numero_pista INT,
    fecha_lanzamiento DATE,
    FOREIGN KEY (id_album) REFERENCES Albumes(id_album)
);


<<<<<<< HEAD
INSERT INTO Canciones (Titulo, Duracion,Año_lanzamiento)
VALUES ('Tuntakmon', ),
('Omatopopih', ''),
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
=======
INSERT INTO Canciones (Album_id,Titulo, Duracion)
VALUES ('Tuntakmon',2:32),
('Omatopopih',1:00),
('Hijo prodigo',2:46),
('Vamo a bailar a tribunales',),
('Mas sencillo',4:25),
('Dejando de fumar',0:59),
('La mochila del mundo',3:06),
('Sigo intentando',3:19),
('Astronautas',2:48),
('Anita',),
('Casi 30',0:50),
('No tengo hambre tengo ansiedad',2:14),
('Cultura porno disney',2:34),
('El moutros del sofa',2:38),
('Dopamina',3:21),
('Algo nuevo',3:07),
('La era del Rivotril',3:41),
('Un dia a la vez + 135',3:13),
('Las vacas',),
('Vertigo',),
('Entre los dedos se va',),
('No es cualquier bebida',1:00),
('Bonsai',3:08),
('Nicolas cage',3:30),
('El mundo siempre estuvo',),
('Algo tiene que cambiar',3:32),
('El Heroe de constitucion',3:29),
('Paris es buen lugar para morir',1:00),
('Fin del mundo',),
('Principio a fin',),
('Cancion de julia',3:19),
('El juglar',);
>>>>>>> 5be0dbd14dbc5fb821ec03323325ac64247829b4

