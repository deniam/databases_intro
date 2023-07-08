DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    release_year INTEGER
);

INSERT INTO movies (title, genre, release_year) VALUES ('Batman', 'Fantasy', 1980);
INSERT INTO movies (title, genre, release_year) VALUES ('Terminator', 'Action', 1984);
INSERT INTO movies (title, genre, release_year) VALUES ('The Simpsons', 'Cartoon', 1975);