def main():

   state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
   vowels = [i for i in state.split() if len(i) <6]

   print(vowels)

if __name__ == '__main__':
   main()