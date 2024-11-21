import random
import math


def validar_rango(op, min, may):
    if op is not None:
        return op in range(min, may+1)
    return False


def es_primo(n):
    if n == 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return False
    raiz = math.trunc(math.sqrt(n))
    for i in range(3, raiz+1, 2):
        if n % i == 0:
            return False
    return True


def siguiente_primo(n):
    if n % 2 == 0:
        n += 1
    while not es_primo(n):
        n += 2
    return n


def generar_primo_de_n_bits(bitn):
    min = 10 ** (bitn - 1)
    may = 10 ** bitn - 1
    primo = random.randint(min, may)
    return siguiente_primo(primo)


def generar_primo_hasta(min):
    primo = random.randint(0, min)
    return siguiente_primo(primo)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x-(b//a)*y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def generar_keys(klen):
    p = generar_primo_de_n_bits(klen)
    q = generar_primo_de_n_bits(klen)
    n = p * q
    phi = (p-1) * (q-1)
    e = generar_primo_hasta(phi - 1)
    while phi % e == 0:
        e = generar_primo_hasta(phi - 1)
    d = modinv(e, phi)
    key_privada = (e, n)
    key_publica = (d, n)
    return key_privada, key_publica


def calcular_desplazamiento(n):
    bits = 0
    while n > 0:
        bits += 1
        n >>= 1
    return bits


def cifrar(txt, key):
    ret = 0
    desplazamiento = calcular_desplazamiento(key[1])
    for caracter in txt:
        ret <<= desplazamiento
        caracter_ascii = ord(caracter)
        caracter_ascii_cifrado = (caracter_ascii ** key[0]) % key[1]
        ret += caracter_ascii_cifrado
    return ret


def descifrar(msg_int, key):
    ret = []
    msg_int = int(msg_int)
    desplazamiento = calcular_desplazamiento(key[1])
    max_desplazamiento = 2 ** desplazamiento - 1
    while msg_int > 0:
        caracter_ascii = msg_int & max_desplazamiento
        caracter_ascii_descifrado = (caracter_ascii ** key[0]) % key[1]
        ret.insert(0, chr(caracter_ascii_descifrado))
        msg_int >>= desplazamiento
    return ''.join(ret)


def pausa():
    input("Presione Enter para continuar...")


def main():

    # Mensaje de inicializacion
    print("Cifrado asimetrico")

    # Variables generales
    op = 1
    key_privada = None
    key_publica = None

    # Bucle principal
    while validar_rango(op, 1, 7):

        # Imprimo opciones
        print("\n1) Generar claves")
        print("2) Ingresar claves manualmente")
        print("3) Encriptar mensaje con clave privada")
        print("4) Encriptar mensaje con clave publica")
        print("5) Desencriptar mensaje con clave privada")
        print("6) Desencriptar mensaje con clave publica")
        print("7) Mostrar claves")
        print("8) Salir\n")

        # Solicito opcion
        op = int(input('Ingrese opcion: '))

        # Realizo acciones segun opcion
        if op == 1:
            klen = int(input("\nIngrese el orden de p y q: "))
            key_privada, key_publica = generar_keys(klen)
            print("Su clave privada actual es:", key_privada)
            print("Su clave publica actual es:", key_publica)
            pausa()

        elif op == 2:
            key_priv = int(input("\nIngrese su clave privada manualmente: "))
            key_publ = int(input("\nIngrese su clave publica manualmente: "))
            n = int(input("\nIngrese su numero n manualmente: "))
            key_privada = (key_priv, n)
            key_publica = (key_publ, n)
            print("Su clave privada actual es:", key_privada)
            print("Su clave publica actual es:", key_publica)
            pausa()

        elif op == 3:
            if key_privada is None or key_publica is None:
                print("\nDebe generar sus claves antes de encriptar o desencriptar")
                pausa()
                continue
            msg = input("\nIngrese el mensaje a escriptar: ")
            if msg == "":
                print("Su mensaje no puede ser vacio")
                pausa()
                continue
            msg_encriptado = cifrar(msg, key_privada)
            print("Su mensaje encriptado es:", msg_encriptado)
            pausa()

        elif op == 4:
            if key_privada is None or key_publica is None:
                print("\nDebe generar sus claves antes de encriptar o desencriptar")
                pausa()
                continue
            msg = input("\nIngrese el mensaje a escriptar: ")
            if msg == "":
                print("Su mensaje no puede ser vacio")
                pausa()
                continue
            msg_encriptado = cifrar(msg, key_publica)
            print("Su mensaje encriptado es:", msg_encriptado)
            pausa()

        elif op == 5:
            if key_privada is None or key_publica is None:
                print("\nDebe generar sus clave antes de encriptar o desencriptar")
                pausa()
                continue
            msg = input("\nIngrese el mensaje a desescriptar: ")
            if msg == "":
                print("Su mensaje no puede ser vacio")
                pausa()
                continue
            msg_desencriptado = descifrar(msg, key_privada)
            print("Su mensaje desencriptado es:", msg_desencriptado)
            pausa()

        elif op == 6:
            if key_privada is None or key_publica is None:
                print("\nDebe generar sus clave antes de encriptar o desencriptar")
                pausa()
                continue
            msg = input("\nIngrese el mensaje a desescriptar: ")
            if msg == "":
                print("Su mensaje no puede ser vacio")
                pausa()
                continue
            msg_desencriptado = descifrar(msg, key_publica)
            print("Su mensaje desencriptado es:", msg_desencriptado)
            pausa()

        elif op == 7:
            print("\nSu clave privada actual es: ", key_privada)
            print("\nSu clave publica actual es: ", key_publica)
            pausa()

    # Mensaje de finalizacion
    print("\nFin del programa")


if __name__ == '__main__':
    main()


