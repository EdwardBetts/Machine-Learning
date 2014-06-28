'''
Created May 27, 2014

@author Rainicy
'''

import numpy as np

from util import RMSE, initialData
from LinearBatchGD import LinearBatchGD
from LinearStochasticGD import LinearStochasticGD
from LogisticBatchGD import *
from LogisticStochasticGD import LogisticStochasticGD
from SmoothLogisticStochasticGD import SmoothLogisticStochasticGD


def main():

	# For testing
	# np.set_printoptions(threshold='nan')

	# Part 1: Prepare for the data for training and testing
	data = np.loadtxt('../../data/spambase/spambase.data', delimiter=',')
	trainX, trainY, testX, testY = initialData(data)

	# Part 2: Training the theta model by Batch Gradient Descent
	options = {'alpha': 5e-6, 'threshold': 1e-6, 'regularized': True, 'lambda': 500}
	theta = LinearBatchGD(trainX, trainY, options)
	# theta = LinearStochasticGD(trainX, trainY, options)
	# theta = LogisticBatchGD(trainX, trainY, options)
	# theta = LogisticStochasticGD(trainX, trainY, options)
	# theta = SmoothLogisticStochasticGD(trainX, trainY, options)

	# Part 3: Testing data 
	## for linear
	predictTrain = np.dot(trainX, theta)
	predictTest = np.dot(testX, theta)
	## for logistic 
	# predictTrain = logistic(np.dot(trainX, theta))
	# predictTest = logistic(np.dot(testX, theta))

	rmseTrain = RMSE(predictTrain, trainY)
	rmseTest = RMSE(predictTest, testY)

	print "RMSE for Training Data: %f" % rmseTrain
	print "RMSE for Testing Data: %f " % rmseTest

	# testing for logistic function
	# trainER = np.sum((predictTrain > .5) != trainY) / float(trainY.size)
	# testER = np.sum((predictTest > .5) != testY) / float(testY.size)
	# print "Error Rate on training: %f" % trainER
	# print "Error Rate on testing : %f" % testER

if __name__ == '__main__':
	main()