from fabric.api import *


def init_service():

     # Iniciamos el servicio web
    
     run('cd proyecto-iv-1819/ && sudo gunicorn webApp:app -b 0.0.0.0:80')
      
      
def update_service():
    
    # Descargamos desde el repositorio
    run('git pull origin master')

    # Instalamos las dependencias mediante el fichero requirements.txt por si acaso hayan cambiado
    run('pip3 install -r proyecto-iv-1819/requirements.txt')
     
def stop_service():
     
    # Paramos el servicio web

    run('service gunicorn stop')

def remove_service():
    
    # Eliminamos por completo el servicio
    
    run('rm -rf proyecto-iv-1819')
