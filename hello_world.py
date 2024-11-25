import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub, tequiero :)!")

if __name__ == "__main__":
    main()