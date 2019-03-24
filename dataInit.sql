PRAGMA foreign_keys = on;

INSERT INTO modules
VALUES
(0, 'Bandsintown'),
(1, 'Songkick');

INSERT INTO bands (name, module_id, module_arg)
VALUES
('Konflikt', 0, 'Konflikt,official'),
('Rammstein', 0, 'Rammstein'),
('IDLES', 1,'1352869-idles');
