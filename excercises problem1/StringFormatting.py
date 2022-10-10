def print_formatted(n):
     length = len(bin(n)[2:])
     for i in range (1, (n+1)):
                oc = str(oct(i))[2:]
                he = str(hex(i))[2:].upper()
                bi = str (bin(i))[2:]
                print( str(i).rjust(length), oc.rjust(length), he.rjust(length), bi.rjust(length))

