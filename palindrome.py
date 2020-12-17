count = 1     
def make_pal(x,new_pal=''):
    str_num = str(x)
    for i in range(1,len(str_num)+1):
        new_pal = new_pal + str_num[i*-1]
    print(x,"Was Given")
    print(new_pal, "Is the Palinomal")
    return int(new_pal)

def check_pal(x,y=-1):
    str_num = str(x)
    for i in range(len(str_num)):
        a = str_num[i]
        b = str_num[y]
        if a == b:
            y -= 1
        else:
            return False
    return True

def find_pal(x):
    global count
    y = make_pal(int(x))
    z = int(x) + y
    print(x, '+', y,'=', z)
    if check_pal(z):
        print(z, 'is pal!')
    else:
        print()
        count += 1
        find_pal(z)


x = input('Enter a number to start with: ')
y = int(x)
find_pal(y)
print(f'it took {count} tries!')