# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
   nom = input("Introduce el nombre: ")
   cognom = input("Introduce el pimer apellido: ")
   segundo = input("Introduce el segundo apellido: ")


   print ("*********************")

   print(cognom[:2], end="")
   print(segundo[:2], end="")
   print(nom[:2], end="")

if __name__ == '__main__':
   main()

