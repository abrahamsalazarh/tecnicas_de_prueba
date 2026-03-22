# ================================================================
#  PISTAS - EJERCICIOS TDL PYTHON
#
#  REGLA DE ORO:
#  Solo abre este archivo si llevas 15 minutos atascado.
#  Lee primero la PISTA 1 y vuelve a intentar.
#  Si sigues atascado después de otros 15 min → lee la PISTA 2.
#  Nunca leas las dos pistas al mismo tiempo.
# ================================================================


# ================================================================
#  TEMA 1: OPERADORES Y VARIABLES
# ================================================================

# --- PISTAS 1.1 ---
# Pista 1: Python permite asignar dos variables en una sola línea
# Pista 2: base, altura = 8, 5  |  area = base * altura  |  perimetro = 2 * (base + altura)

# --- PISTAS 1.2 ---
# Pista 1: existe un operador matemático que devuelve el residuo de una división
# Pista 2: el operador % da el residuo → 17 % 2 = 1

# --- PISTAS 1.3 ---
# Pista 1: IMC = peso dividido entre la altura elevada al cuadrado
# Pista 2: usa ** para elevar al cuadrado → altura ** 2  |  round(valor, 2) redondea a 2 decimales

# --- PISTAS 1.4 ---
# Pista 1: 1 hora = 3600 segundos | divide y guarda el residuo en cada paso
# Pista 2: horas = total // 3600
#          residuo = total % 3600
#          minutos = residuo // 60
#          segundos = residuo % 60

# --- PISTAS 1.5 ---
# Pista 1: Python puede asignar dos variables al mismo tiempo en una sola línea
# Pista 2: a, b = b, a  hace el intercambio en una sola línea sin variable auxiliar


# ================================================================
#  TEMA 2: CONDICIONALES
# ================================================================

# --- PISTAS 2.1 ---
# Pista 1: necesitas if, elif y else para cubrir los 3 casos
# Pista 2: if numero < 0 → negativo | elif numero == 0 → cero | else → positivo

# --- PISTAS 2.2 ---
# Pista 1: evalúa de mayor a menor para no necesitar and en las condiciones
# Pista 2: if nota >= 90 → Sobresaliente
#          elif nota >= 70 → Aprobado
#          elif nota >= 50 → Suficiente
#          else → Reprobado

# --- PISTAS 2.3 ---
# Pista 1: necesitas verificar 3 condiciones al mismo tiempo usando and
# Pista 2: acceso = (usuario == "admin") and (contrasena == "1234") and (intentos < MAX_INTENTOS)
#          if acceso: print("Acceso permitido") else: print("Acceso denegado")

# --- PISTAS 2.4 ---
# Pista 1: usa if/elif para cada operador: +, -, *, /
# Pista 2: if operacion == "+": resultado = num1 + num2
#          elif operacion == "/":
#              if num2 != 0: resultado = num1 / num2
#              else: print("Error: división entre cero")

# --- PISTAS 2.5 ---
# Pista 1: un triángulo es válido si la suma de cualquier par de lados
#          es mayor que el tercer lado
# Pista 2: if (a+b > c) and (a+c > b) and (b+c > a):  → triángulo válido
#              if a == b == c → Equilátero
#              elif a==b or b==c or a==c → Isósceles
#              else → Escaleno
#          else: → No forma un triángulo


# ================================================================
#  TEMA 3: FUNCIONES + TYPE HINTS
# ================================================================

# --- PISTAS 3.1 ---
# Pista 1: def nombre_funcion(parametro: tipo) -> tipo_retorno:
# Pista 2: def saludar(nombre: str) -> str:
#              return f"Hola, {nombre}! Bienvenido al taller."
#          print(saludar("Abraham"))

# --- PISTAS 3.2 ---
# Pista 1: C a F: (temp * 9/5) + 32  |  F a C: (temp - 32) * 5/9
# Pista 2: def celsius_a_fahrenheit(temp: float) -> float:
#              return (temp * 9/5) + 32
#          def fahrenheit_a_celsius(temp: float) -> float:
#              return (temp - 32) * 5/9

# --- PISTAS 3.3 ---
# Pista 1: precio_final = precio - (precio * porcentaje / 100)
# Pista 2: def calcular_descuento(precio: float, porcentaje: float) -> float:
#              if porcentaje < 0 or porcentaje > 100:
#                  return precio
#              return precio - (precio * porcentaje / 100)

# --- PISTAS 3.4 ---
# Pista 1: def funcion(p1, p2, p3="valor_por_defecto"):
# Pista 2: def generar_id(nombre: str, apellido: str, separador: str = ".") -> str:
#              return f"{nombre}{separador}{apellido}".lower()

# --- PISTAS 3.5 ---
# Pista 1: def funcion(parametro_obligatorio: str, **kwargs) -> None:
# Pista 2: def configurar_entorno(url_base: str, **opciones) -> None:
#              navegador = opciones.get("browser", "chrome")
#              reintentos = opciones.get("retries", 1)
#              timeout = opciones.get("timeout", 30)


# ================================================================
#  TEMA 4: BUCLES
# ================================================================

# --- PISTAS 4.1 ---
# Pista 1: range(inicio, fin) genera números desde inicio hasta fin-1
# Pista 2: numero = 7
#          for i in range(1, 11):
#              print(f"{numero} x {i} = {numero * i}")

# --- PISTAS 4.2 ---
# Pista 1: while condicion:  |  no olvides actualizar el contador dentro del while
# Pista 2: contador = 10
#          while contador > 0:
#              print(contador)
#              contador -= 1
#          print("¡Despegue!")

# --- PISTAS 4.3 ---
# Pista 1: el orden de los if importa → empieza siempre por el caso combinado (3 y 5)
# Pista 2: for n in range(1, 31):
#              if n % 3 == 0 and n % 5 == 0: print("FizzBuzz")
#              elif n % 3 == 0: print("Fizz")
#              elif n % 5 == 0: print("Buzz")
#              else: print(n)

# --- PISTAS 4.4 ---
# Pista 1: while True crea un bucle infinito | input() siempre devuelve string
#          necesitas convertir a int con int()
# Pista 2: secreto = 7
#          intentos = 0
#          while True:
#              numero = int(input("Adivina: "))
#              intentos += 1
#              if numero == secreto: print(f"¡Correcto en {intentos} intentos!") | break
#              elif numero < secreto: print("Más alto")
#              else: print("Más bajo")

# --- PISTAS 4.5 ---
# Pista 1: factorial = multiplicar todos los números de 1 hasta n
#          6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# Pista 2: # Con while:
#          resultado = 1
#          i = 1
#          while i <= n:
#              resultado *= i
#              i += 1
#          # Con for:
#          resultado = 1
#          for i in range(1, n + 1):
#              resultado *= i


# ================================================================
#  TEMA 5: STRINGS
# ================================================================

# --- PISTAS 5.1 ---
# Pista 1: los métodos de string se pueden encadenar: cadena.metodo1().metodo2().metodo3()
# Pista 2: nombre = "  JUAN PÉREZ  "
#          resultado = nombre.strip().lower().replace(" ", "_")

# --- PISTAS 5.2 ---
# Pista 1: existe un método que verifica con qué texto empieza un string
# Pista 2: url.startswith("https") devuelve True o False
#          if url.startswith("https"): print("URL segura")
#          else: print("URL insegura")

# --- PISTAS 5.3 ---
# Pista 1: split(separador) divide un string y devuelve una lista
# Pista 2: partes = email.split("@")
#          usuario = partes[0]
#          dominio = partes[1]

# --- PISTAS 5.4 ---
# Pista 1: len() cuenta caracteres | [0] accede al primer caracter | [-1] al último
# Pista 2: len(contrasena) >= 8          → longitud ok
#          not contrasena[0].isdigit()   → no empieza con número
#          " " not in contrasena         → sin espacios
#          contrasena[-1].isdigit()      → termina con número

# --- PISTAS 5.5 ---
# Pista 1: recorre la lista de palabras con for y aplica replace() en cada iteración
#          el resultado de replace() se guarda en la misma variable texto
# Pista 2: for palabra in palabras_clave:
#              texto = texto.replace(palabra, "*" * len(palabra))


# ================================================================
#  TEMA 6: LISTAS
# ================================================================

# --- PISTAS 6.1 ---
# Pista 1: append(x) agrega al final | insert(pos, x) inserta en posición
#          remove(x) elimina la primera aparición del valor
# Pista 2: frutas.append("mango")
#          frutas.insert(1, "fresa")
#          frutas.remove("pera")

# --- PISTAS 6.2 ---
# Pista 1: sort(reverse=True) ordena de mayor a menor
#          slicing lista[inicio:fin] extrae una parte de la lista
# Pista 2: puntajes.sort(reverse=True)
#          top3 = puntajes[:3]
#          peores3 = puntajes[-3:]

# --- PISTAS 6.3 ---
# Pista 1: crea lista vacía | recorre con for | continue salta al siguiente elemento
# Pista 2: lecturas_validas = []
#          for lectura in lecturas:
#              if lectura == 0: continue
#              lecturas_validas.append(lectura)
#          promedio = sum(lecturas_validas) / len(lecturas_validas)

# --- PISTAS 6.4 ---
# Pista 1: enumerate() devuelve el índice y el valor en cada iteración del for
# Pista 2: for i, resultado in enumerate(resultados):
#              if resultado == "FAIL_CRIT":
#                  print(f"Falla crítica encontrada en el índice: {i}")
#                  break

# --- PISTAS 6.5 ---
# Pista 1: append() agrega al final | pop() elimina y retorna el último elemento
# Pista 2: historial.append("copiar")
#          historial.append("pegar")
#          historial.append("formatear")
#          for _ in range(2):
#              accion = historial.pop()
#              print(f"Deshaciendo: {accion}")


# ================================================================
#  TEMA 7: EXCEPCIONES
# ================================================================

# --- PISTAS 7.1 ---
# Pista 1: try: código que puede fallar  |  except TipoDeError: qué hacer si falla
# Pista 2: try:
#              numero = int(texto)
#              print(f"Número convertido: {numero + 1}")
#          except ValueError:
#              print("Error: no es un número válido")

# --- PISTAS 7.2 ---
# Pista 1: finally se ejecuta siempre, haya error o no
# Pista 2: try:
#              resultado = a / b
#              print(f"Resultado: {resultado}")
#          except ZeroDivisionError:
#              print("Error: división entre cero")
#          finally:
#              print("Operación finalizada")

# --- PISTAS 7.3 ---
# Pista 1: puedes tener múltiples bloques except después de un try
# Pista 2: for dato in datos:
#              try:
#                  print(f"100 / {dato} = {round(100/dato, 2)}")
#              except TypeError:
#                  print("Error tipo: no se puede dividir entre string")
#              except ZeroDivisionError:
#                  print("Error división: no se puede dividir entre cero")

# --- PISTAS 7.4 ---
# Pista 1: open("archivo", "r") intenta leer | open("archivo", "w") crea/escribe
# Pista 2: try:
#              archivo = open(nombre_archivo, "r")
#          except FileNotFoundError:
#              print("Archivo no encontrado, creando uno nuevo...")
#              archivo = open(nombre_archivo, "w")
#              archivo.write("Archivo creado automáticamente")
#          finally:
#              print("Proceso de archivo terminado")

# --- PISTAS 7.5 ---
# Pista 1: raise ValueError("mensaje") lanza un error manualmente
#          except ValueError as e: captura el error y guarda el mensaje en e
# Pista 2: while True:
#              try:
#                  n = int(input("Ingresa número (1-10): "))
#                  if n < 1 or n > 10:
#                      raise ValueError("fuera de rango, intenta de nuevo")
#                  print(f"Número aceptado: {n}")
#                  break
#              except ValueError as e:
#                  print(f"Error: {e}")


# ================================================================
#  TEMA 8: EXPRESIONES REGULARES
# ================================================================

# --- PISTAS 8.1 ---
# Pista 1: \d representa cualquier dígito (0-9) | + significa 1 o más veces
#          ^ ancla al inicio | $ ancla al final del string
# Pista 2: patron = r"^\d+$"
#          if re.match(patron, codigo): print("Solo dígitos")
#          else: print("Contiene otros caracteres")

# --- PISTAS 8.2 ---
# Pista 1: re.findall() devuelve una lista con todas las coincidencias encontradas
# Pista 2: numeros = re.findall(r"\d+", texto)
#          print(f"Números encontrados: {numeros}")

# --- PISTAS 8.3 ---
# Pista 1: una IP tiene 4 grupos de 1 a 3 dígitos separados por puntos
#          \b marca el límite de una palabra | \. es un punto literal
# Pista 2: patron = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
#          ips = re.findall(patron, log)

# --- PISTAS 8.4 ---
# Pista 1: re.match() verifica desde el inicio del string
#          {2,3} significa exactamente 2 o 3 repeticiones
# Pista 2: patron = r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
#          if re.match(patron, email): print("Válido")
#          else: print("Inválido")

# --- PISTAS 8.5 ---
# Pista 1: re.sub(patron, reemplazo, texto) reemplaza todas las coincidencias
# Pista 2: texto = re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}", "****-****-****-****", texto)
#          texto = re.sub(r"[\w]+@[\w]+\.[\w]+", "[EMAIL OCULTO]", texto)
