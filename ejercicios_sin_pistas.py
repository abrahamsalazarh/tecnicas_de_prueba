# ================================================================
#  EJERCICIOS TDL - PYTHON
#  Taller: Programación con Python (TPS)
#
#  REGLAS:
#  1. Lee el PROBLEMA y el OUTPUT ESPERADO
#  2. Cierra el notebook del profesor
#  3. Intenta resolverlo SOLO — mínimo 15 minutos
#  4. Si no puedes, abre el archivo: pistas_ejercicios.py
#  5. Al día siguiente repite el ejercicio SIN ver tu solución
# ================================================================


# ================================================================
#  TEMA 1: OPERADORES Y VARIABLES
# ================================================================
print("\n" + "="*55)
print("  TEMA 1: OPERADORES Y VARIABLES")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 1.1
# PROBLEMA:
#   Un arquitecto necesita calcular el área y perímetro
#   de una habitación rectangular de 8m x 5m.
#
# OUTPUT ESPERADO:
#   Área: 40
#   Perímetro: 26
#
# RESTRICCIÓN: usa una sola línea para definir ambas variables
# ----------------------------------------------------------------
print("\n--- Ejercicio 1.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 1.2
# PROBLEMA:
#   Un sistema de turnos determina si el número de tarea
#   17 es par o impar usando solo matemáticas, sin if.
#
# OUTPUT ESPERADO:
#   Número: 17
#   Residuo: 1
#
# RESTRICCIÓN: no uses if, solo operadores matemáticos
# ----------------------------------------------------------------
print("\n--- Ejercicio 1.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 1.3
# PROBLEMA:
#   Un sistema de salud calcula el IMC de un paciente
#   que pesa 70.5 kg y mide 1.75 m. El límite normal es 24.9.
#
# OUTPUT ESPERADO:
#   IMC: 23.02
#   Límite normal: 24.9
#
# RESTRICCIÓN: resultado con exactamente 2 decimales
#              la constante en MAYÚSCULAS
# ----------------------------------------------------------------
print("\n--- Ejercicio 1.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 1.4
# PROBLEMA:
#   Un corredor terminó una carrera en 3725 segundos.
#   El sistema debe mostrar ese tiempo en formato legible.
#
# OUTPUT ESPERADO:
#   1 hora(s), 2 minuto(s), 5 segundo(s)
#
# RESTRICCIÓN: no uses librerías, solo operadores // y %
# ----------------------------------------------------------------
print("\n--- Ejercicio 1.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 1.5
# PROBLEMA:
#   Dos servidores deben intercambiar sus valores a=15 y b=42
#   sin usar una tercera variable. Verifica que la suma no cambie.
#
# OUTPUT ESPERADO:
#   Antes:   a=15, b=42, suma=57
#   Después: a=42, b=15, suma=57
#
# RESTRICCIÓN: no uses variable temporal auxiliar
# ----------------------------------------------------------------
print("\n--- Ejercicio 1.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 2: CONDICIONALES
# ================================================================
print("\n" + "="*55)
print("  TEMA 2: CONDICIONALES")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 2.1
# PROBLEMA:
#   Un sensor devuelve valores que pueden ser positivos,
#   negativos o cero. Clasifica el número -8.
#
# OUTPUT ESPERADO:
#   El número -8 es negativo
#
# RESTRICCIÓN: debes cubrir los 3 casos posibles
# ----------------------------------------------------------------
print("\n--- Ejercicio 2.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 2.2
# PROBLEMA:
#   Un sistema universitario clasifica la nota 78.
#
# OUTPUT ESPERADO:
#   Nota: 78 → Aprobado
#
# RANGOS:
#   90-100 → Sobresaliente
#   70-89  → Aprobado
#   50-69  → Suficiente
#   0-49   → Reprobado
# ----------------------------------------------------------------
print("\n--- Ejercicio 2.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 2.3
# PROBLEMA:
#   Un sistema permite acceso solo si el usuario es "admin",
#   la contraseña es "1234" y los intentos no superan 3.
#   usuario="admin", contraseña="1234", intentos=2
#
# OUTPUT ESPERADO:
#   Acceso permitido
#
# RESTRICCIÓN: usa and en una sola expresión booleana
# ----------------------------------------------------------------
print("\n--- Ejercicio 2.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 2.4
# PROBLEMA:
#   Una calculadora recibe dos números y una operación como
#   string. Calcula 10 / 4. Si se divide entre 0, error.
#
# OUTPUT ESPERADO:
#   10 / 4 = 2.5
#
# RESTRICCIÓN: operación como variable string
#              maneja la división entre cero
# ----------------------------------------------------------------
print("\n--- Ejercicio 2.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 2.5
# PROBLEMA:
#   Un sistema recibe 3 lados (a=5, b=5, c=8) y debe
#   verificar si forman triángulo y clasificarlo.
#
# OUTPUT ESPERADO:
#   Triángulo válido → Isósceles
#
# TIPOS:
#   Equilátero: 3 lados iguales
#   Isósceles:  2 lados iguales
#   Escaleno:   todos diferentes
# ----------------------------------------------------------------
print("\n--- Ejercicio 2.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 3: FUNCIONES + TYPE HINTS
# ================================================================
print("\n" + "="*55)
print("  TEMA 3: FUNCIONES + TYPE HINTS")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 3.1
# PROBLEMA:
#   El sistema de onboarding necesita generar mensajes
#   de bienvenida personalizados.
#
# OUTPUT ESPERADO:
#   Hola, Abraham! Bienvenido al taller.
#   Hola, Mundo! Bienvenido al taller.
#
# RESTRICCIÓN: type hints en parámetro y retorno
#              la función retorna el string, no lo imprime
# ----------------------------------------------------------------
print("\n--- Ejercicio 3.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 3.2
# PROBLEMA:
#   Un sistema meteorológico convierte temperaturas.
#   Crea dos funciones: Celsius→Fahrenheit y Fahrenheit→Celsius.
#
# OUTPUT ESPERADO:
#   0°C = 32.0°F
#   100°C = 212.0°F
#   98.6°F = 37.0°C
#
# RESTRICCIÓN: type hints en ambas funciones
# ----------------------------------------------------------------
print("\n--- Ejercicio 3.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 3.3
# PROBLEMA:
#   Una tienda aplica descuentos. Si el porcentaje está
#   fuera de 0-100, retorna el precio sin cambios.
#
# OUTPUT ESPERADO:
#   Precio final: 170.0
#   Precio final: 500.0   ← porcentaje 110 es inválido
#
# RESTRICCIÓN: type hints completos | valida el porcentaje
# ----------------------------------------------------------------
print("\n--- Ejercicio 3.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 3.4
# PROBLEMA:
#   Un sistema genera IDs de usuario. El separador por
#   defecto es "." pero puede cambiarse.
#
# OUTPUT ESPERADO:
#   juan.perez
#   juan_perez
#
# RESTRICCIÓN: parámetro con valor por defecto
#              resultado siempre en minúsculas
# ----------------------------------------------------------------
print("\n--- Ejercicio 3.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 3.5
# PROBLEMA:
#   Un framework de testing configura entornos de prueba.
#   La URL es obligatoria. El resto son opcionales:
#   browser(chrome), retries(1), timeout(30).
#
# OUTPUT ESPERADO:
#   URL: https://app.com | Browser: chrome | Reintentos: 1 | Timeout: 30
#   URL: https://app.com | Browser: firefox | Reintentos: 1 | Timeout: 30
#   URL: https://app.com | Browser: safari | Reintentos: 3 | Timeout: 60
#
# RESTRICCIÓN: usa **kwargs con .get() para los opcionales
# ----------------------------------------------------------------
print("\n--- Ejercicio 3.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 4: BUCLES
# ================================================================
print("\n" + "="*55)
print("  TEMA 4: BUCLES")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 4.1
# PROBLEMA:
#   Genera la tabla de multiplicar del 7 del 1 al 10.
#
# OUTPUT ESPERADO:
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
# RESTRICCIÓN: usa for con range()
# ----------------------------------------------------------------
print("\n--- Ejercicio 4.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 4.2
# PROBLEMA:
#   Un sistema de lanzamiento necesita cuenta regresiva
#   del 10 al 1, luego muestra el mensaje de despegue.
#
# OUTPUT ESPERADO:
#   10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#   ¡Despegue!
#
# RESTRICCIÓN: usa while, no for
# ----------------------------------------------------------------
print("\n--- Ejercicio 4.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 4.3
# PROBLEMA:
#   Resuelve FizzBuzz del 1 al 30.
#
# REGLAS:
#   múltiplo de 3 y 5 → FizzBuzz
#   múltiplo de 3     → Fizz
#   múltiplo de 5     → Buzz
#   si no             → el número
# ----------------------------------------------------------------
print("\n--- Ejercicio 4.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 4.4
# PROBLEMA:
#   Crea un juego para adivinar el número secreto (7).
#   El sistema da pistas y cuenta los intentos.
#
# OUTPUT ESPERADO:
#   Intento 1: 3 → Más alto
#   Intento 2: 9 → Más bajo
#   Intento 3: 7 → ¡Correcto en 3 intentos!
#
# RESTRICCIÓN: usa while True con break
# ----------------------------------------------------------------
print("\n--- Ejercicio 4.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 4.5
# PROBLEMA:
#   Calcula el factorial de 6 usando DOS métodos: while y for.
#   Ambos deben dar 720.
#
# OUTPUT ESPERADO:
#   Factorial de 6 (while) = 720
#   Factorial de 6 (for)   = 720
#
# RESTRICCIÓN: no uses math.factorial()
# ----------------------------------------------------------------
print("\n--- Ejercicio 4.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 5: STRINGS Y SUS MÉTODOS
# ================================================================
print("\n" + "="*55)
print("  TEMA 5: STRINGS Y SUS MÉTODOS")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 5.1
# PROBLEMA:
#   Normaliza el nombre "  JUAN PÉREZ  " para usarlo
#   como username en base de datos.
#
# OUTPUT ESPERADO:
#   juan_pérez
#
# RESTRICCIÓN: una sola línea encadenando métodos
# ----------------------------------------------------------------
print("\n--- Ejercicio 5.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 5.2
# PROBLEMA:
#   Un escáner verifica que las URLs usen protocolo seguro.
#
# OUTPUT ESPERADO:
#   https://www.ejemplo.com → URL segura
#   http://sitio.com → URL insegura
#
# RESTRICCIÓN: usa un método de string, no in ni ==
# ----------------------------------------------------------------
print("\n--- Ejercicio 5.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 5.3
# PROBLEMA:
#   Un sistema separa el usuario del dominio en un correo.
#
# OUTPUT ESPERADO:
#   usuario@empresa.com    → usuario: usuario  | dominio: empresa.com
#   contacto@google.com.mx → usuario: contacto | dominio: google.com.mx
#
# RESTRICCIÓN: usa split(), sin índices manuales ni regex
# ----------------------------------------------------------------
print("\n--- Ejercicio 5.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 5.4
# PROBLEMA:
#   Un sistema valida la contraseña "miPass123" con 4 reglas.
#
# OUTPUT ESPERADO:
#   ✓ Longitud mínima de 8 caracteres
#   ✓ No empieza con número
#   ✓ No tiene espacios
#   ✓ Termina con número
#
# REGLAS: mínimo 8 chars | no empieza con dígito
#         sin espacios | termina con dígito
# ----------------------------------------------------------------
print("\n--- Ejercicio 5.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 5.5
# PROBLEMA:
#   Un sistema censura palabras críticas en logs.
#   Reemplaza cada palabra por asteriscos del mismo largo.
#
# INPUT:
#   "El error fue CRITICO y el fallo fue GRAVE en el sistema"
#   palabras: ["CRITICO", "GRAVE"]
#
# OUTPUT ESPERADO:
#   Original:  El error fue CRITICO y el fallo fue GRAVE en el sistema
#   Censurado: El error fue ******* y el fallo fue ***** en el sistema
#
# RESTRICCIÓN: asteriscos del mismo largo que la palabra
# ----------------------------------------------------------------
print("\n--- Ejercicio 5.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 6: LISTAS
# ================================================================
print("\n" + "="*55)
print("  TEMA 6: LISTAS")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 6.1
# PROBLEMA:
#   Sobre la lista ["manzana","pera","uva"]: agrega "mango"
#   al final, inserta "fresa" en posición 1, elimina "pera".
#
# OUTPUT ESPERADO:
#   Lista final: ['manzana', 'fresa', 'uva', 'mango']
#   Total: 4
# ----------------------------------------------------------------
print("\n--- Ejercicio 6.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 6.2
# PROBLEMA:
#   Muestra el top 3 y los 3 peores de esta lista:
#   puntajes = [88, 45, 97, 63, 72, 55, 91]
#
# OUTPUT ESPERADO:
#   Top 3:    [97, 91, 88]
#   Peores 3: [45, 55, 63]
#
# RESTRICCIÓN: usa sort() y slicing
# ----------------------------------------------------------------
print("\n--- Ejercicio 6.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 6.3
# PROBLEMA:
#   Filtra los ceros (errores) de las lecturas de un sensor
#   y calcula el promedio de las válidas.
#   lecturas = [10.5, 0, 12.1, 0, 0, 15.3, 9.8]
#
# OUTPUT ESPERADO:
#   Lecturas válidas: [10.5, 12.1, 15.3, 9.8]
#   Promedio: 11.925
#
# RESTRICCIÓN: usa continue para saltar los ceros
# ----------------------------------------------------------------
print("\n--- Ejercicio 6.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 6.4
# PROBLEMA:
#   Encuentra la primera falla crítica en la lista y su posición.
#   resultados = ["PASS", "PASS", "FAIL_SOFT", "FAIL_CRIT", "PASS"]
#
# OUTPUT ESPERADO:
#   Falla crítica encontrada en el índice: 3
#
# RESTRICCIÓN: usa enumerate() y break
# ----------------------------------------------------------------
print("\n--- Ejercicio 6.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 6.5
# PROBLEMA:
#   Implementa un sistema Undo. Parte de ["abrir","editar",
#   "guardar"], agrega 3 acciones más, deshaz las últimas 2.
#
# OUTPUT ESPERADO:
#   Historial: ['abrir', 'editar', 'guardar', 'copiar', 'pegar', 'formatear']
#   Deshaciendo: formatear
#   Deshaciendo: pegar
#   Historial final: ['abrir', 'editar', 'guardar', 'copiar']
#
# RESTRICCIÓN: usa pop() dentro de un for
# ----------------------------------------------------------------
print("\n--- Ejercicio 6.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 7: MANEJO DE EXCEPCIONES
# ================================================================
print("\n" + "="*55)
print("  TEMA 7: MANEJO DE EXCEPCIONES")
print("="*55)

# ----------------------------------------------------------------
# EJERCICIO 7.1
# PROBLEMA:
#   Un sistema convierte datos a número. Si falla, lo maneja.
#
# OUTPUT ESPERADO (texto="abc"):
#   Error: no es un número válido
#
# OUTPUT ESPERADO (texto="42"):
#   Número convertido: 43
#
# RESTRICCIÓN: usa try/except ValueError
# ----------------------------------------------------------------
print("\n--- Ejercicio 7.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 7.2
# PROBLEMA:
#   Una calculadora maneja la división entre cero y siempre
#   reporta que terminó la operación.
#
# OUTPUT ESPERADO (b=0):
#   Error: división entre cero
#   Operación finalizada
#
# OUTPUT ESPERADO (b=4):
#   Resultado: 2.5
#   Operación finalizada
#
# RESTRICCIÓN: usa try/except/finally
# ----------------------------------------------------------------
print("\n--- Ejercicio 7.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 7.3
# PROBLEMA:
#   Un procesador divide 100 entre datos mixtos y maneja
#   errores distintos por separado.
#   datos = [10, "veinte", 30, 0, 40]
#
# OUTPUT ESPERADO:
#   100 / 10 = 10.0
#   Error tipo: no se puede dividir entre string
#   100 / 30 = 3.33
#   Error división: no se puede dividir entre cero
#   100 / 40 = 2.5
#
# RESTRICCIÓN: captura TypeError y ZeroDivisionError por separado
# ----------------------------------------------------------------
print("\n--- Ejercicio 7.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 7.4
# PROBLEMA:
#   Un sistema lee un archivo. Si no existe, lo crea.
#   Siempre reporta que terminó el proceso.
#
# OUTPUT ESPERADO (archivo no existe):
#   Archivo no encontrado, creando uno nuevo...
#   Proceso de archivo terminado
#
# RESTRICCIÓN: usa try/except FileNotFoundError/finally
# ----------------------------------------------------------------
print("\n--- Ejercicio 7.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 7.5
# PROBLEMA:
#   Un sistema pide un número entre 1 y 10. Si el usuario
#   escribe texto o número fuera de rango, vuelve a pedir.
#
# OUTPUT ESPERADO:
#   Ingresa número (1-10): abc  → Error: entrada inválida
#   Ingresa número (1-10): 15  → Error: fuera de rango
#   Ingresa número (1-10): 7   → Número aceptado: 7
#
# RESTRICCIÓN: while True + try/except + raise ValueError
# ----------------------------------------------------------------
print("\n--- Ejercicio 7.5 ---")
# TU SOLUCIÓN:


# ================================================================
#  TEMA 8: EXPRESIONES REGULARES
# ================================================================
print("\n" + "="*55)
print("  TEMA 8: EXPRESIONES REGULARES")
print("="*55)

import re

# ----------------------------------------------------------------
# EJERCICIO 8.1
# PROBLEMA:
#   Un sistema valida que los códigos contengan solo dígitos.
#
# OUTPUT ESPERADO:
#   12345  → Solo dígitos
#   123abc → Contiene otros caracteres
#   00789  → Solo dígitos
#
# RESTRICCIÓN: usa re.match() con anclas ^ y $
# ----------------------------------------------------------------
print("\n--- Ejercicio 8.1 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 8.2
# PROBLEMA:
#   Un sistema extrae todos los números de una descripción.
#   "El pedido 4521 tiene 3 artículos por $199 cada uno"
#
# OUTPUT ESPERADO:
#   Números encontrados: ['4521', '3', '199']
#
# RESTRICCIÓN: usa re.findall()
# ----------------------------------------------------------------
print("\n--- Ejercicio 8.2 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 8.3
# PROBLEMA:
#   Un sistema extrae IPs de un log de red para auditarlas.
#   "Falla en 192.168.1.15 y error en 10.0.0.1 y timeout"
#
# OUTPUT ESPERADO:
#   IPs encontradas: ['192.168.1.15', '10.0.0.1']
#
# RESTRICCIÓN: usa re.findall() con patrón de IP
# ----------------------------------------------------------------
print("\n--- Ejercicio 8.3 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 8.4
# PROBLEMA:
#   Un sistema valida correos antes de registrarlos.
#
# OUTPUT ESPERADO:
#   contacto@empresa.com  → Válido
#   usuario@dominio       → Inválido
#   test.user@correo.mx   → Inválido
#
# PATRÓN: letras/números + @ + solo letras + . + 2-3 letras
# ----------------------------------------------------------------
print("\n--- Ejercicio 8.4 ---")
# TU SOLUCIÓN:


# ----------------------------------------------------------------
# EJERCICIO 8.5
# PROBLEMA:
#   Un sistema enmascara datos sensibles en logs.
#   "Tarjeta: 4532-1234-5678-9012 del cliente juan@mail.com"
#
# OUTPUT ESPERADO:
#   Original:    Tarjeta: 4532-1234-5678-9012 del cliente juan@mail.com
#   Enmascarado: Tarjeta: ****-****-****-**** del cliente [EMAIL OCULTO]
#
# RESTRICCIÓN: usa re.sub() dos veces
# ----------------------------------------------------------------
print("\n--- Ejercicio 8.5 ---")
# TU SOLUCIÓN:


print("\n" + "="*55)
print("  ¡Fin de los ejercicios!")
print("  Si te atascaste → abre pistas_ejercicios.py")
print("  Mañana repite los que más te costaron")
print("="*55 + "\n")
