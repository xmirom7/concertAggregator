PRAGMA foreign_keys = on;

DELETE FROM bands;
DELETE FROM modules;

INSERT INTO modules
VALUES
(0, 'Bandsintown'),
(1, 'Songkick');

INSERT INTO bands (name, module_id, module_arg)
VALUES
('Konflikt', 0, 'Konflikt,official'),
('Rammstein', 0, 'Rammstein'),
('IDLES', 1,'1352869-idles'),
('SLAVES', 1, '22255-slaves'),
('Sum 41', 0, 'sum 41'),
('Dropkick Murphys', 0, 'dropkick murphys'),
('Polemic', 0, 'polemic'),
('Bad Manners', 0, 'bad manners'),
('Medial Banana', 0, 'medial banana'),
('Horkýže Slíže', 0, 'Horkýže Slíže');
