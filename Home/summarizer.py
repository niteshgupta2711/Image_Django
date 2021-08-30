import nltk
import string
from heapq import nlargest
nltk.download('stopwords')
nltk.download('punkt')
def Summarize(text):

      #if text.count(". ") > 20:
    #length = int(round(text.count(". ")/10, 0))
  #else:
    #length = 1
  #text=input("enter your sentence here")
  nopuch =[char for char in text if char not in string.punctuation]
  nopuch = "".join(nopuch)

  processed_text = [word for word in nopuch.split() if word.lower() not in nltk.corpus.stopwords.words('english')]

  word_freq = {}
  for word in processed_text:
      if word not in word_freq:
          word_freq[word] = 1
      else:
          word_freq[word] = word_freq[word] + 1

  max_freq = max(word_freq.values())
  for word in word_freq.keys():
      word_freq[word] = (word_freq[word]/max_freq)

  sent_list = nltk.sent_tokenize(text)
  sent_score = {}
  for sent in sent_list:
      for word in nltk.word_tokenize(sent.lower()):
          if word in word_freq.keys():
              if sent not in sent_score.keys():
                  sent_score[sent] = word_freq[word]
              else:
                  sent_score[sent] = sent_score[sent] + word_freq[word]

  summary_sents = nlargest(4, sent_score, key=sent_score.get)
  return " ".join(summary_sents)
#print(Summarize("Machine learning involves computers discovering how they can perform tasks without being explicitly programmed to do so. It involves computers learning from data provided so that they carry out certain tasks. For simple tasks assigned to computers, it is possible to program algorithms telling the machine how to execute all steps required to solve the problem at hand; on the computer's part, no learning is needed. For more advanced tasks, it can be challenging for a human to manually create the needed algorithms. In practice, it can turn out to be more effective to help the machine develop its own algorithm, rather than having human programmers specify every needed step. The discipline of machine learning employs various approaches to teach computers to accomplish tasks where no fully satisfactory algorithm is available. In cases where vast numbers of potential answers exist, one approach is to label some of the correct answers as valid. This can then be used as training data for the computer to improve the algorithm(s) it uses to determine correct answers. For example, to train a system for the task of digital character recognition, the MNIST dataset of handwritten digits has often been used"))