import search
 
inputstr = input('Enter hashed value to search, type "done" to leave: ')
pwtable = search.create_table()

while inputstr != 'done':
    hashed = int(inputstr)
    found, found_pw, found_salt, search_count = search.search(hashed, pwtable)
     
    if found:
        print('Search success!\n')
        print(f'Password: {found_pw}')
        print(f'Salt: {found_salt}')
        print(f'Number of searches: {search_count}')
        print()
    else:
        print('Search failed!\n')
        print(f'Number of searches: {search_count}')
        print()

    inputstr = input('Enter hashed value to search, type "done" to leave: ')
