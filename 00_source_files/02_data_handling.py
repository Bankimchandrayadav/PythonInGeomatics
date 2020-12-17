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
## Read files 
ds = xr.open_dataset("../02_data/01_netcdf/hourly_2000.nc")


# %% [markdown]
## Convert to netcdf
outDir = "../02_data/02_netcdf_multiple/"
for i in td(range(0, 1000), 'Extracting multiple files'):
    fileName = str(ds.time[i].values)[:13]  # extract slice's time as a string
    ds1 = ds.isel(time=i)  # subset dataset to the time slice
    ds1.to_netcdf(outDir + "./" + fileName + ".nc")  # write a slice 


# %% [markdown]
## Time elapsed
end = time.time()
print('Time elapsed:', np.round(end-start ,2), 'secs')


# %%
