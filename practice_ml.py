 
 # 1. define important attribute (k, max_iter)
 # 2. define distance (arrA, arrB, )
 # 3. define random initiation (data_x, k)
 # 4. 


 class KMeansClassifier(object):
 	def __int__(self,k = 3, initCent = 'random', max_iter = 500):
 		self._k = k 
 		self._initCent = initCent
 		self._max_iter = max_iter
 		self._clusterAssment = None
 		self._labels = None
 		self._sse = None

 	def _calEDist(self, arrA,  arrB):
 		return np.math.sqrt(sum(np.power(arrA - arrB, 2)))

 	def _randCent(self, data_X, k):
 		m = data_X.shape[1]
 		centroids = np.empty((k, m))
 		for j in range(m):
 			minJ = min(data_X[:,j])
 			rangeJ = float(max(data_X[:, j] - minJ))

