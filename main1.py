def main():
   n1 = int(input("Introduce el primer numero: "))
   n2 = int(input("Introduce el segundo numero: "))

   if n1 > n2:
      print("Error")
   else:
     for n1 in range (n1, n2):
        print(n1)
        n1 += 1

if __name__ == '__main__':
  main()
