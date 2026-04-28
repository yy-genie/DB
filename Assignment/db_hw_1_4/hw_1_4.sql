-- database: ./tracks.sqlite3

SELECT * FROM tracks WHERE name LIKE '%love%';
SELECT * FROM tracks WHERE GenreId = 1 and Milliseconds >= 300000 ORDER BY UnitPrice DESC;
SELECT GenreId, COUNT(*) AS TotalTracks FROM tracks GROUP BY GenreId;
SELECT GenreId, SUM(UnitPrice) AS TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice >= 100;