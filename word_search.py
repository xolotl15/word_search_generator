# defining function to write a word from word_list in matrix
# word      : word to be writing
# i         : row where the word begins
# j         : column where the word begins
# direction : towards the word is aimed { 1: NE ; 2: E ; 3: SE ; 4: S ; 5: SW ; 6: W ; 7: NW ; 8: N }

def insert_word( word: str , i:int , j:int , direction:int , row:int , column:int , matrix:list ):
    # to avoid writing the same word in different directions, create a copy of the original matrix
    matrix_temp = [row_temp.copy() for row_temp in matrix.copy()]

    # loop for every letter of the word
    for letter in word.upper():
        
        # condition to avoid writing a word over another or to crossing boundaries of the matrix
        # raise an error to recall insert_word function and try another direction
        if ( (row > i and i >= 0) and (column > j and j >= 0) ) and (matrix_temp[i][j] == '-' or matrix_temp[i][j] == letter):
            matrix_temp[i][j] = letter
        else:
            raise(RuntimeError)

        if direction in (3,4,5):
            i += 1
        elif direction in (1,7,8):
            i -= 1
            
        if direction in (1,2,3):
            j += 1
        elif direction in (5,6,7):
            j -= 1
    return matrix_temp

# core of the program
def run():
    # importing necessary libraries and modules
    from random import randint
    from secrets import choice

    # CREATING NECESSARY ELEMENTS
    # words that are fillers for empty spaces in the 'matrix'
    abc : list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # matrix that contains word search (empty spaces are represented by '-')
    row: int = 20
    column : int = 20
    matrix : list = [['-' for j in range(0,column)] for i in range(0,row)]

    # extracting list of words from a text file and storing them in a list
    f = open('word_list.txt','r',encoding='utf-8')
    word_list = [word.replace('\n','') for word in f.readlines()]
    f.close()

    # loop for writing every word in the matrix
    for word in word_list:
        # Deciding initial position
        i = randint(0,row - 1)
        j = randint(0,column - 1)

        # setting direction as NE by default
        direction = randint(1,8)

        # loop for trying different directions
        while direction < 9:
            # calling inser_word function
            try:
                matrix = insert_word( word, i , j , direction , row , column , matrix)
                break
            except RuntimeError:
                direction += 1
            
            # condition for chosing another initial position
            if direction == 9:
                direction = 1
                i = randint(0,row - 1)
                j = randint(0,column - 1)

    # replacing all empty spaces with random words
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == '-':
                matrix[i][j] = choice(abc)

    # printing final matrix word searcher
    for i in matrix:
        print(i)


if __name__ == '__main__':
    run()