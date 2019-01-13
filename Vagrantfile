# Fichero utilizado para el funcionamiento de la máquina virtual y la conexión con azure.

Vagrant.configure('2') do |configuracion| # Variable de configuración para la máquina virtual. Establecemos que la versión de la máquina sea del rango 1.1+ - 2.0.x
  configuracion.vm.box = 'azure' # El nombre de nuestra máquina vitual

  # Claves ssh para conectarse a la máquina.
  configuracion.ssh.private_key_path = '~/.ssh/id_rsa' # Cogemos la clave ssh almacenada en esta ruta de nuestro sistema para conectarnos a la máquina
                                                       # sin necesidad de contraseña.
  

