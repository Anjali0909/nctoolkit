import nctoolkit as nc
import numpy as np
import pandas as pd
import xarray as xr
import os, pytest
import re

nc.options(lazy=True)



class TestCrop:
    def test_plot(self):
        ff = "data/sst.mon.mean.nc"
        ds = nc.open_data(ff, checks = False)
        ds.subset(time = 0)
        out_file = nc.temp_file.temp_file(".html")
        ds.plot(out= out_file)
        assert os.path.exists(out_file)
        os.remove(out_file)

        ds = nc.open_data(ff, checks = False)
        ds.subset(time = [0,1,2])
        out_file = nc.temp_file.temp_file(".html")
        ds.plot(out= out_file)
        assert os.path.exists(out_file)
        os.remove(out_file)



        ds = nc.open_data(ff, checks = False)
        ds.subset(time = [0,1,2])
        ds.spatial_mean()
        out_file = nc.temp_file.temp_file(".html")
        ds.plot(out= out_file)
        assert os.path.exists(out_file)
        os.remove(out_file)

        ds = nc.open_data(ff, checks = False)
        ds.subset(time = [0,1,2])
        ds.zonal_mean()
        out_file = nc.temp_file.temp_file(".html")
        ds.plot(out= out_file)
        assert os.path.exists(out_file)
        os.remove(out_file)

        ds = nc.open_data(ff, checks = False)
        ds.subset(time = [0,1,2])
        ds.assign(tos = lambda x: x.sst + 273.15)
        ds.zonal_mean()
        out_file = nc.temp_file.temp_file(".html")
        ds.plot(out= out_file)
        assert os.path.exists(out_file)
        os.remove(out_file)

