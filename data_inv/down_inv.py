#!/usr/bin/env python
"""
Python script to download selected files from gdex.ucar.edu.
After you save the file, don't forget to make it executable
i.e. - "chmod 755 <name_of_script>"
"""
import sys, os
from urllib.request import build_opener

opener = build_opener()

filelist = [
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_026_cl.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_027_cvl.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_028_cvh.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_029_tvl.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_030_tvh.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_043_slt.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_074_sdfor.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_129_z.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_160_sdor.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_161_isor.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_162_anor.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_163_slor.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.128_172_lsm.ll025sc.1979010100_1979010100.nc',
  'https://osdf-director.osg-htc.org/ncar/gdex/d633000/e5.oper.invariant/197901/e5.oper.invariant.228_007_dl.ll025sc.1979010100_1979010100.nc'
]

for file in filelist:
    ofile = os.path.basename(file)
    sys.stdout.write("downloading " + ofile + " ... ")
    sys.stdout.flush()
    infile = opener.open(file)
    outfile = open(ofile, "wb")
    outfile.write(infile.read())
    outfile.close()
    sys.stdout.write("done\n")

