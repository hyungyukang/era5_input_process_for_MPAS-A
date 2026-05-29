### Download ERA5 from ECMWF (3d pl, sfc) and merge for MPAS-A forcing

#### Requirements:
- CDSAPI setup: https://cds.climate.copernicus.eu/how-to-api
- CDO (Cliate Data Operators)
  - If the CDO module is available: `module load cdo`
  - Install using conda: `conda install -c conda-forge cdo`

#### How to use:
- `git clone https://github.com/hyungyukang/era5_input_process_for_MPAS-A.git`
- `cd era5_input_process_for_MPAS-A`
- Set a case date in `era5_cdsapi_down_all.py`
- `python era5_cdsapi_down_all.py`
- The final GRIB data for MPAS-A will be saved in `data_all`.
