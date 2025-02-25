import random
import math
import urllib, json
from pyvis.network import Network
import matplotlib.pyplot as plt

NUM_CHAR = 26
class TrieNode:
    def __init__(self, inputChar=""):
        self.childnode = [None] * NUM_CHAR
        self.word_count = 0
        self.char = inputChar
        self.end = False

def insert_word(root, word):
    ## Make current node the root
    currNode = root

    for c in word:
        if not currNode.childnode[ord(c) - ord('a')]:
            ## Node for current character does not exist, create node
            ## Point the current character's pos to the newNode
            newNode = TrieNode(c)
            currNode.childnode[ord(c) - ord('a')] = newNode
        currNode = currNode.childnode[ord(c) - ord('a')]
    
    currNode.word_count += 1
    currNode.end = True

def search_word(root, word):
    currNode = root

    for c in word:
        if not currNode.childnode[ord(c) - ord('a')]:
            return False
        currNode = currNode.childnode[ord(c) - ord('a')]

    return ((currNode.word_count > 0) and currNode.end)

def delete_word(root, word):
    currNode = root
    lastBranchNode = None
    lastBranchChar = 'a'

    for c in word:
        if not currNode.childnode[ord(c) - ord('a')]: 
           return False
        else:
            count = 0
            for i in range(NUM_CHAR):
                if currNode.childnode[i]:
                   count += 1
            if count > 1:
                lastBranchNode = currNode
                lastBranchChar = c
            currNode = currNode.childnode[ord(c) - ord('a')]
           
    count = 0
    for i in range(NUM_CHAR):
        if currNode.childnode[i]:
            count += 1

    # Case 1: deleted word is a prefix of other words in the Trie
    if count > 0:
        currNode.word_count -= 1
        currNode.end  = False
        return True
    
    # Case 2: deleted word shares a common prefix with other words in Trie.
    if lastBranchNode:
        lastBranchNode.childnode[ord(lastBranchChar) - ord('a')] = None
        return True
    
    # Case 3: deleted word does not share any common prefix with other words in Trie.
    else:
        root.childnode[ord(word[0]) - ord('a')] = None
        return True
    
def view_trie(root, htmlFile):      
      g = Network(directed = True)      
      #g.show_buttons()

      nodeIndex = 1
      currentNode = 0
      #print(type(root))
      q = [root] 
      ## Color of root is red     
      g.add_node(currentNode, label="", color="red")
      tempLabels = {0:""}
      while q:
        n = q.pop(0)             
        for node in n.childnode:
          if node:
            tempLabels[nodeIndex] = tempLabels[currentNode] + node.char
            g.add_node(nodeIndex, label = tempLabels[currentNode] + node.char, color="#48e073" if node.end else "blue")
            g.add_edge(currentNode, nodeIndex)
            nodeIndex += 1
            q.append(node)
        currentNode += 1
      g.show(htmlFile, notebook=False)

if __name__ == '__main__':
    # Make a root node for the Trie
    root = TrieNode()

    # Stores the strings that we want to insert in the Trie
    input_strings = ["and", "ant", "do", "geek", "dad", "ball", "tree", "train"]

    # number of insert operations in the Trie
    n = len(input_strings)

    for i in range(n):
        insert_word(root, input_strings[i])

    view_trie(root, 'init.html')

    # Stores the strings that we want to search in the Trie
    search_query_strings = ["do", "geek", "bat", "train", "travel"]

    # number of search operations in the Trie
    search_queries = len(search_query_strings)

    for i in range(search_queries):
        result = "Not present"
        if search_word(root, search_query_strings[i]):
            result = "present"
        
        print("Query String: %s Result: %s \n"%(search_query_strings[i], result))

    # stores the strings that we want to delete from the Trie
    delete_query_strings = ["geek", "tea", "tr"]

    # number of delete operations from the Trie
    delete_queries = len(delete_query_strings)

    for i in range(delete_queries):
        result = "Not present"
        if delete_word(root, delete_query_strings[i]):
            result = "Delete successful"

        print("Delete String: %s Result: %s \n"%(delete_query_strings[i], result))

    view_trie(root, 'final.html')
        