# Usar la imagen oficial de MySQL
FROM mysql:8.0

# Configurar variables de entorno para MySQL
ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=pacientes

# Copiar el archivo init.sql al contenedor
COPY init.sql /docker-entrypoint-initdb.d/

# Exponer el puerto de MySQL
EXPOSE 3306