import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



class KMeansClassifier():
	"this is a k-means classifier"
	def __init__(self, k = 3, initCent = 'random', max_iter = 500):
		self._k = k
		self._initCent = initCent
		self._max_iter = max_iter
		self._clusterAssment = None
		self._labels = None
		self._sse = None

	def _calEDist(self, arrA, arrB):
		return np.math.sqrt(sum(np.power(arrA - arrB, 2)))

	def _calMDist(self, arrA, arrB):
		return sum(np.abs(arrA - arrB))

	def _randCent(self, data_X, k):
		"""
		output: k*m matrix of random centroid
		"""
		m = data_X.shape[1]
		centroids = np.empty((k, m))
		for j in range(m):
			minJ = min(data_X[:,j])
			rangeJ = float(max(data_X[:, j] - minJ))
			centroids[:, j] = (minJ + rangeJ*np.random.rand(k, 1)).flatten()
		return centroids

	def loadDataset(self, infile):
		df = []
		fileIn = open(infile)  
		for line in fileIn.readlines():  
			lineArr = line.strip().split()  
			df.append([float(lineArr[0]), float(lineArr[1])])
		df = pd.DataFrame(df)
		return np.array(df).astype(np.float)

	def fit(self, data_X):
		"""
		input n*m matrix
		"""
		if not isinstance(data_X, np.ndarray) or isinstance(data_X, np.matrixlib.defmatrix.matrix):
			try:
				data_X = np.asarray(data_X)
			except:
				raise TypeError("numpy.ndarray resuired for data_X")

		n = data_X.shape[0]
		self._clusterAssment = np.zeros((n, 2))
		if self._initCent == 'random':
			self._centroids = self._randCent(data_X, self._k)

		clusterChanged = True
		for _ in range(self._max_iter):
			clusterChanged = False
			# loop over each data point
			for i in range(n):
				minDist = np.inf
				minIndex = -1
				for j in range(self._k):
					# loop over each centroid
					arrA = self._centroids[j,:]
					arrB = data_X[i,:]
					distJI = self._calEDist(arrA, arrB)
					if distJI < minDist:
						minDist = distJI
						minIndex = j
				if self._clusterAssment[i, 0] != minIndex or self._clusterAssment[i, 1] > minDist**2:
					clusterChanged = True
					self._clusterAssment[i, :] = minIndex, minDist**2
			if not clusterChanged:
				break
			for i in range(self._k):
				index_all = self._clusterAssment[:, 0]
				value = np.nonzero(index_all == i)
				ptsInClust = data_X[value[0]]
				self._centroids[i,:] = np.mean(ptsInClust, axis = 0)

		self._labels = self._clusterAssment[: , 0]
		self._sse = sum(self._clusterAssment[:, 1])

	def predict(self, X):
		if not isinstance(X, np.ndarray):
			try:
				X = np.asarray(X)
			except:
				raise TypeError("numpy.ndarray required for X")

		n = X.shape[0]
		preds = np.zeros((n,))
		for i in range(n):
			minDist = np.inf
			for j in range(self._k):
				distJI = self._calEDist(X[i,:], self._centroids[j,])
				if distJI < minDist:
					minDist = distJI
					preds[i] = j
		return preds





if __name__=="__main__":
	k = 4
	clf = KMeansClassifier(k)
	data_X = clf.loadDataset("C:/Users/zihao.zhang/Desktop/kmenastestdata.txt")
	clf.fit(data_X)
	cents = clf._centroids
	labels = clf._labels
	sse = clf._sse
	colors = ['b','g','r','k','c','m','y','#e24fff','#524C90','#845868']
	for i in range(k):
		index = np.nonzero(labels==i)[0]
		x0 = data_X[index, 0]
		x1 = data_X[index, 1]
		y_i = i
		for j in range(len(x0)):
			plt.text(x0[j], x1[j], str(y_i), color=colors[i], \
						fontdict={'weight': 'bold', 'size': 6})
		plt.scatter(cents[i,0],cents[i,1],marker='x',color=colors[i],\
					linewidths=7)
	
	plt.title("SSE={:.2f}".format(sse))
	plt.axis([-7,7,-7,7])
	outname = "./result/k_clusters" + str(k) + ".png"
	plt.show()




