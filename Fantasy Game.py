stuff = {'rope': 1, 'torch': 6, 'gold': 42, 'dagger': 1, 'arrow': 12}
loot = ['gold', 'dagger', 'gold', 'gold', 'ruby']

def dispinventory(inven):
    print('inventory:\n')
    for k, v in inven.items():
        print(k+'\t', v)


def addinventory(inven, ainven):

    for i in range(0, 5, 1):
        print(ainven[i], ' ', 'Added')

        if ainven[i] not in inven.items():
            inven.setdefault(ainven[i], 0)

        if ainven[i] in inven.keys():
            inven[ainven[i]] += 1


dispinventory(stuff)
print('\n')
print(loot)

addinventory(stuff,loot)

dispinventory(stuff)