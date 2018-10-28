import numpy as np

scores = np.array([[80,85],
	[82,81],[67,90],[65,76],[88,96]],dtype='float64')
print(scores)
print(scores>80)
print(np.where(scores<80,0,100))

print(np.amax(scores,axis=0))#column
print(np.amin(scores,axis=1))#row
print(np.mean(scores,axis=0))#average
print(np.std(scores,axis=1))#s2

scores[:,0] /= 2
print(scores)
A = np.array([[2,0,4],[3,4,2]])
print(scores@A)
print(np.dot(scores,A))

B = A.T
print(B)
print(np.vstack((scores,B)))
print(np.hstack((scores,np.eye(5))))