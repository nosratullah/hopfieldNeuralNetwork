import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sp
import matplotlib.image as img

# import the image and extract
def imageGenerator(imageVector):
    cleanImage = np.zeros([len(imageVector)-1,len(imageVector)-1])
    for i in range(len(imageVector)-1):
        for j in range(len(imageVector)-1):
            if (imageVector[i][j] > 1):
                cleanImage[i][j] = 1
            else:
                cleanImage[i][j] = -1
    noisyImage = cleanImage + np.random.normal(0, 2, [len(image)-1,len(image)-1])

    for i in range(len(image)-1):
        for j in range(len(image)-1):
            if (noisyImage[i][j] >= 0):
                noisyImage[i][j] = 1
            else:
                noisyImage[i][j] = -1

    return cleanImage,noisyImage
# Building up the coefficient matrix
def trainer(vector,oldCoefMat):
    vector = vector.flatten()
    coefMat = np.zeros([len(vector)-1,len(vector)-1])
    if (np.isscalar(oldCoefMat)):
        for i in range(len(vector)-1):
            for j in range(len(vector)-1):
                if (i!=(i-j)):
                    coefMat[i][i-j] = vector[i]*vector[i-j]
    if (np.shape(oldCoefMat) == np.shape(coefMat)):
        for i in range(len(vector)-1):
            for j in range(len(vector)-1):
                if (i!=(i-j)):
                    coefMat[i][i-j] = vector[i]*vector[i-j]
        coefMat = coefMat + oldCoefMat

    vector = np.reshape(vector, [int(np.sqrt(len(vector))),int(np.sqrt(len(vector)))])
    return coefMat

#
def prediction(curuptedVec,coefMat):
    curuptedVec = curuptedVec.flatten()
    predictVec = np.zeros(len(curuptedVec))
    for i in range(len(curuptedVec)-1):
        temp = 0
        for j in range(len(curuptedVec)-1):
             temp += coefMat[i][j] * curuptedVec[j]
        if (temp>0):
            predictVec[i] = 1
        if (temp<0):
            predictVec[i] = -1

    predictVec = np.reshape(predictVec, [int(np.sqrt(len(predictVec))),int(np.sqrt(len(predictVec)))])
    return predictVec


#Import the images
plt.figure(figsize=(15,10))
for i in range(1,4):
    image = img.imread('dataset/pgms/{}.png'.format(i),'w').copy()
    if (i==1):
        vector,noisyVec = imageGenerator(image)
        coefMatrix = trainer(vector,0)
        predictedVec = prediction(noisyVec,coefMatrix)
    else:
        vector,noisyVec = imageGenerator(image)
        coefMatrix = trainer(vector,coefMatrix)
        predictedVec = prediction(noisyVec,coefMatrix)

    plt.subplot(i,4,1)
    plt.imshow(image)
    plt.title('Imported Picture 1')
    plt.subplot(i,4,2)
    plt.imshow(vector);
    plt.title('Cleaned and Squared Picture 1')
    plt.subplot(i,4,3)
    plt.imshow(noisyVec);
    plt.title('Noisy Picture 1')
    plt.subplot(i,4,4)
    plt.imshow(predictedVec);
    plt.title('Recalled Picture 1')

plt.savefig('hopfields.png')
plt.clf()
plt.imshow(coefMatrix)
plt.savefig('matrix.png')
plt.title('Coefficient Matrix')
plt.show()
