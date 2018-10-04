print("---------- Exercise 3 script ----------")

print("Question 1:")
from netCDF4 import Dataset
import numpy as np
import time as mytime
from numpy.random import uniform
from datetime import datetime, timedelta
from netCDF4 import num2date, date2num

dataset = Dataset("data/ggas2014121200_00-18.nc", "r", format="NETCDF4_CLASSIC")
print("Dataset variables:")
for variable in dataset.variables:
    print(variable)

sst = dataset.variables["SSTK"]
print(f"sst:\n{sst}")

print("id:  length:")
for dimension in sst.dimensions:
    print(dimension, len(dataset.variables[dimension]))

print(f"sst shape: {sst.shape}, sst size: {sst.size}")

print("sst attributes:")
for attr in sst.ncattrs():
    print(f"{attr} = {getattr(sst, attr)}")

print("Question 2:")
arr = sst[1, 0, 10:20, 30:35]
print(f"arr type = {type(arr)}")
dims = list(sst.dimensions)
print(f"dims: {dims}")
vars = dataset.variables
arr_time = vars["time"][1]
arr_level = vars["surface"][0]
arr_lats = vars["latitude"][10:20]
arr_lons = vars["longitude"][30:35]

print("Values in arr slice: ")
for vals in (arr_time, arr_level, arr_lats, arr_lons):
    print(vals)

metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst, attr)
print(f"metadata:\n{metadata}")
