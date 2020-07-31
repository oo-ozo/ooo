def main():
    from os import system as ter
    from sys import argv as a
    ter("clear")
    print("{} is need to import".format(a[0]))
    print("this module is made by Tricker")
    print("this module is in {} don\'t change it".format("$HOME/usr/lib/python3.8/"))
        
red = "\033[31m"
white = "\033[m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
cyan = "\033[36m"

def show_color():
    print(red+"red")
    print(white+"white")
    print(green+"green")
    print(yellow+"yellow")
    print(blue+"blue")
    print(purple+"purple")
    print(cyan+"cyan"+white)

def color(x):
    if x == "red":
        return red
    elif x == 'white':
        return white
    elif x == 'green':
        return green
    elif x == 'yellow':
        return yellow
    elif x == 'blue':
        return blue
    elif x == 'purple':
        return purple
    elif x == 'cyan':
        return cyan
        

def square(x,y):
    sq="""
            {1}##############################
                        {0}          
            ##############################{2}"""
    if y == "white":
        return sq.format(x,white,white)
    elif y == "red":
        return sq.format(x, red, white)
    elif y == "green":
        return sq.format(x, green, white)
    elif y == "yellow":
        return sq.format(x, yellow, white)
    elif y == "blue":
        return sq.format(x, blue, white)
    elif y == "purple":
        return sq.format(x, purple, white)
    elif y == "cyan":
        return sq.format(x, cyan, white)

def line():
    p="""
_______________________________________________________"""
    return p

def big(x):
    import os
    return os.system("figlet " + x)

def cow_say(x):
    import os
    os.system("cowsay "+x)


if __name__ == '__main__':
    main()
