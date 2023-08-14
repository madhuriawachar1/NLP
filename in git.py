#syhdkjjgit 
import nltk
#nltk.download()


paragraph = "Differential privacy [10] is a robust, precise and mathe- matically rigorous notion of privacy, and it has emerged in a recent line of work that seeks private data analysis (See [5, 6, 29, 30, 27, 7, 3, 28, 11, 14, 9]). Differential privacy promises that very little about any specific individual can be learned in the data analysis process irrespective of the attacker’s prior knowledge, information source and other datasets. Al- gorithm A is ε-differentially private if the following holds. When A is applied on any two databases that differ only on the details of one individual, the probability distributions of the two outputs are very similar, i.e., the probability of outputs lying in any specific single fixed set differs by a mul- tiplicative factor exp(ε). In other words, the output is in- sensitive to a specific individual and depends only on the statistics of the database."

# Tokenizing sentences
sentences = nltk.sent_tokenize(paragraph)

# Tokenizing words
words = nltk.word_tokenize(paragraph)
print(sentences)
print(words)
