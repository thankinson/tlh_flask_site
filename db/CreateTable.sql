CREATE TABLE IF NOT EXISTS user_admin (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	roles_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS users (
	id INTEGER NOT NULL, 
	user_name VARCHAR(30) NOT NULL, 
	first_name VARCHAR(30) NOT NULL, 
	last_name VARCHAR(30) NOT NULL, 
	user_email VARCHAR(30) NOT NULL, 
	password VARCHAR(200) NOT NULL, 
	remember_user BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (user_name), 
	UNIQUE (user_email)
);

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','admin', 'admin@admin.com', '$2b$12$JbYx.GgrXWxZ0wIZxXbP/eyP7pG7A3cru.osarVqhv3KRUVkSqZxG');
INSERT INTO `user_admin` VALUES (1,(users.id) 1);

/*!40000 ALTER TABLE `users` ENABLE KEYS */;