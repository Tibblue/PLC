#!/usr/bin/python3
#------------------------------------------------------------------------------
import regex as re
import pandas as pd

dict = {}

def build_dict():
    for line in open('lexico_v3.2.txt', 'r'):
        a = re.split(r'[,]+', line)
        dict[a[0]] = int(a[2])
    for line in open('SentiLex-flex-PT02.txt', 'r'):
      a = re.findall(r'([^\n\.;]+),([^\n\.;]+).PoS=([A-Za-z]+);[^\n;]*;[^\n;]*;POL:N.=(-1|0|1).*',line)
      a = a[0]
      dict[a[0]] = int(a[3])

      

def polarity(text):
    value = 0
    found = 0
    text = text.lower()
    lines = re.split(r'[\p{punct}\s]+', text)
    for p in lines:
      if p in dict:
         found += 1
         value += dict.get(p,0)  
    if (found < 6):
        return("No")   
    if (value < 0):
       return ("Negativo")
    elif (value > 0):
       return ("Positivo")
    else:
       return ("Neutro") 

   #  if found:                 
   #          print("Analisadas " + str(found) + " palavras. Polaridade: " + str(value/found))
   #  else:
   #          print("Não foi possível analisar!!!")


def teste():
   dataset = pd.read_csv('Tweets_Mg.csv',encoding='utf-8')
   tweets = dataset["Text"].values
   classes = dataset["Classificacao"].values
   total = len(tweets)
   values = [ polarity(tweet) for tweet in tweets]

   tot_prec= 0
   tot_recall = 0
   tot_f1 = 0

   sentiments = ["Positivo", "Neutro", "Negativo"]
   for sentiment in sentiments:
      true_positives = 0
      false_positives = 0
      true_negatives = 0
      false_negatives = 0

      for i in range(0,len(tweets)):
         if (values[i]!="No"):
            if (classes[i]==sentiment and values[i]==sentiment):
                  true_positives+=1
            elif (classes[i]!=sentiment and values[i]!=sentiment):
                  true_negatives +=1
            elif (classes[i]!=sentiment and values[i]==sentiment):
                  false_positives +=1
            elif (classes[i]==sentiment and values[i]!=sentiment):
                  false_negatives +=1
      print("\n" + sentiment + ":")
      precision = true_positives/(true_positives+false_positives)
      recall = true_positives/(true_positives+false_negatives)
      f1_score = 2 * ((precision * recall) / (precision + recall))
      tot_prec += precision
      tot_recall += recall
      tot_f1 += f1_score
      print("Precision: {0:.3f}".format(round(precision,3)))
      print("Recall: {0:.3f}".format(round(recall,3)))
      print("F1: {0:.3f}".format(round(f1_score,3)))

   print("\nAverage:")
   print("Precision: {0:.3f}".format(round(tot_prec/3,3)))
   print("Recall: {0:.3f}".format(round(tot_recall/3,3)))
   print("F1: {0:.3f}".format(round(tot_f1/3,3)))

build_dict()
#polarity()
teste()