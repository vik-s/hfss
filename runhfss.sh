#!/bin/bash

# Clear the terminal window
clear

# Greeting
echo "Hi, $USER."
echo "Starting HFSS simulation ..."
echo " "

# Load EM module
module load ansysEM/16.0

# Run HFSS simulation
ansysedt -distributed includetypes=default maxlevels=1 -machinelist list=localhost:4:8 -monitor -waitforlicense -ng -batchsolve $1

# Automatically exports s-parameter file.
ansysedt -ng -machinelist num=1 -batchextract ~/expsp_hfss.py $1

# Sends email after simulation is complete.
echo | mail -s "HFSS Done: $1 " "$USER@psemi.com"

