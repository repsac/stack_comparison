# stack_comparison
Comparing image stacking results between:
- Adobe Photoshop
- Affinity Photo
- Python numpy & scypy

These tests were generated from stacking the following two frames
![](images/frames/frame1.png)
![](images/frames/frame2.png)

Python setup
```
import numpy
from scipy import stats
from PIL import Image
x = numpy.array(Image.open('images/frames/frame1.png'))
y = numpy.array(Image.open('images/frames/frame2.png'))
```
---
## Maximum
Adobe Photoshop
![](images/maximum/ps.maximum.png)
Affinity Photo
![](images/maximum/ap.maximum.png)
Python numpy
```
stacked = numpy.uint8(numpy.amax([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/maximum/np.maximum.png', format='PNG')
```
![](images/maximum/np.maximum.png)

All samples appear consistent.

---
## Mean
Adobe Photoshop
![](images/mean/ps.mean.png)
Affinity Photo
![](images/mean/ap.mean.png)
Python numpy
```
stacked = numpy.uint8(numpy.mean([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/mean/np.mean.png', format='PNG')
```
![](images/mean/np.mean.png)

All samples appear consistent.

---
## Median
Adobe Photoshop
![](images/median/ps.median.png)
Affinity Photo
![](images/median/ap.median.png)
Python numpy
```
stacked = numpy.uint8(numpy.median([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/median/np.median.png', format='PNG')
```
![](images/median/np.median.png)

I noticed that results from Affinity Photo were not inline with Photoshop or numpy. Affinity Photo had an option unique from the other two called "Midrage" which seemed to yield a result closer to median.
![](images/ap.midrange.png)

---
## Minimum
Adobe Photoshop
![](images/minimum/ps.minimum.png)
Affinity Photo
![](images/minimum/ap.minimum.png)
Python numpy
```
stacked = numpy.uint8(numpy.amin([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.minimum.png', format='PNG')
```
![](images/minimum/np.minimum.png)

All samples appear consistent.

---
## Range
Adobe Photoshop
![](images/range/ps.range.png)
Affinity Photo
![](images/range/ap.range.png)
Python numpy
```
stacked = numpy.uint8(numpy.ptp([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.range.png', format='PNG')
```
![](images/range/np.range.png)

The results for Photoshop appear to produce whiter circles.

---
## Standard Deviation
Adobe Photoshop
![](images/standard-deviation/ps.standard-deviation.png)
Affinity Photo
![](images/standard-deviation/ap.standard-deviation.png)
Python numpy
```
stacked = numpy.uint8(numpy.std([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.standard-deviation.png', format='PNG')
```
![](images/standard-deviation/np.standard-deviation.png)

The results for Photoshop appear to produce whiter circles.

---
## Summation
Adobe Photoshop
![](images/summation/ps.summation.png)
Affinity Photo did not have a "Summation" option, rather it had "Total" which appears to yield the same result.
Affinity Photo
![](images/summation/ap.total.png)
Python numpy
![](images/summation/np.summation.png)
```
stacked = numpy.uint8(numpy.sum([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.summation.png', format='PNG')
```

Numpy appears to have produced border artifacts.

---
## Variance
Adobe Photoshop
![](images/variance/ps.variance.png)
Affinity Photo
![](images/variance/ap.variance.png)
Python numpy
![](images/variance/np.variance.png)
```
stacked = numpy.uint8(numpy.var([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.variance.png', format='PNG')
```

The results for Photoshop appear to produce whiter circles.

---
## Skewness
Adobe Photoshop
![](images/skewness/ps.skewness.png)
Affinity Photo
![](images/skewness/ap.skewness.png)
Python numpy
![](images/skewness/sp.skewness.png)
```
stacked = numpy.uint8(stats.skew([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/sp.skewness.png', format='PNG')
```

The input test frames are probably not ideal for this test.

---
## Kurtosis
Adobe Photoshop
![](images/kurtosis/ps.kurtosis.png)
Affinity Photo
![](images/kurtosis/ap.kurtosis.png)
Python numpy
![](images/kurtosis/sp.kurtosis.png)
```
stacked = numpy.uint8(stats.kurtosis([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/sp.kurtosis.png', format='PNG')
```

I'm a bit confused on the results of numpy.