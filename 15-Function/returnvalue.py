#fungsi dengan return value

def kuadrat(argumen):
    total = argumen ** 2
    print(f'nilai kuadrat dari {argumen} adalah {total}')
    return total
a = kuadrat(3)
print(a)

print('+'*100)

#fungsi dengan return value dan multi argument
def tambah(argument1, argument2):
    total = argument1 + argument2
    print(f'{argument1} ditambah {argument2} sama dengan {total}')
    return total


def kali(argument1, argument2):
    total = argument1 * argument2
    print(f'{argument1} dikali {argument2} sama dengan {total}')
    return total


b = kali(3,tambah(3,4))

print(20*'=')
def smaller_num(x, y): ## Can be rephrased to  def smaller_num(x, y):
    if x > y:          ##                          if x > y:
        number = y     ##                              return y
    else:              ##                          else:
        number = x     ##                              return x
    return number

x = input("Enter first number:-")
y = input("Enter second number:-")
result = smaller_num(x, y)
print("The smaller number between " +  str(x) + " and " + str(y) + " is " + str(result))