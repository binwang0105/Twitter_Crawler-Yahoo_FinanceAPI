from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF
doc = sc.textFile(“target url”).map(lambda line: line.split(' '))
hashingTF = HashingTF()
hashingTF.indexOf("COMPANY NAME")
tf = hashingTF.transform(doc)
idf = IDF().fit(tf)
tfidf = idf.transform(tf).collect()
print(tfidf)