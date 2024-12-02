def main():
    #get morse code
    print("Enter your morse code.\n\n1. Words are separated by 7 spaces\n" +
                  "2. Letters are separated by 3 spaces\n" +
                  "3. Parts of the same letter are separated by 1 space\n")
    print("Here's an example: ")

    print(". . . .   . .   - - . . - -       . . . .   - - -   . - -       . -   . - .   .       - . - -   - - -   . . -   . . - - . .\n")
    
    print("translates to: ")
    
    translate(". . . .   . .   - - . . - -       . . . .   - - -   . - -       . -   . - .   .       - . - -   - - -   . . -   . . - - . .")

    morse = input("\n\nMorse Code: ")
    
    translate(morse)


def translate(morse):
    
    #letters of the alphabet
    alphabet = ['. -', '- . . .', '- . - .', '- . .', '.', '. . - .', '- - .',
             '. . . .', '. .', '. - - -', '- . -', '. - . .', '- -', '- .', '- - -',
             '. - - .', '- - . -', '. - .', '. . .', '-', '. . -', '. . . -', '. - -',
             '- . . -', '- . - -', '- - . .']

    #numbers 0-9
    numbers = ['- - - - -', '. - - - -', '. . - - -', '. . . - -',
               '. . . . -', '. . . . .']

    #special characters
    special = ['- - . . - -', '. - . - . -', '. . - - . .']
    special_char = [',', '.', '?']
    
    #split into words
    words = morse.split('       ')

    #for each word
    for word in words:

        #split into characters
        segments = word.split('   ')

        #seach in each array for matching morse
        for segment in segments:

            #check if alphabetical
            try:
                index = alphabet.index(segment)
                print(chr(index + 65), end = '')
            except:

                #check if numeric
                try: 
                    index2 = numbers.index(segment)
                    print(index2, end = '')
                except:

                    #check if a special character
                    try:
                        index3 = special.index(segment)
                        print(special_char[index3], end = '')
                    except:
                        print("Not a valid char!")
                


        print(' ', end = '')


main()


