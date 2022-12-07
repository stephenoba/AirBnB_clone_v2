-- Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_dev on performance_schema.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED WITH mysql_native_password BY "hbnb_test_pwd";
GRANT ALL PRIVILEGES
   ON hbnb_dev_db.*
   TO 'hbnb_test'@'localhost';
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
