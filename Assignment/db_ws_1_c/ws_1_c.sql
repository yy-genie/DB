-- database: ./songs.sqlite3

SELECT * FROM songs;
SELECT genre, COUNT(*), AVG(duration) FROM songs GROUP BY genre;
SELECT genre, COUNT(*) FROM songs GROUP BY genre;