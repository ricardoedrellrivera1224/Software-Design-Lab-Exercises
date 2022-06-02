def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")

        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")

        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'RIVERA')
insert(HashTable, 25, 'MEJIA')
insert(HashTable, 20, 'ULEP')
insert(HashTable, 9, 'GARCIA')
insert(HashTable, 21, 'REYES')
insert(HashTable, 21, 'DEVERA')

display_hash(HashTable)