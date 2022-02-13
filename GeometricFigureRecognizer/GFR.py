from sklearn import tree

X = [[1, 1], [1, 2], [3, 1],
	 [2, 2], [5, 7], [4, 4],
	 [4, 4], [5, 9], [9, 9],
	 [101, 89], [81, 81], [967, 103],
	 [65, 43], [34, 90], [13, 90]]

Y = ['sq', 'rec', 'rec',
	 'sq', 'rec', 'sq',
	 'sq', 'rec', 'sq',
	 'rec', 'sq', 'rec',
	 'rec', 'rec', 'rec']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

pred = clf.predict([[65, 90]])
print(pred)
