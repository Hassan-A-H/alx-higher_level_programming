-- SQL script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

SELECT s.title, g.name
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS sg
       ON g.id = sg.genre_id
       RIGHT JOIN tv_shows AS s
       ON s.id = sg.show_id
ORDER BY s.title, g.name;
