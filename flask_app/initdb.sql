use lista_negra;
CREATE TABLE telefonos (
	id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	nombre varchar(60),
	telefono varchar(20) UNIQUE
	);
	