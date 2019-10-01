DROP TABLE IF EXISTS modules;
DROP TABLE IF EXISTS bands;
DROP TABLE IF EXISTS events;

CREATE TABLE modules (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE
);

CREATE TABLE bands (
id integer PRIMARY KEY,
name text NOT NULL UNIQUE,
module_id integer NOT NULL,
module_arg text,
         FOREIGN KEY (module_id) REFERENCES modules(id)
);

CREATE TABLE events (
id integer PRIMARY KEY,
band text not null,
country text not null,
city text not null,
clubName text,
date text not null,
url text,
additionalInfo text,
UNIQUE(band, country, city, clubName, date, url, additionalInfo)
);
