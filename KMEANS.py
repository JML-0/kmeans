import math
import random

max_i = 10000 #Max itérations

def k_means(k, means):
    i               = 0
    n               = len(means[0])
    cluster         = means * [0]
    prev_cluster    = means * [-1]
    random_cluster  = []

    for i in range(0, k):
        new_cluster = []
        random_cluster += [random.choice(means)] #randomint(0,10)

    while (cluster != prev_cluster) or (i > max_i):
        prev_cluster = list(cluster)
        i += 1

        for p in range (0, len(means)):
            m_d = float("inf") #valeur sup illimitée -> comp
            for c in range(0, len(0, len(random_cluster))):
                d = distance_eucli(means[p], random_cluster[c])
                if (d < m_d): #distance minimale
                    m_d = d
                    cluster[p] = c

        for k in range(0, len(random_cluster)): #MàJ clus
            new_random = [0] * n
            mbs = 0
            for p in range(0, len(means)):
                if (cluster[p] == k):
                    for j in range(0, n):
                        new_random[j] += means[p][j]
                    mbs += 1 #acc
            
            for s in range(0, n):
                if (mbs):
                    new_random[s] /= float(mbs) #cast x -> x.x
    
    print "Clusters = ", random_cluster
    print "Cluster  = ", cluster
    print "i        = ", i

def distance_eucli(a, b):
    r = 0.0
    for i in range(0, len(a)):
        r += (a[i] - b[i]) ** 2 #^2
    return math.sqrt(r)

#test
test_points = [(1,0),(1,1),(5,6),(7,7),(11,13),(12,12),(12,13),(13,13),(9,10),(3,2),(2,2),(1,2),(0,1)]
k_means(3, test_points)