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
rasters = glob.glob("../02_data/04_reprojected/*.tif")
outDir = "../02_data/05_resampled/"


# %% [markdown]
## Resampling
for i in td(range(0, len(rasters)), desc='Reprojecting'):
    fileName = rasters[i].split('\\')[1].split('.')[0]  
    outName = outDir + "{}.tif".format(fileName)  # outfile name
    gdal.Warp(
        destNameOrDestDS=outName,
        srcDSOrSrcDSTab=rasters[i], 
        xRes = 5000, 
        yRes = 5000,
    )


# %% [markdown] 
## Time elapsed
end = time.time()
print('Time elapsed:', np.round(end-start ,2), 'secs')


# %%
