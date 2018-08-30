'''Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.'''

dimensions = str(input("Please enter the two dimensions(comma seperated): "))
dimension = dimensions.split(',')
twoDlist = [[0 for x in range(int(dimension[1]))] for y in range(int(dimension[0]))]

for y in range(int(dimension[0])):
    for x in range(int(dimension[1])):
        twoDlist[y][x] = x*y

print(twoDlist)

