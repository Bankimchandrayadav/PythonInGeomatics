# %% [markdown] 
## About 
# - This notebook is a part of tutorial series prepared by B. C. Yadav, Research Scholar @ IIT Roorkee.
# - This notebook demonstrates the reprojecting satellite images to the required projection.


# %% [markdown]
## Importing libraries
import gdal
import glob
from tqdm.notebook import tqdm as td 
import rioxarray
import xarray as xr
import time
import numpy as np 
start = time.time()


# %% [markdown]
## Reading files 
rasters = glob.glob("../02_data/05_resampled/*.tif")
outDir = "../02_data/06_clipped/"


# %% [markdown]
## Resampling
for i in td(range(0, len(rasters)), desc='Reprojecting'):
    fileName = rasters[i].split('\\')[1].split('.')[0]  
    outName = outDir + "{}.tif".format(fileName)  # outfile name
    gdal.Warp(
        destNameOrDestDS=outName,
        srcDSOrSrcDSTab=rasters[i], 
        outputBounds = [159236.23230056558, 3170068.6251568096, 509236.2323005656, 3500068.6251568096]
    )


# %% [markdown] 
## Time elapsed
end = time.time()
print('Time elapsed:', np.round(end-start ,2), 'secs')


# %%