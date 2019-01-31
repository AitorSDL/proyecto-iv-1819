# Fichero utilizado para el funcionamiento de la máquina virtual y la conexión con azure.

Vagrant.configure('2') do |configuracion| # Variable de configuración para la máquina virtual. Establecemos que la versión de la máquina sea del rango 1.1+ - 2.0.x
  configuracion.vm.box = 'azurevm' # El nombre de nuestra máquina vitual

  # Claves ssh para conectarse a la máquina.
  configuracion.ssh.private_key_path = '~/.ssh/id_rsa' # Cogemos la clave ssh almacenada en esta ruta de nuestro sistema para conectarnos a la máquina
                                                       # sin necesidad de contraseña.
  
  config.vm.provider :azure do |azure, override|
    
  azure.tenant_id = ENV['AZURE_TENANT_ID']
  azure.client_id = ENV['AZURE_CLIENT_ID']
  azure.client_secret = ENV['AZURE_CLIENT_SECRET']
  azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
    
  azure.vm_name = "azurevm-proyecto"
  azure.vm_size = "Standard_D2_v2"
  azure.tcp_endpoints = "80"
  azure.location = "westeurope"
  azure.admin_username = "aitorsdl"
  

