# Primero especificamos el lenguaje de programación que emplearemos y la versión

FROM python:3.6

# Ahora indicamos el directorio de trabajo para la aplicación

WORKDIR /webapp

# Después copiamos el contenido de este repositorio a lo que ahora es el directorio de trabajo

COPY . /webapp

# El siguiente paso es instalar las librerías necesarias de requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

# Antes de lanzar la aplicación establecemos un puerto por defecto

EXPOSE 5000

# Y por último, indicamos el comando para iniciar la aplicación y le nombre del fichero

ENTRYPOINT ["python3"]
CMD ["webApp.py"]
