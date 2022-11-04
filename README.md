# Notebooks
Notebooks released by the JWST Early Release Science (ERS) [TEMPLATES](https://sites.google.com/view/jwst-templates/) team, to download, reduce, and analyze JWST data.

We break down getting started with JWST data into simple steps.  We'll use the ERS TEMPLATES program as an example, because hey, that's our program (program ID 01355).  Feel free to grab these tools and use them for your own purposes.   

## Step 0) You should install the JWST pipeline from STScI.  
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

A nice feature of this script is that it won't time out, even when you query very large datasets.  The script finds all the products matching your query, and generates a little bash script that you then run to get the products. We added an optional --token, -t keyword to enter your MAST token, to access secret data.

Here's the script in action (wht a % to mark what to type on the command line).  We said it was easy:
```
% python JWST_API_Fetch_inBulk_templates.py 01355 nircam UNCAL
Querying for program 01355
Querying for science instrument nircam
  Found 16 matching Observations...
  Fetching product list, 8 Observations at a time.
  Number of unique files: 1755
Downloading URL https://mast.stsci.edu/api/v0.1/Download/bundle.sh to ./mastDownload_20220923105400.sh ... [Done]
% chmod u+x mastDownload_20220923105400.sh 
% ./mastDownload_20220923105400.sh 
<<< Downloading File: mast:JWST/product/jw01355024001_07101_00002_nrcb1_uncal.fits
                  To: MAST_2022-09-23T1054/JWST/jw01355024001_07101_00002_nrcb1/jw01355024001_07101_00002_nrcb1_uncal.fits
############      (and so on.... all the files will download with a little status bar)
```


## Step 2) Run the pipeline on the raw data to apply the latest calibration reference files.

While you can download calibrated data directly from MAST, what's in the archive often has calibrations that are several weeks stale.  In this period of early science operations (summer/fall 2022), where the calibrations are changing frequently, it is usually best to download the raw data, and reprocess it yourself, so that the latest calibrations are applied.

We provide simple notebooks reprocessing JWST data for each data mode in TEMPLATES.  



### &mdash; [NIRSpec IFU](https://github.com/JWST-Templates/Notebooks/blob/main/nirspec_pipeline.ipynb)

This is our example Jupter notebook for reducing the NIRSpec IFU data from TEMPLATES.  At first glance, this notebook may seem like a lot of steps, but we've set it up so that it 1) works great for TEMPLATES data, and 2) does a better job than the basic reduction would (e.g., better cosmic ray flagging, background subtraction, etc.).  Right now it's working for target SGAS1723; we'll update it to work with all 4 TEMPLATES targets.

After you've downloaded the data and placed it all where you want it, open up this notebook and start walking through the cells! 


### &mdash; (other instruments+observing modes used in TEMPLATES coming soon!)


