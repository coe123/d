# A Huffman Tree Node
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
   	 # frequency of symbol
   	 self.freq = freq

   	 # symbol name (character)
   	 self.symbol = symbol

   	 # node left of current node
   	 self.left = left

   	 # node right of current node
   	 self.right = right

   	 # tree direction (0/1)
   	 self.huff = ''

    def __lt__(self, nxt):
   	 return self.freq < nxt.freq


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):

    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if(node.left):
   	 printNodes(node.left, newVal)
    if(node.right):
   	 printNodes(node.right, newVal)

   	 # if node is edge node then
   	 # display its huffman code
    if(not node.left and not node.right):
   	 print(f"{node.symbol} -> {newVal}")


# characters for huffman tree
chars=[]
freq=[]
iString=input("Enter a sentence: ")
inputString=iString.lower()
for i in inputString:
    if(i!=" " and i not in chars):
    	chars.append(i)
print(chars)


# frequency of characters
for i in chars:
    count=0
    for j in inputString:
   	 if(i==j):
   		 count+=1
    freq.append(count)



for i in range(0,len(freq)):
    for j in range(0,len(freq)-i-1):
   	 if(freq[j]>=freq[j+1]):
   		 freq[j],freq[j+1]=freq[j+1],freq[j]
   		 chars[j],chars[j+1]=chars[j+1],chars[j]
print("The frequency is: ",freq)
print("The sorted chars array is: ",chars)    


# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:

    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

    heapq.heappush(nodes, newNode)

# Huffman Tree is ready!
printNodes(nodes[0])
