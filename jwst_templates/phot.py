# Helper functions for JWST photometry, from the TEMPLATES ERS team
# Contributors: jrigby, 2022
import pandas

def filter_properties():  # Functions using this should replace the 2 functions below, eventually.
    #filterfile = '/Users/jrrigby1/Python/jrr/jwst_filters.txt'
    testfile = __file__  # this should be the phot.py file
    filterfile = testfile.replace('phot.py', 'jwst_filters.txt')  # Klooodgy, look in module for f
    print("DEBUG2!", filterfile)
    df_filters = pandas.read_csv(filterfile, delim_whitespace=True, comment='#')
    return(df_filters)

def getwave_for_filter(*args):
    # Retrieve either a specific central wavelength for a filter, or a dict of them
    # just NIRCam and MIRI so far.  Pivot wavelengths from JDox on 3/2022
    # This should be in the header; asked helpdesk why it isn't
    filter_wave = {'F070W': 0.704, 'F090W': 0.902, 'F115W': 1.154, 'F150W': 1.501, 'F150W2': 1.659, \
               'F200W': 1.989, 'F212N': 2.121, 'F250M': 2.503, 'F277W': 2.762, 'F300M': 2.989, \
               'F322W2': 3.232, 'F356W': 3.568, 'F410M': 4.082, 'F430M': 4.281,  'F444W': 4.408, 'F480M': 4.874, \
               'F560W': 5.6, 'F770W': 7.7, 'F1000W': 10.0, 'F1130W': 11.3, 'F1280W': 12.8, 'F1500W': 15.0, \
               'F1800W': 18.0, 'F2100W': 21.0, 'F2550W': 25.5 }
    if len(args)==0 : return(filter_wave)
    elif len(args)==1 and args[0] in filter_wave.keys() :
        return(filter_wave[args[0]])

def getwidth_for_filter(*args):
    # Retrieve either a specific central wavelength for a filter, or a dict of them
    # just MIRI so far.  Pivot wavelengths from JDox on 3/2022
    # This should be in the header; asked helpdesk why it isn't
    df_filters = filter_properties()
    filter_width = df_filters.set_index('filtname')['width'].to_dict() 
    if len(args)==0 : return(filter_width)
    elif len(args)==1 and args[0] in filter_width.keys() :
        return(filter_width[args[0]]) 
    
def pixscale(*args):
    # Retrieve the pixel scale in arcseconds, for a given detector. Have not added NIRSpec yet
    pixscale = {'nrc_sw': 0.031, 'nrc_lw': 0.063, 'niriss': 0.0656, 'fgs': 0.0656, 'miri_imager':0.11} #from JDox
    if len(args)==0 : return(pixscale)
    elif len(args)==1 and args[0] in pixscale.keys() :
        return(pixscale[args[0]])
    else : raise Exception("ERROR: number of arguments must be 0 or 1.")
        
def cal_to_Jy(fnu_in, detector):  # no longer assuming a default, that's not safe
    # helper function to convert summed flux density in MJy/SR *Npixels to Jy.
    # This allows user to sum SB in the _CAL images and easily get a flux density in Jy
    megajy_sr_to_Jy_sqarcsec = 2.35044E-5   #1 MJy/sr = 2.35044E-5 Jy/arcsec^2
    area_1pix = pixscale(detector)**2
    fnu_Jy = fnu_in *  megajy_sr_to_Jy_sqarcsec * area_1pix
    return(fnu_Jy)
