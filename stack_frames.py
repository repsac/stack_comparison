import numpy
from scipy import stats
from PIL import Image

x = numpy.array(Image.open('images/frames/frame1.png'))
y = numpy.array(Image.open('images/frames/frame2.png'))

#maximum
stacked = numpy.uint8(numpy.amax([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/maximum/np.maximum.png', format='PNG')

#mean
stacked = numpy.uint8(numpy.mean([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/mean/np.mean.png', format='PNG')

#median
stacked = numpy.uint8(numpy.median([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/median/np.median.png', format='PNG')

#minimum
stacked = numpy.uint8(numpy.amin([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.minimum.png', format='PNG')

#range
stacked = numpy.uint8(numpy.ptp([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/range/np.range.png', format='PNG')

#standard deviation
stacked = numpy.uint8(numpy.std([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/standard-deviation/np.standard-deviation.png', format='PNG')

#summation
stacked = numpy.uint8(numpy.sum([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/summation/np.summation.png', format='PNG')

#variance
stacked = numpy.uint8(numpy.var([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/variance/np.variance.png', format='PNG')

#skewness
stacked = numpy.uint8(stats.skew([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/skewness/sp.skewness.png', format='PNG')

#kurtosis
stacked = numpy.uint8(stats.kurtosis([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/kurtosis/sp.kurtosis.png', format='PNG')