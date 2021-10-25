Analyzer returns the following information about input text:
	Sentences -> split text into senteces using Natural Language Toolkit (suite of libraries and programs in Python for Natural Language Processing Tasks)
	Words -> split sentences into single list of words and leaving only alphanumeric characters in each word
	Number of characters -> number of characters in text except spaces
	Number of words -> number of words in text
	Number of sentences -> number of senteces in text
	Frequency of characters -> Counting fequency of each character using Counter library 
	Distribution of characters as a percentage of total -> calculating destribution of each character as a percentage of total
	Average word length -> calculating average word length using Statistics library
	The average number of words in a sentence -> calculating average number of words in each sentence
	Top 10 most used words -> getting top 10 most used words using Counter
	Top 10 longest words -> using sorted() function
	Top 10 shortest words -> using sorted() function
	Top 10 longest sentences -> using sorted() function
	Top 10 shortest sentences -> using sorted() function
	Number of palindrome words -> number of palindrome (e.g. abba)
	Top 10 longest palindrome words -> using sorted() function
	Is the whole text a palindrome? (Without whitespaces and punctuation marks.) -> True if whole text is a palindrome
	The reversed text -> “This is the text.” -> ”.txet desrever ehT”
	The reversed text but the character order in words kept intact. -> “This is the text.” -> ”text. the is This”
	The time it took to process the text in ms
	Date and time when the report was generated.
	calculation works for UTF8 encoded text as well.