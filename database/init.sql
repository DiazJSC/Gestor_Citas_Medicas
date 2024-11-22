CREATE DATABASE IF NOT EXISTS pacientes;

USE pacientes;

CREATE TABLE IF NOT EXISTS excel_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(255),
    column2 VARCHAR(255),
    column3 VARCHAR(255)
);

INSERT INTO excel_data (column1, column2, column3)
VALUES ('Sample1', 'Sample2', 'Sample3');
