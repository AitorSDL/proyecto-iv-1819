
class ClothesHandler:
  
  def login(self,user,passwd):
    if type(user) != str or type(passwd) != str:
      return "El usuario no existe."
    else:
      return "Usuario OK."
      
  def availablePiece(self,pieceId):
    if type(pieceId) != int:
      return "ID de pieza inválida."
    else:
      print("Buscando pieza...")
      return "ID válida."
      
  def searchPiece(self, itemName):
    if not isinstance(itemName, str):
      return "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
    else:
      print("Buscando artículo...")
      return "articulo"
