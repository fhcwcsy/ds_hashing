import sys

PASSWORD_FN = sys.argv[1]
DICT_OUTPUT_FN = 'Dictionary.txt' 
SALTSIZE = 1000
SALTDIGIT = 3
PWLEN = 6

def hashpswd(pswd):
    left = int(pswd[:8])
    right = int(pswd[8:])
    return ( (243*left) + right ) % 85767489 

with open(PASSWORD_FN) as fin:
    with open(DICT_OUTPUT_FN, 'w') as fout:
        for line in fin.readlines():

            pw = line.strip()
            if len(pw) == PWLEN:
            
                # char ord(char must be a 2-digit integer.
                pw_ascii = ''.join([str(ord(char)) for char in pw]) 

                for salt in range(SALTSIZE):
                    saltstr = ( '{:0>' + str(SALTDIGIT) + 'd}' ).format(salt)
                    fout.write( f'{pw} {saltstr} {hashpswd(saltstr+pw_ascii)}\n' )
    
