'''theorcy
reate vectors
apple-->[0.1,0.3,..]
cars-->[0.1,0.3,..]
banana-->[0.1,0.3,..]
Truck-->[0.1,0.3,..]

if 2 vectors are similar then it will show the similarity between them
sim(apple,cars)<sim(apple,banana)
'''

from numpy import dot
from numpy.linalg import norm
import nltk
from nltk.corpus import reuters

from nltk import word_tokenize
from nltk.corpus import stopwords

