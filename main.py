import os
import sys

class Main:
    def __init__(self):
        self.dev = 'Lotus Saga'
        self.version = '1.0.4'
        self.github = 'github.com/LotusCorp'

    def print_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''
                    .?B5^ 
                   !B@@@&J.  
                 :5@@@@@@@B~ 
                ^B@@@@@@@@@&7  
      7J7~:    .5@@@@@@@@@@@B^    .^7??.
      P@@@&GY!.  ^JB@@@@@#5~  .~JG#@@@#:
      Y@@@@@@@#5~   !G@#?:  ^JB@@@@@@@B.
      !@@@@@@@@@@G7.  ~:  ~P&@@@@@@@@@Y                 Developers..: {self.dev}
      .G@@@@@@@@@@@B!   ~P@@@@@@@@@@@&^                 Version.....: {self.version}
       !&@@@@@@@@@@@@P~Y&@@@@@@@@@@@@J                  Github......: {self.github}
        7&@@@@@@@@@@@@@@@@@@@@@@@@@@J                   
         ~B@@@@@@@@@@@@@@@@@@@@@@@#7 
          .?B@@@@@@@@@@@@@@@@@@@#J: 
            .~JG#@@@@@@@@@@@&BY!. 
            ''')

    def main_menu(self):
        print('''
    [1] Bash            [6] NetCat          [11] SoCat
    [2] Gawk            [7] Perl
    [3] GoLang          [8] PHP
    [4] Java            [9] Python
    [5] Lua             [10] Ruby
                ''')

        option = int(input('''[LOTUS] SELECT A REVERSE SHELL TO PRINT: '''))

        try:
            if option == 1:
                with open('./rs/bash.txt', 'r') as file:
                    print(file.read())
            elif option == 2:
                with open('./rs/gawk.txt', 'r') as file:
                    print(file.read())
            elif option == 3:
                with open('./rs/golang.txt', 'r') as file:
                    print(file.read())
            elif option == 4:
                with open('./rs/java.txt', 'r') as file:
                    print(file.read())
            elif option == 5:
                with open('./rs/lua.txt', 'r') as file:
                    print(file.read())
            elif option == 6:
                with open('./rs/netcat.txt', 'r') as file:
                    print(file.read())
            elif option == 7:
                with open('./rs/perl.txt', 'r') as file:
                    print(file.read())
            elif option == 8:
                with open('./rs/php.txt', 'r') as file:
                    print(file.read())
            elif option == 9:
                with open('./rs/python.txt', 'r') as file:
                    print(file.read())
            elif option == 10:
                with open('./rs/ruby.txt', 'r') as file:
                    print(file.read())
            elif option == 11:
                with open('./rs/socat.txt', 'r') as file:
                    print(file.read())
            else:
                print("Invalid option selected")

        except KeyboardInterrupt:
            print("\n[LOTUS] Exiting...")

if __name__ == '__main__':
    main = Main()
    main.print_banner()
    main.main_menu()
