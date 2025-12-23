-- Crea la base de datos
CREATE DATABASE IF NOT EXISTS left4dead_db;

-- Usa la base de datos
USE left4dead_db;

-- Crea la tabla de registros
CREATE TABLE IF NOT EXISTS registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    fecha_registro DATETIME NOT NULL
);

-- Muestra todos los registros
SELECT * FROM registros;