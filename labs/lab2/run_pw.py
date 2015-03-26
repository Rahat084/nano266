#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/.

Author: Shyue Ping Ong
"""

import os
import shutil

# We use numpy, a numerical python package to help with some analyses. It comes
# with most modern Unix-based OSes, including Mac and Linux.
import numpy as np

# Load the Fe.pw.in.template file as a template.
with open("Si.pw.in.template") as f:
    template = f.read()

# Set the k-point grid
k = 8
ecut = 10 # In Ry
alat = 10.26 # The lattice parameter for the cell in Bohr.
psp = "Si.pbe-n-kjpaw_psl.0.1.UPF"

# Loop through a series of values of ecut. Note that ecut is stipulated in Ry
# in PWSCF. Google for the meaning of the numpy.arange function (as well as any
# other python functions that are alien to you). When writing code to automate
# anything, you frequently need to consult documentation on the web.
for ecut in np.arange(10, 50, 10):

    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(alat=alat, k=k, ecut=ecut, pseudopotential=psp)

    # Let's define an easy jobname.
    jobname = "Si_%s_%s_%s" % (ecut, k, alat)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with ecut = %f, alat = %f, k = %f..." % (ecut, alat, k))

    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x < {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done")

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
