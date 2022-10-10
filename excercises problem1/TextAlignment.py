# Enter your code here. Read input from STDIN. Print output to STDOUT
text = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(text):
    print((c*i).rjust(text-1)+c+(c*i).ljust(text-1))

#Top Pillars
for i in range(text+1):
    print((c*text).center(text*2)+(c*text).center(text*6))

#Middle Belt
for i in range((text+1)//2):
    print((c*text*5).center(text*6))    

#Bottom Pillars
for i in range(text+1):
    print((c*text).center(text*2)+(c*text).center(text*6))    

#Bottom Cone
for i in range(text):
    print(((c*(text-i-1)).rjust(text)+c+(c*(text-i-1)).ljust(text)).rjust(text*6))
