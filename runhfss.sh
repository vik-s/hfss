#!/bin/bash

# Clear the terminal window
clear

# Greeting
echo "Hi, $USER."
echo "Starting HFSS simulation ..."
echo " "

# Load EM module (update to latest version as needed)
module load ansysEM/17.2

# Run HFSS simulation
ansysedt -distributed -machinelist num=4 -monitor -waitforlicense -ng -batchextract ~/expsp_hfss.py -batchsolve $1

# Sends email after simulation is complete.
# echo | mail -s "HFSS Done: $1 " "$USER@psemi.com"
