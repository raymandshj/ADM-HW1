# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 
numpy.set_printoptions(sign=' ')
print(numpy.eye(*map(int, input().split())))
