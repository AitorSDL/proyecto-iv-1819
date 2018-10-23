
class ClothesHandler:
  
  def login(self,user,passwd)
    if type(user) != str or type(passwd) != str:
        return "El usuario no existe."
    else:
        return "Usuario OK."
      
  def availablePiece(self,id)
    if type(id) != int:
        return "ID de pieza inválida."
    else:
        print("Buscando pieza...")
