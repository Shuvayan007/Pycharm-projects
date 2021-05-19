import numpy as np

class KMeans:

    def __init__(self,n_clusters):
        self.k=n_clusters
        self.centroid=[]

    def fit_predict(selfself,X):
        #1. Select k centroids randomly
        self.centroids=X[np.random.randint(X.shape[0],size=self.k),:]
        assignment=None

        self.classify(X)

        while True:
            new_assignment=np.array(self.classify(X))
            print(new_assignment.shape)
            #
            # if assignment ==new_assignment:
            #     return assignment
            #
            # #Reassign centroid
            # self.reassign_centroids()
            #assignment=new_assignment
            # Calculate new mean

        #4. For each  cluster calculate the mean
        #5. Move the centroids to the new location

    def classify(self,X):
        for i in X:
            #Calculate distance from each centroid
            for j in self.centroids:
                distances.append(self.calculate_euclidean_distance(i,j))
            assignment.append(sorted(list(enumerate(distances)),key=lambda x:x[1])[0][0])
        return assignment
    # 2. Calculate distance of each training point from every centroid
    # 3. Based on distance decide the centroids for each training point

    def reassign_centroids(self,X,assignments):
        for i in zip()

    def calculate_euclidean_distance(selfself,a,b):
        return np.sqrt(np.dot(b-a,b-a))