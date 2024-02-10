# !wget https://raw.githubusercontent.com/JuanUNAL/code/main/juanma.py
# import juanma
# juanma.clean()
# juanma.info()

def clean():
  print("\b" * 1000, end=())

def info():
  funcionesNombres = [
      " info | clean()                                                              |",
      " info | info()                                                               |",      
      " info | table(data, stiles)                                                  |",
      " info | tableInfo()                                                          |",      
      " info | centrar(a, t, i, f)                                                  |",
      " info | centrarInfo()                                                        |",
      " info | square(t, c, bg)                                                     |",
      " info | squareInfo()                                                         |",
      " info | triangle(t, c)                                                       |",
      " info | triangleInfo()                                                       |"
  ]
  print(" info | Para importar copia en tu codigo lo siguiente:                       |")
  print(" info | !wget https://raw.githubusercontent.com/JuanUNAL/code/main/juanma.py |")
  print(" info | import juanma                                                        |")
  print(" info | juanma.clean()                                                       |")
  print(" info |                                                                      |")
  print(" info | Funciones:                                                           |")
  for i in funcionesNombres:
    print(i)

def table(data, stiles):
  print(f"\033[{stiles}m")
  columnas = 0
  for i in data:
    if len(i) > columnas:
      columnas = len(i)
  anchos = [0] * columnas

  for i in data:    
    for j in i:
      if len(str(j)) > anchos[i.index(j)]:
        anchos[i.index(j)] = len(str(j))
  
  for i in anchos:
    espacios = "─" * i
    print(f"● {espacios}",end=(" "))
  print("●")
  for i in data:
    if data.index(i) == 0:
      for j in i:
        espacios = " " * (anchos[i.index(j)] - len(str(j)))
        print(f"│ {j}{espacios}",end=(" "))
      print("│")
      for i in anchos:
        espacios = "─" * i
        print(f"● {espacios}",end=(" "))
      print("●")
    else: 
      for j in i:
        espacios = " " * (anchos[i.index(j)] - len(str(j)))
        print(f"│ {j}{espacios}",end=(" "))
      print("│")

  for i in anchos:
    espacios = "─" * i
    print(f"● {espacios}",end=(" "))
  print("●")
  print("\033[0m")

def tableInfo():
  print(" info | table(data, stiles)                                                                              |")
  print(" info | data  = [[t1, t2, ...,  tn], [e11, e12, ..., e1n], [e21, e22, ..., 2n], [en2, en2, ..., enn]]    |")
  print(" info | t = titulo                                                                                       |")
  print(" info | e = elemento                                                                                     |"),
  print(" info |                                                                                                  |"),
  print(" info | Ejemplo:                                                                                         |")
  print(' info | table([                                                                                          |')
  print(' info |  ["Nombre", "Número", "Fecha"],                                                                  |')
  print(' info |  ["Ana López", "123456789", "14/02/2024"],                                                       |')
  print(' info |  ["Pedro García", "987654321", "01/01/2023"],                                                    |')
  print(' info |  ["María Pérez", "234567890", "03/03/2022"],                                                     |')
  print(' info |  ["Juan Martín", "456789012", "05/05/2021"],                                                     |')
  print(' info | ])                                                                                               |')
  print(" info |                                                                                                  |"),
  print(' info | stiles = codigos de estilo separados por ; por ejemplo "36;3", codigos que puedes encontrar en   |')
  print(" info | https://python-para-impacientes.blogspot.com/2016/09/dar-color-las-salidas-en-la-consola.html    |")


def centrar(a, t, i, f): 
  ajuste = ""
  if (len(t) % 2 == 1):
      ajuste = " "
  aux = " " * int((a - len(t))/2)
  return i + aux + t + aux + ajuste + f

def centrarInfo():
  print(" info | centrar(a, t, i, f)      |")
  print(" info | a  = Ancho en caracteres |")
  print(" info | t  = Texto               |")
  print(" info | i = Inició               |")
  print(" info | f = Final                |")

def square(t, c, bg):
  for fil in range(t):
      if fil == 0 or fil == t - 1:
          for col in range(t - 1):
              print(f"{c} ", end=(""))
          print(f"{c}")
      else:
          for col in range(t):
              if col == 0:
                  print(f"{c} ", end=(""))
              else:
                if col == t - 1:
                  print(f"{c} ")
                else:
                  print(f"{bg} ", end=(""))

def squareInfo():
  print(" info | square(t, c, bg)         |")
  print(" info | t  = Tamaño              |")
  print(" info | c  = Caracter del borde  |")
  print(" info | bg = Caracter de relleno |")

def triangle(t, c):
  cont = t - 2
  cont2 = 1
  print(" " * (cont - 1), c)
  while cont!=0 and  cont2 != t:
    cont = cont - 1
    cont2 = cont2 + 2
    for space in range(cont):
      print(" ", end=(""))
    for space in range(cont2):
      print(c, end=(""))
    print("")

def triangleInfo():
  print(" info | triangle(t, c)           |")
  print(" info | t  = Tamaño              |")
  print(" info | c  = Caracter del borde  |")
  print(" info | bg = Caracter de relleno |")
