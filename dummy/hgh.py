def rev_sen(sen):
    
    

    words=sen.split(' ')

    reverse_sen=' '.join(reversed(words))

    return reverse_sen

if __name__== "__main__":
    
    input ='my.name.is.nishant'
    print(rev_sen(input))
