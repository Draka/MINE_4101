# Instalación

 * Instalar Docker
 * Ir a la carpeta del proyecto y ejecutar

 ```
 docker build -t jupyter/python37 .
 ```
 * iniciar la imágen por primera vez con este comando
 ```
 docker run -p 8888:8888 -v "RUTA LOCAL PROYECTO":/home/jovyan/work -it -e GRANT_SUDO=yes --user root jupyter/python37
 ```
 * Ir a la consola de la imagen del docker e instalar gdal

 ```
 conga install gdal
 ```