if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())  
    my_list = [[i,j,v] for i in range (x+1) for j in range (y+1) for v in range (z+1) if ((0 <= i <= x) and (0 <= j <= y) and (0 <= v <= z) and (i+j+v != n))];
    print(my_list);
