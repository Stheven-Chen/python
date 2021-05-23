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