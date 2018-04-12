#Complete the mode function to make it return the mode of a list of numbers
data1=[1,2,5,10,-20,5,5]
def mode(data):
    #Insert your code here
    d = dict()

    for i in range(len(data)):
        if data[i] in d:
            d[data[i]] += 1
        else:
            d[data[i]] = 1
    
    sorted_d = sorted(d.items(), key=lambda key: key[1], reverse=True)
    return sorted_d[0][0]

print(mode(data1))        
