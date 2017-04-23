SELECT *
FROM users;

INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES('Lars', 'Codus', now(), now()),
('Wally', 'MacDuggen', now(), now()),
('Deitrick', 'Fahrvergnugen', now(), now()),
('Stoney', 'McFranklin', now(), now()),
('Johnny', 'Framebox', now(), now());

INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (6, 4, now(), now()),
(6, 2, now(), now()),
(6, 3, now(), now()),
(8, 4, now(), now()),
(8, 2, now(), now()),
(10, 1, now(), now()),
(10, 2, now(), now());

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON user2.id = friendships.friend_id