class Palindromo:
  def palindromo_texto(string):
    texto = "".join(string.split())
    texto =texto.lower()
    string=string.replace("", "")
    texto=""
    for n in string:
       texto= n + texto
    if (string == texto):
      print("La frase es Palindromo")
    else:
      print("La frase no es Palindromo")
class  contar:
  def contar_vocales(texto):
    return sum(c in {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"} for c in texto)