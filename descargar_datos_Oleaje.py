#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "area": "14/275/11/283",
    "class": "ei",
    "dataset": "interim",
    "date": "1979-01-01/to/2017-12-31",
    "expver": "1",
    "format": "netcdf",
    "grid": "0.125/0.125",
    "levtype": "sfc",
    "param": "229.140/230.140/232.140",
    "step": "0",
    "stream": "wave",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "target": "DataEraInterim_Wavesdaily.nc",
})
