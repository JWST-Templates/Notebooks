from astropy.io import fits
from astropy.time import Time
from re import split

def get_coords_dayofyear_from_jwstfile(jwstfile, verbose=False):
     hdu = fits.open(jwstfile)
     return(get_coords_dayofyear_from_jwst_hdu(hdu))
    
def get_coords_dayofyear_from_jwst_hdu(hdu, verbose=False):
    # Grab RA, DEC, Day of Year from header.  Converts UTC date (in header) to DOY (what JWST Background Tool expects).
    datetime = hdu[0].header['DATE-BEG']
    dayofyear = int((split(':', Time(datetime).yday)[1]).lstrip('0'))  # cumbersome format for jwst_backgrounds
    # Gotta format day of year so it's int and doesn't have a leading zero
    RA       = hdu[0].header['TARG_RA']
    DEC      = hdu[0].header['TARG_DEC']
    if verbose: print("DEBUGGING:", dayofyear)
    return(RA, DEC, dayofyear)
