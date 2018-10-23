from main import ClothesHandler

clothesManager = ClothesHandler()

class Tests(object):

  # Comprueba la función login
  def test_login(self)
    assert clothesManager.login("user","password") == "Usuario OK."
    assert clothesManager.login(123,123456) == "El usuario no existe."
    assert clothesManager.login("testUser","testPass") != "El usuario no existe."
    
  # Comprueba la función availablePiece
  def test_availablePiece(self)
    assert clothesManager.availablePiece(001) == "ID válida."
    assert clothesManager.availablePiece("a0012l") == "ID de pieza inválida."
    assert clothesManager.availablePiece(005) != "ID de pieza inválida."
