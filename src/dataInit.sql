PRAGMA foreign_keys = on;

DELETE FROM bands;
DELETE FROM modules;

INSERT INTO modules
VALUES
(0, 'Bandsintown'),
(1, 'Songkick');

INSERT INTO bands (name, module_id, module_arg)
VALUES
('Madness', 1, '1959190-madness'),
('Sleaford Mods', 1, '635776-sleaford-mods'),
('Shame', 1, '134405-shame'),
('IDLES', 1,'1352869-idles'),
('SLAVES', 1, '22255-slaves'),
('Konflikt', 0, 'Konflikt,official'),
('Rammstein', 0, 'Rammstein'),
('Sum 41', 0, 'sum 41'),
('Dropkick Murphys', 0, 'dropkick murphys'),
('Polemic', 0, 'polemic'),
('Bad Manners', 0, 'bad manners'),
('Medial Banana', 0, 'medial banana'),
('Horkýže Slíže', 0, 'Horkýže Slíže');
