CREATE TABLE IF NOT EXISTS `users` (
	`id` INTEGER NOT NULL,
	`user_name` VARCHAR(30) NOT NULL,
	`first_name` VARCHAR(30) NOT NULL,
	`last_name` VARCHAR(30) NOT NULL,
	`user_email`	VARCHAR(30) NOT NULL,
	`password`	VARCHAR(200) NOT NULL,
	`remember_user`	BOOLEAN,
	PRIMARY KEY(`id`),
	UNIQUE(`user_email`),
	UNIQUE(`user_name`)
);
CREATE TABLE IF NOT EXISTS `user_admin` (
	`id` INTEGER NOT NULL,
	`user_id`	INTEGER,
	`roles_id` INTEGER,
	FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
	PRIMARY KEY(`id`)
);
INSERT INTO `users` (`id`,`user_name`,`first_name`,`last_name`,`user_email`,`password`,`remember_user`) VALUES (1,'admin','admin','admin','admin@email.com','$2b$12$WovjzWcD6y9XQtvocqiosOzwlp/xLrDLG7Nz.WaHpYoVJaLeGx8Om',0);
INSERT INTO `user_admin` (`id`,`user_id`,`roles_id`) VALUES (1,1,1);

GRANT ALL PRIVILEGES ON finalproject.* TO 'root'@'localhost'

