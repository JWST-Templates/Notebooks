# This is a script by Dick Shaw shaw@stci.edu   2022-Aug-08, modified by Jane.Rigby@nasa.gov,
# to grab a bunch of JWST data out of the archive, for a specific program ID, science instrument,
# and data type.  This script will work even if there are a lot of data products, which can
# otherwise cause timeouts.  This script generates a bash script of curl commands to download the data,
# which can be run on the command line.
#
# Call this script from within ipython as:   run JWST_API_Fetch_inBulk_templates.py 01355 nircam UNCAL
# or call it from the command line as:       python JWST_API_Fetch_inBulk_templates.py 01355 nircam RATE

# Before using, you'll need to install astroquery:  "pip install --pre astroquery"   or "conda install -c astropy astroquery"

# The results are returned in an astropy Table, so import some table methods
import argparse
from astroquery.mast import Observations
from astropy.table import unique, vstack, Table

def fetch_files(PID, INSTRUMENT, KINDOFDATA='UNCAL', obsmode='all', token=False, sz_chunk=8):
    '''Perform a search for all matching observations in the specified JWST 
    program. Specifying the mission as 'JWST' will optimize the search.
    '''
    print('Querying for program {}'.format(PID))
    print('Querying for science instrument ' + INSTRUMENT)

    # If someone wants to specify e.g. NIRSpec IFU vs. NIRSpec MOS, they can do it as 
    # 'obsmode', and in that case, only the entries of that type will be downloaded. 
    # If the user doesn't care, we don't force them to think about this.
    if obsmode != 'all':
        print(f'Querying for instrument mode {obsmode}')
        obsmode = f"/{obsmode}"
    else:
        obsmode = "*"
    # print(f"{INSTRUMENT}{obsmode}")
    matched_obs = Observations.query_criteria(
        obs_collection = 'JWST', instrument_name = f"{INSTRUMENT}{obsmode}", proposal_id = PID)

    print('  Found {} matching Observations...'.format(len(matched_obs)))

    if len(matched_obs) > 0:
        # Here's the key part: if the number of products that are associated 
        # with all the observations is large, the query may timeout. Instead, 
        # search for products for small subsets of observations, storing the 
        # result in a list of tables. This step may take awhile (half an hour?). 
        print('  Fetching product list, {} Observations at a time.'.format(sz_chunk))
        chunks = [matched_obs[i:i+sz_chunk] for i in range(0,len(matched_obs), sz_chunk)]
        t = [Observations.get_product_list(obs) for obs in chunks]

        # Stack the tables to get a complete list of products, but take the 
        # unique set to eliminate redundancy. For instance, guide-star files 
        # may be common to many or most of the observations. 
        files = unique(vstack(t), keys='productFilename')
        print('  Number of unique files: {}'.format(len(files)))

        # If the observations are not public, you will need a valid Auth.MAST 
        # token for retrieval (see: https://auth.mast.stsci.edu/info). Specify 
        # the token as an argument to the login() method, or put it in the 
        # environment variable $MAST_API_TOKEN. OTOH, if all the matching products 
        # are public you may skip this step.
        if token : Observations.login(token)

        # Download a bash script which has cURL commands to fetch the products. 
        # Note the option to download only 'SCIENCE' files (excluding, e.g., 
        # guide-star files). Yet another alternative (commented out) is to a 
        # specify product type, such as UNCALibrated (L-1b) products.
        manifest = Observations.download_products(
               files
               #,productGroupDescription=['Minimum Recommended Products']
               ,productType=['SCIENCE','INFO']
               ,productSubGroupDescription=KINDOFDATA
               #,extension='fits'
               ,curl_flag=True
               )

    # Run the script from the command-line, in bash, like this: 
    #     bash mastDownload_20220808145528.sh


if __name__ == '__main__':
    '''
    Generate report of DADS JWST holdings from the command-line.
    '''
    descr_text = 'Fetch a script for downloading data products from a JWST Program'
    parser = argparse.ArgumentParser(description=descr_text)
    parser.add_argument('progID', type=str,
                        help='JWST Program ID')
    parser.add_argument('instrument', type=str,
                        help='science instrument name')
    parser.add_argument('kindofdata', type=str,
                        help='kind of data (examples: RATE, CAL, UNCAL, I2D)')
    parser.add_argument('-o', '--obsmode', type=str, default="all",
                        help='instrument mode (examples: IMAGE, MOS, IFU, SLIT)')
    parser.add_argument('-t', '--token', type=str, default="",
                        help='If data are not public, you should supply a MAST token.')
    parser.add_argument('-c', '--chunk_size', type=int, default=8,
                        choices=range(1,100), 
                        help='Number of Obs to process at a time')
    args = parser.parse_args()
    fetch_files(args.progID, args.instrument, args.kindofdata, args.obsmode, args.token, args.chunk_size)
