-- Creates/Setup hbnb_dev_db and user hbnb_dev
CREATE DATABASE IF NOT EXISTS hbhb_dev_db;
CREATE USER IF NOT EXISTS 'hbhb_dev'@'localhost' IDENTIFIED BY 'hbhb_dev_pwd';
GRANT ALL PRIVILEGES ON hbhb_dev_db.* TO 'hbhb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';