This README describes the file for COMP90049 2018S2, Project 1. 

The code of project 1 has only one file called project1.py and to run it using command python project1.py. 

The program implements 6 approximate string matching methods and evaluate them to generate precision, recall.

The dataset files that support it to generate results are： dict.txt, wiki_misspell.txt and wiki-correct.txt. After running the program, it will generate six new files contains predicted words for each method. The precision and recall are shown in the terminal.

Wikipedia contributors (n.d.) Wikipedia:Lists of common misspellings. In Wikipedia: The
Free Encyclopedia, https://en.wikipedia.org/w/index.php?title=Wikipedia: Lists_of_common_misspellings&oldid=813410985

The program imports three packages from Internet:

- editdistance: source: https://github.com/aflc/editdistance

- nltk: source: http://nltk.org 

- jellyfish: source: https://github.com/jamesturk/jellyfish