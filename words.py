def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase.

    for example:
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

        
        this should print "HELLO", "HEY", "YO", and "YES"
    """
    # Your code here
    for word in words:
        up_word = word.upper()
        if up_word[0] == "H" or up_word[0] == "Y":
            print(up_word)


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])