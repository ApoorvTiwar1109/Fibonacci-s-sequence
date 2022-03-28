#Fibonacci sequence
#0 1 1 2 3 5 8 13 21...
index = int(input("Enter the term till which you wanto print the fibonacci sequence : "))
term_1 = 0
term_2 = 1
x = 0
if index == 1:
    print(term_1)
else:
    while x < index:
        print(term_1)
        numbers = term_1 + term_2
        term_1 = term_2
        term_2 = numbers
        x += 1