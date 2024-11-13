CREATE TABLE Canciones (
    id_cancion INT PRIMARY KEY AUTO_INCREMENT,
    id_album INT,
    titulo VARCHAR(255) NOT NULL,
    duracion TIME,      -- Duración de la canción (HH:MM:SS)
    numero_pista INT,
    fecha_lanzamiento DATE,
    FOREIGN KEY (id_album) REFERENCES Albums(id_album)
);

INSERT INTO Canciones (Album_id, titulo, duracion, numero_pista, fecha_lanzamiento)
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
(1, 'Mi lugar', '00:02:35', 10, '2018-04-24');

<<<<<<< HEAD
(2, 'Por casualidad', '00:03:27', 1)
(2, 'La era del Rivotril','00:03:41',2)
(2, 'El heroe de constitucion', '00:03:29',3)


INSERT INTO Canciones (Album_id,Titulo, duracion)
VALUES ('Tuntakmon','00:02:32'),
('Omatopopih','00:1:00'),
('Hijo prodigo','00:2:46'),
('Mas sencillo','4:25'),
('Dejando de fumar','00:00:59'),
('La mochila del mundo','00:3:06'),
('Sigo intentando','00:03:19'),
('Astronautas','00:02:48'),
('Casi 30','00:00:50'),
('No tengo hambre tengo ansiedad','00:02:14'0),
('Cultura porno disney','00:02:34'),
('El moutñros del sofa','00:02:38'), 
('Dopamina','00:03:21'),
('Algo nuevo','00:03:07'),
('Un dia a la vez + 135','00:01:13'),
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
>>>>>>> 59c87dacd7e095874104cec2aa6f91aa13340677
('Las vacas',),
('Entre los dedos se va',),
('No es cualquier bebida','00:01:00'),
('Bonsai','00:03:08'),
('Nicolas cage','00:03:30'),
('El mundo siempre estuvo',),
('Algo tiene que cambiar','00:03:32'),
('El Heroe de constitucion','00:03:29'),
('Paris es buen lugar para morir','00:01:00'),
('Fin del mundo',),
('Principio a fin',),
<<<<<<< HEAD
('Cancion de julia','00:03:19');
=======
('Cancion de julia',3:19),
('El juglar',);

>>>>>>> 59c87dacd7e095874104cec2aa6f91aa13340677
