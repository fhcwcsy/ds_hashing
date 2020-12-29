SEARCH_INPUT_FN = './list_pa2.txt'
SEARCH_OUTPUT_FN = 'results_pa2.txt' 
DICT_OUTPUT_FN = 'Dictionary.txt' 
SALTDIGIT = 3
PWLEN = 6
 
def create_table():
    with open(DICT_OUTPUT_FN) as fdict:
        pwtable = [(
            int(dictline.strip().split(' ')[2]),    # hash value in int
            dictline.strip().split(' ')[0],         # password
            dictline.strip().split(' ')[1]          # salt
            ) for dictline in fdict.readlines()]
    return pwtable

def search(hashed, pwtable):
    found = False
    for i in range(len(pwtable)):
        if pwtable[i][0] == hashed:
            found = True
            found_pw = pwtable[i][1]
            found_salt = pwtable[i][2]
            search_count = i+1
            break

    if not found:
        found_pw = '*'*PWLEN
        found_salt = '*'*SALTDIGIT
        search_count = len(pwtable)

    return found, found_pw, found_salt, search_count

if __name__ == "__main__":
    fin = open(SEARCH_INPUT_FN)
    fout = open(SEARCH_OUTPUT_FN, 'w')

    pwtable = create_table()

    for hashed_str in fin.readlines():
        hashed = int(hashed_str.strip())
        found, found_pw, found_salt, search_count = search(hashed, pwtable)
        result_str = f'{hashed} {found_pw} {found_salt} {search_count}\n'
        fout.write(result_str)


    fin.close()
    fout.close()
