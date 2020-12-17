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
rasters = glob.glob("../02_data/02_netcdf_multiple/*.nc")
outDir = "../02_data/03_tiff/"


# %% [markdown]
## Converting to tiff 
for i in td(range(0, len(rasters)), desc = 'Converting to tiff'):
    fileName = rasters[i].split('\\')[1].split('.')[0]  
    ds = rioxarray.open_rasterio(rasters[i])
    ds = ds.rio.write_crs('epsg:4326')
    ds['tp'].rio.to_raster(outDir + fileName + ".tif")
    

# %% [markdown]
## Time elapsed
end = time.time()
print('Time elapsed:', np.round(end-start ,2), 'secs')


# %%
