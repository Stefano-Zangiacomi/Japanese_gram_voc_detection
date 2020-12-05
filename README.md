# Japanese_gram_voc_detection

The goal of this personal project is to help people to learn japanese using japanese content such as articles, animes or movies.
The idea is to extract grammar and vocabulary from each sentence to help people in their learning journey.

I used the JMDict dictionnary as the main database for vocabulary. I used a japanese tokenizer to tokenize each sentence and then search for each entry in the dictionnary or my own grammar database.  

The project is far from perfect. They are some difficulties with the tokenizer and the search within the dictionnary. For example, two words can be written the same but don't have the same meaning.  

To identfy conjugation patterns, I decided to conjugate each verb from its dictionnary form and create a csv file containing "all" conjugation.
