
#  nothing much just some class initiallisation
class Tree():
    def __init__(self,letter = None):
        self.letter = letter
        self.children = {}
        self.leaf = False
# here i have added a word one letter at a time in the tree 
#  it honestly feels like a tri though as in c++
    def add(self,word):
        if(len(word)) :
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Tree(letter)
            return self.children[letter].add(word)
        else :
            leaf = True
            return self
    # now finding the word
    def search(self,letter):
        if letter not in self.children:
            return None
        return self.children[letter]

#function for word solver

def findword(board, tree ,validated , row , col , path = None,currletter = None,word= None):
    letter = board[row][col]
    if path is None or currletter is None or word is None:
        currletter = tree.search(letter)
        path = [(row,col)]
        word = letter
    else:
        currletter = currletter.search(letter)
        path.append((row,col))
        word = word + letter
    
    #base case
    if currletter is None:
        return
    if currletter.leaf:
        validated.add(word)
    # bfs call
    for r in range(row-1,row+1):
        for c in range(col-1,col+1):
            if(r>=0 and r<=3 and c>=0 and c < 4 and r != row and c!= col and (r,c) not in path):
                findword(board,tree,validated,r,c,path[:],currletter,word[:])


def main():
    # game board initiallisation
    board = []
    print('Enter now')
    for i in range(0,4):
        # adding empty row
        board.append([])
        for j in range(0,4):
            board[i].append(input().strip().upper())
  # printing board
    for i in range(0,4):
        for j in range(0,4):
            print(board[i][j],end = " ")
        print()
       
        # a general dictionary with 2.6k wor
        # ds used in competitions
    di = open('dictionary-yawl.txt',"r")
    tree = Tree()
    for line in di:
        word = line.rstrip().upper()
        tree.add(word)
    # set to store strings that match valid strings found in that Dictionary doc.
    validated = set()

    # callinf findword function from each grid
    for row in range(0,4):
        for col in range(0,4):
            findword(board,tree,validated,row,col)

    # print out to see it worked or not
    for word in sorted(validated):
        if(len(word)>2):
            print(word)
    print('Done!')
    
main()