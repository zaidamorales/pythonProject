# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
   aux = aux2 = 0
   num = int(input("Introdueix un nombre enter: "))
   while num < 1:
      num = int(input("Introdueix un nombre enter: "))
   for x in range(num):
      aux += x
      if aux < num:
         print(x, end= " ")
         aux2 += x
   print("\nLa suma dels valors és: ", aux2)

if __name__ == '__main__':
   main()

