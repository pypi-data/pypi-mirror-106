[![Build Status](https://travis-ci.org/JeanBilheux/SectorizedRadialProfile.svg?branch=master)](https://travis-ci.org/JeanBilheux/SectorizedRadialProfile)
[![codecov](https://codecov.io/gh/JeanBilheux/SectorizedRadialProfile/branch/master/graph/badge.svg)](https://codecov.io/gh/JeanBilheux/SectorizedRadialProfile)
[![PyPI version](https://badge.fury.io/py/sectorizedradialprofile.svg)](https://badge.fury.io/py/sectorizedradialprofile)

# SectorizedRadialProfile
Calculate radial profile of a given angle

**Principle**

The goal of this library is to integrate (sum) all the pixel that are at the same distance
from the center (defined by the user) over a given sector (angular range).

![alt text](docs/_static/readme_principle.png "principle")

This will produce a profile that looks something like this

![alt text](docs/_static/readme_result.png "result")


**Example**

```
from sectorizedradialprofile.calculate_radial_profile import CalculateRadialProfile
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib notebook
```

```
data_file = 'data_2_circles.tif'
data = np.array(Image.open(data_file))
working_data = data[:,:,0]   
```

```
plt.figure(0)
plt.imshow(working_data)
```

![alt text](docs/_static/raw_data.png "workding data")

``` 
center = {'x0': 500, 'y0': 500}  #pixels
angle_range = {'from': 0, 'to': 90}  #degrees
```

```
o_profile = CalculateRadialProfile(data=working_data, center=center, angle_range=angle_range)
o_profile.calculate()
profile = o_profile.radial_profile
```

```
plt.figure(1)
plt.plot(profile)
```

![alt text](docs/_static/sector_profile.png "profile")







**How to run the tests**

to run test and see coverage of test
> pytest -v --cov

