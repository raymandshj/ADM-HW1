# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
shapes = list(map(int, input().split()))
print(numpy.zeros((shapes), dtype = numpy.int))
print(numpy.ones((shapes), dtype = numpy.int))
