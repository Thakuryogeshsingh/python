from spellchecker  import spellchecker
corrector = spellchecker()

Word = input("Enter a word: ")
if Word in corrector:
    print("Correct")
else:
    correct_word =  corrector.correction(Word)
    print("Correct Spelling is ", correct_word)