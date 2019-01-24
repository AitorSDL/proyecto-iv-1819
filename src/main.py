from flask import json, jsonify

class ClothesHandler:
  
  def item(self, item_id, title, price, colour):
    self.item_id = item_id
    self.title = title
    self.price = price
    self.colour = colour
    
  def item_none(self):
    self.item_id = None
    self.title = None
    self.price = None
    self.colour = None
    
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
      
  def randomItem(self):
    with open('warehouse.json') as f:
      data = json.load(f)
      
    return data
      
  def searchPiece(self, itemName):
    if not isinstance(itemName, str):
      return "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
    else:
      print("Buscando artículo...")
      return "articulo"
