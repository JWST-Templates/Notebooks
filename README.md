# Notebooks
Notebooks released by the JWST ERS TEMPLATES team, to download, reduce, and analyze JWST data.

We break down getting started with JWST data into simple steps.  We'll use the ERS TEMPLATES program as an example, because hey, that's our program (program ID 01355).  Feel free to grab these tools and use them for your own purposes.   

## Step 0) You should install the JWST pipeline.  
Our simple notebook [0_install_pipeline.ipynb](https://github.com/JWST-Templates/Notebooks/blob/main/0_install_pipeline.ipynb) shows you how.

## Step 1) Get some sweet sweet JWST data.  
There are several ways to query and download JWST data.  The most obvious is the [MAST web portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html), which has a lot of options, but can be overwhelming and clunky.  There's also an API, but man is the learning curve steep. 

Instead, TEMPLATES recommends that you grab JWST data using this simple command-line script [JWST_API_Fetch_inBulk_templates.py](https://github.com/JWST-Templates/Notebooks/blob/main/JWST_API_Fetch_inBulk_templates.py).  It makes an easy thing easy.

Run the script from the command line as:
>python JWST_API_Fetch_inBulk_templates.py 01355 nircam RATE

or, run it from within python as: 

>run JWST_API_Fetch_inBulk_templates.py 01355 nirspec UNCAL

There are three simple arguments:
- The program ID or PID.  Each JWST program has a PID.  For TEMPLATES it's 01355.
- The science instrument for which you want data.  Lower-case, choices are nircam, miri, niriss, nirspec.
- The [kind of data](https://jwst-pipeline.readthedocs.io/en/latest/jwst/data_products/product_types.html) you want.  Our experience is that 90% of the time, we just want all of one type of data product ("get me all the raw data").   

Common kinds of files are:
- UNCAL (Level 1b uncalibrated or "raw" data)
- RATE (Level 2a imaging data in units of DN/s)
- CAL (Level 2b calibrated imaging data in units of MJy/sr)
- I2D (same as CAL, but resampled)

A nice feature of this script is that it won't time out, even when you query very large datasets.  The script finds all the products matching your query, and generates a little bash script that you then run to get the products. 

Here's the script in action (wht a % to mark what to type ont he command line).  We said it was easy:
```
% python JWST_API_Fetch_inBulk_templates.py 01355 nircam UNCAL
Querying for program 01355
Querying for science instrument nircam
  Found 16 matching Observations...
  Fetching product list, 8 Observations at a time.
  Number of unique files: 1755
INFO: MAST API token accepted, welcome Jane Rigby [astroquery.mast.auth]
Downloading URL https://mast.stsci.edu/api/v0.1/Download/bundle.sh to ./mastDownload_20220923105400.sh ... [Done]
% chmod u+x mastDownload_20220923105400.sh 
% ./mastDownload_20220923105400.sh 
<<< Downloading File: mast:JWST/product/jw01355024001_07101_00002_nrcb1_uncal.fits
                  To: MAST_2022-09-23T1054/JWST/jw01355024001_07101_00002_nrcb1/jw01355024001_07101_00002_nrcb1_uncal.fits
############      (and so on.... all the files will download with a little status bar)
```




## Step 2) (Coming soon) Run the pipeline on the raw data to apply the latest reference files.

