'''
This script will rotate the table_data and print with right_aligned columns.
(Essentially a rewrite of the .rightjust method for strings)

FINAL OUTPUT:
  apples  Alice   dogs
 oranges    Bob   cats
cherries  Carol  moose
  banana  David  goose


'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

max_lengths = []
length_diff = {}

# find max word lengths in each row
def getMaxLengths(table_data):
    for x in range(len(table_data)):
        word_lengths = []

        for y in range(len(table_data[x])):
            word_lengths.append(len(table_data[x][y]))
        
        max_lengths.append(max(word_lengths))
    print("Max Lengths:\n%s\n" % max_lengths)
    return max_lengths

# create dictionary of word length differences
def createDictionary(max_lengths):
    for word_list in table_data:
        for word in word_list:
            length_diff[word] = max_lengths[table_data.index(word_list)] - len(word)          
    print("Length Differences:\n%s\n" % length_diff)
    return length_diff

# print final output
def printData(table_data):
    # rearrange data
    rearranged_data = []
    for i in range(len(table_data[0])):
        rearranged_data.append([x[i] for x in table_data])
    
    print("Rearranged Data:\n%s\n" % rearranged_data)

    # print rearranged data with spaces
    print("FINAL OUTPUT:")
    for i in range(len(rearranged_data)):
        for word in rearranged_data[i]:
            print("%s%s  " % (length_diff[word] * " ", word), end="")
        print()

# put it all together
def rearrangeData(table_data):
    getMaxLengths(table_data)
    createDictionary(max_lengths)
    printData(table_data)

# run it
rearrangeData(table_data)