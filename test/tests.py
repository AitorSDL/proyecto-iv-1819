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
    assert clothesManager.searchPiece(111) == "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
    assert clothesManager.searchPiece("test") == "articulo"
    assert clothesManager.searchPiece("Test001") == "articulo"
    assert clothesManager.searchPiece(True) == "Debe escribir un nombre de artículo. Ejemplo: camiseta, pantalón, etc."
    
  # Comprueba que las funciones devuelvan el tipo correcto
  def test_correctType(self):
    assert isinstance(clothesManager.availablePiece(0012),str)
    assert isinstance(clothesManager.searchPiece(0012),str)
    assert isinstance(clothesManager.availablePiece("0012"),str)
    assert isinstance(clothesManager.searchPiece("0012"),str)
