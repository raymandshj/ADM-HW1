# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)

    except (ValueError, ZeroDivisionError) as error:
        print("Error Code:", error)
