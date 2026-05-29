import cdsapi
import os

#######################################################################
# Download ERA5 from ECMWF (3d pl, sfc) and merge for MPAS-A forcing
#######################################################################

# Date (user modification)

year = "2026"
month = "05"
day = "24"
time = "00:00"

#######################################################################
#######################################################################

fname_invar = "./data_inv/era5_inv.grib"
date = year+month+day+time[0:2]

dir_3d = "./data_3d"
dir_sfc = "./data_sfc"
dir_all = "./data_all"

cmd = "mkdir -p "+dir_3d
os.system(cmd)
cmd = "mkdir -p "+dir_sfc
os.system(cmd)
cmd = "mkdir -p "+dir_all
os.system(cmd)

fname_prim = "era5.pl.all."
fname_sufix = ".grib"

fname_3d = dir_3d+"/" + "era5.3d.pl."+date+fname_sufix
fname_sfc = dir_sfc+"/" + "era5.sfc."+date+fname_sufix
fname_all = dir_all+"/" + "era5.pl.all."+date+fname_sufix
data_format = "grib"

#######################################################################
#######################################################################

# Required vars for MPAS-A input

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "geopotential",
        "relative_humidity",
        "specific_humidity",
        "temperature",
        "u_component_of_wind",
        "v_component_of_wind"
    ],
    "year": [year],
    "month": [month],
    "day": [day],
    "time": [time],
    "pressure_level": [
        "1", "2", "3",
        "5", "7", "10",
        "20", "30", "50",
        "70", "100", "125",
        "150", "175", "200",
        "225", "250", "300",
        "350", "400", "450",
        "500", "550", "600",
        "650", "700", "750",
        "775", "800", "825",
        "850", "875", "900",
        "925", "950", "975",
        "1000"
    ],
    "data_format": data_format,
    "download_format": "unarchived"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download(fname_3d)

#######################################################################
#######################################################################

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "2m_dewpoint_temperature",
        "2m_temperature",
        "mean_sea_level_pressure",
        "sea_surface_temperature",
        "surface_pressure",
        "skin_temperature",
        "lake_cover",
        "snow_density",
        "snow_depth",
        "snow_evaporation",
        "snowfall",
        "total_column_snow_water",
        "soil_temperature_level_1",
        "soil_temperature_level_2",
        "soil_temperature_level_3",
        "soil_temperature_level_4",
        "volumetric_soil_water_layer_1",
        "volumetric_soil_water_layer_2",
        "volumetric_soil_water_layer_3",
        "volumetric_soil_water_layer_4",
        "soil_type",
        "geopotential",
        "land_sea_mask",
        "sea_ice_cover"
    ],
    "year": [year],
    "month": [month],
    "day": [day],
    "time": [time],
    "data_format": data_format,
    "download_format": "unarchived"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download(fname_sfc)

#######################################################################
# Merge 3d+sfc+inv files
#######################################################################

date = year+month+day+time[0:2]

fname_prim = "era5.pl.all."
fname_sufix = ".grib"

fname_3d = dir_3d+"/" + "era5.3d.pl."+date+fname_sufix
fname_sfc = dir_sfc+"/" + "era5.sfc."+date+fname_sufix
fname_all = dir_all+"/" + "era5.pl.all."+date+fname_sufix
data_format = "grib"

#######################################################################
#######################################################################

# Set time axis for the invariants
time_format = year+"-"+month+"-"+day+","+time+":00,1day"
cmd = "cdo settaxis,"+time_format+" "+fname_invar+" era5_inv_temp.grib"
os.system(cmd)

# Merge GRIB files
cmd = "cdo merge "+fname_3d+" "+fname_sfc+" "+"era5_inv_temp.grib "+fname_all
os.system(cmd)

# Delete the invariant file
cmd = "rm era5_inv_temp.grib"
os.system(cmd)

