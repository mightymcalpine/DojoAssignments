SELECT *
FROM users;

SELECT *
FROM messages;

SELECT *
FROM comments;

SELECT messages.id, messages.message, messages.created_at, CONCAT(users.first_name, ' ', users.last_name) AS name
FROM messages 
LEFT JOIN users ON messages.user_id = users.id
ORDER BY messages.id DESC;

DELETE FROM messages
WHERE id > 0;

SELECT comments.id, comments.comment, comments.created_at, CONCAT(users.first_name, ' ', users.last_name) AS name
FROM comments
LEFT JOIN messages ON comments.message_id = messages.id
LEFT JOIN users ON messages.user_id = users.id
ORDER BY comments.id DESC;