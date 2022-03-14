# stack_comparison
Comparing image stacking results between:
- Adobe Photoshop
- Affinity Photo
- Python numpy & scypy

The tests were generated from stacking the following two frames<br />
<img src="images/frames/frame1.png" width="200" height="200">
<img src="images/frames/frame2.png" width="200" height="200">

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
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/maximum/ps.maximum.png" width="200" height="200"> | <img src="images/maximum/ap.maximum.png" width="200" height="200"> | <img src="images/maximum/np.maximum.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.amax([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/maximum/np.maximum.png', format='PNG')
```

All samples appear consistent.

---
## Mean
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/mean/ps.mean.png" width="200" height="200"> | <img src="images/mean/ap.mean.png" width="200" height="200"> | <img src="images/mean/np.mean.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.mean([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/mean/np.mean.png', format='PNG')
```

All samples appear consistent.

---
## Median
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/median/ps.median.png" width="200" height="200"> | <img src="images/median/ap.median.png" width="200" height="200"> | <img src="images/median/np.median.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.median([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/median/np.median.png', format='PNG')
```

I noticed that results from Affinity Photo were not inline with Photoshop or numpy. Affinity Photo had an option unique from the other two called "Midrage" which seemed to yield a result closer to median.<br />
<img src="images/ap.midrange.png" width="200" height="200">

---
## Minimum
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/minimum/ps.minimum.png" width="200" height="200"> | <img src="images/minimum/ap.minimum.png" width="200" height="200"> | <img src="images/minimum/np.minimum.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.amin([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.minimum.png', format='PNG')
```

All samples appear consistent.

---
## Range
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/range/ps.range.png" width="200" height="200"> | <img src="images/range/ap.range.png" width="200" height="200"> | <img src="images/range/np.range.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.ptp([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.range.png', format='PNG')
```

The results vary between applications.

---
## Standard Deviation
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/standard-deviation/ps.standard-deviation.png" width="200" height="200"> | <img src="images/standard-deviation/ap.standard-deviation.png" width="200" height="200"> | <img src="images/standard-deviation/np.standard-deviation.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.std([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.standard-deviation.png', format='PNG')
```

The results vary between applications.

---
## Summation
| Adobe Photoshop | Python numpy |
| :----: | :----: |
| <img src="images/summation/ps.summation.png" width="200" height="200"> | <img src="images/summation/np.summation.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.sum([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.summation.png', format='PNG')
```

Numpy appears to have produced border artifacts.

There was no "Summation" option for Affinity Photo, but there was a "Total" option which appears to yield the same results.<br />
<img src="images/summation/ap.total.png" width="200" height="200">

---
## Variance
| Adobe Photoshop | Affinity Photo | Python numpy |
| :----: | :----: | :----: |
| <img src="images/variance/ps.variance.png" width="200" height="200"> | <img src="images/variance/ap.variance.png" width="200" height="200"> | <img src="images/variance/np.variance.png" width="200" height="200"> |
```
stacked = numpy.uint8(numpy.var([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/np.variance.png', format='PNG')
```

The results vary between applications.

---
## Skewness
| Adobe Photoshop | Affinity Photo | Python scypy |
| :----: | :----: | :----: |
| <img src="images/skewness/ps.skewness.png" width="200" height="200"> | <img src="images/skewness/ap.skewness.png" width="200" height="200"> | <img src="images/skewness/sp.skewness.png" width="200" height="200"> |
```
stacked = numpy.uint8(stats.skew([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/sp.skewness.png', format='PNG')
```

The input test frames are probably not ideal for this test.

---
## Kurtosis
| Adobe Photoshop | Affinity Photo | Python scypy |
| :----: | :----: | :----: |
| <img src="images/kurtosis/ps.kurtosis.png" width="200" height="200"> | <img src="images/kurtosis/ap.kurtosis.png" width="200" height="200"> | <img src="images/kurtosis/sp.kurtosis.png" width="200" height="200"> |
```
stacked = numpy.uint8(stats.kurtosis([x, y], axis=0))
array = Image.fromarray(stacked)
array.save('images/minimum/sp.kurtosis.png', format='PNG')
```

I'm a bit confused by the results of scypy.
