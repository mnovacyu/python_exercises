#Complete the median function to make it return the median of a list of numbers
data1=[1,2,5,10,-20]
#Function currently only works for a list with an odd number of elements
def median(data):
    #Insert your code here
    sorted_data = sorted(data)
    return sorted_data[int(len(data)/2)]

print(median(data1))
