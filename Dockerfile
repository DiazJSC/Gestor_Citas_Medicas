# Usa una imagen base ligera de Python con versión 3.10
FROM python:3.10-slim

# Establece un directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos del proyecto al contenedor
COPY . .

# Expone el puerto en el que se ejecutará Flask (por defecto 5000)
EXPOSE 5000

# Comando para iniciar tu aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
