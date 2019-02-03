from fabric.api import *


def init_service():

     # Iniciamos el servicio web
    
     run('cd proyecto-iv-1819/ && sudo gunicorn webApp:app -b 0.0.0.0:80')
      
      
def update_service():

    # Eliminamos la instalación actual para prevenir posible problemas
    run('rm -rf proyecto-iv-1819')

    # Descargamos desde el repositorio
    run('git clone https://github.com/AitorSDL/proyecto-iv-1819.git')

    # Instalamos las dependencias mediante el fichero requirements.txt
    run('pip3 install -r proyecto-iv-1819/requirements.txt')


