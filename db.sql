CREATE USER IF NOT EXISTS 'pld_test'@'localhost' IDENTIFIED BY 'pld_test_pwd';
CREATE DATABASE IF NOT EXISTS pld_test_db;
GRANT ALL PRIVILEGES ON `pld_test_db`.* TO 'pld_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pld_test'@'localhost';