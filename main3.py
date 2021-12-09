def main():

    llista = [x for x in range(0,1001)]
    llista_dos = [x for x in llista if str(x) in '6, 16, 26']

    print(llista_dos)

if __name__ == '__main__':
  main()
