import bayes


listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)

'''
print(listOPosts)
print(listClasses)

print(myVocabList)
'''
print(bayes.setOfWords2Vec(myVocabList, listOPosts[0]))
print(bayes.setOfWords2Vec(myVocabList, listOPosts[3]))
