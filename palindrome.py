#Hannah Moore  3/28/18
#CSC-131-005
#
#Test 2


def palindromeChecker(word):
    '''This functions purpose is to return True if a  provided string is a palindrome,
and False otherwise.'''
    
    list_word = []
    reversed_list = []

    for each in word:
        list_word.append(each.lower())

    reversed_list = list(list_word)
    list_word.reverse()

    if list_word == reversed_list:    

        return True

    else:
        return False

