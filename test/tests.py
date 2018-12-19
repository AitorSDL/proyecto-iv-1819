from src.main import ClothesHandler

clothesManager = ClothesHandler()

class Tests(object):

  # Comprueba la función login
  def test_login(self):
    assert clothesManager.login("user","password") == "Usuario OK."
    assert clothesManager.login(123,123456) == "El usuario no existe."
    assert clothesManager.login("testUser","testPass") != "El usuario no existe."
    
  # Comprueba la función availablePiece
  def test_availablePiece(self):
    assert clothesManager.availablePiece(1298347) == "ID válida."
    assert clothesManager.availablePiece("a0012l") == "ID de pieza inválida."
    assert clothesManager.availablePiece(111) != "ID de pieza inválida."

  # Comprueba la función searchItem
  def test_searchItem(self):
    assert clothesManager.searchItem(001) == "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
    assert clothesManager.searchItem("test") == "articulo"
    assert clothesManager.searchItem("Test001") == "articulo"
    assert clothesManager.searchItem(True) == "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
