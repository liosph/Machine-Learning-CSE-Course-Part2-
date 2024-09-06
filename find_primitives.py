## Modify the number here:
# Input from the user
# number = 132 for standard usage
number = int(input("Enter the number (integer) you want to calculate the dimensions for:"))

dividers = range(2,100)

results = []
for i in dividers:
    div = number/i
    mod = number % i
    if mod == 0:
        results.append((div,i))
if len(results)==0:
    print("The number is prime...")
    print("Opt for 'Solution 2' \nOR\nRun the \n'Samples Selection' part of the code again\n(in order to achieve different results from the PCA Method)")


for dim1,dim2 in results:
    print("Dimension 1: " ,dim1)
    print("Dimension 2: " ,dim2)
    print("Modify the reshape_dims variable as:({},{})".format(dim1,dim2))
    print("----------------------------------------------------------------")
