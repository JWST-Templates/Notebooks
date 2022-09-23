# Notebooks
Notebooks released by the JWST ERS TEMPLATES team, to download, reduce, and analyze JWST data.

Let's break down how to get started on JWST data into simple steps.  We'll use the ERS TEMPLATES program as an example, because hey, that's our program (program ID 01355).  Feel free to grab these tools and use them for your own purposes.   

## Step 0) You probably should install the JWST pipeline.  
Our simple notebook [0_install_pipeline.ipynb](https://github.com/JWST-Templates/Notebooks/blob/main/0_install_pipeline.ipynb) shows you how.

## Step 1) Get some sweet sweet JWST data.  
You can do this from the MAST portal, but many find it hard to use.  TEMPLATES recommends a simple command-line script [JWST_API_Fetch_inBulk_templates.py](https://github.com/JWST-Templates/Notebooks/blob/main/JWST_API_Fetch_inBulk_templates.py)  

Run the script from the command line as:
>python JWST_API_Fetch_inBulk_templates.py 01355 nircam RATE

or, run it from within python as: 

>run JWST_API_Fetch_inBulk_templates.py 01355 nirspec UNCAL

There are three simple arguments:
- The program ID or PID.  Each JWST program has a PID.  For TEMPLATES it's 01355.
- The science instrument for which you want data.  Lower-case, choices are nircam, miri, niriss, nirspec.
- The [kind of data](https://jwst-pipeline.readthedocs.io/en/latest/jwst/data_products/product_types.html) you want.  While there are many ways to search, our experience is that 90% of the time, we just want all of one type of data product ("get me all the raw data").   

Common kinds of files are:
- UNCAL (Level 1b uncalibrated or "raw" data)
- RATE (Level 2a imaging data in units of DN/s)
- CAL (Level 2b calibrated imaging data in units of MJy/sr)
- I2D (same as CAL, but resampled)

## Step 2) (Coming soon) Run the pipeline on the raw data to apply the latest reference files.

