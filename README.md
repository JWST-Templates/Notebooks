# Notebooks
Notebooks released by the JWST ERS TEMPLATES team, to download, reduce, and analyze JWST data.

Let's break down how to get started on JWST data into simple steps.  We'll use the ERS TEMPLATES program as an example, because hey, that's our program.  Feel free to grab these tools and use them for your own purposes.  

## Step 0) You probably should install the JWST pipeline.  
Our simple notebook [0_install_pipeline.ipynb](https://github.com/JWST-Templates/Notebooks/blob/main/0_install_pipeline.ipynb) shows you how.

## Step 1) Get some sweet sweet JWST data.  
You can do this from the MAST portal, but many find it hard to use, so we recommend a simple command-line script [JWST_API_Fetch_inBulk_templates.py](https://github.com/JWST-Templates/Notebooks/blob/main/JWST_API_Fetch_inBulk_templates.py)  Run it from the command line as:
>python JWST_API_Fetch_inBulk_templates.py 01355 nircam RATE

or, run it from within python as: 

>run JWST_API_Fetch_inBulk_templates.py 01355 nircam UNCAL

Common kinds of files are:
- UNCAL (Level 1b uncalibrated or "raw" data)
- RATE (Level 2a data in units of DN/s)
- CAL (Level 2b calibrated data in units of MJy/sr)
- I2D (same as CAL, but resampled I think.)

## Step 2) (Coming soon) Run the pipeline on the raw data to apply the latest reference files.

