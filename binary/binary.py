########## Two's complement ##############

'''
1. Get positive binary representation 
2. Invert bits in positive representation
3. Add 1
4. Prepend sign bit (1) to front

Ex. for n =3
Step 1. +ve rep     => 011
Step 2. flip bits   => 100
Step 3. add 1       => 101
Step 4. Sign bit    => 1101
'''



########## Conversion functions ##############


# Convert int to binary string
def int2binstr(n:int) -> str:
    m = n # copy number to retain original value after transforms
    n = n & 0b1111111111111111111
    s = "" # hold string
    while n > 0:
        i = n % 2
        n //= 2
        s = str(i) + s
    
    print(s, bin(m))
    assert s == bin(m).replace('0b', '')
    return s

int2binstr(-12312312)


# Convert int to binary number
def int2bin(n:int) -> int:
    m = n # Copy number to check at end
    s = 0 # hold sum
    e = 0 # exponent
    while n > 0:
        i = n % 2
        n //= 2
        s += i * 10 ** e
        e += 1
    
    print(s, bin(m)) 
    assert s == int(bin(m).replace('0b', ''))
    return s



# Convert binary number to int
def bin2int(b:int) -> int:
    a = b # copy number to check at end
    s = 0 # hold sum
    e = 0 # exponent
    while b > 0:
        i = b % 10
        b //= 10
        s += i * 2 ** e
        e += 1
        
    print(int(str(a), 2), s) 
    assert int(str(a), 2) == s
    return s    
            
