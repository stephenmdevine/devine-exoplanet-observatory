import lightkurve as lk
from astropy.io import fits
from pathlib import Path

def load_lightcurve_from_kepler(target_id):
    """
    Loads a Kepler lightcurve using Lightkurve's search interface.
    Returns a LightCurve object.
    """
    search = lk.search_lightcurve(f"KIC {target_id}", mission="Kepler")
    lc = search.download().remove_nans()
    return lc

def load_lightcurve_from_tess(sector, target_id):
    """
    Loads a TESS lightcurve for a given sector and TIC ID.
    """
    search = lk. search_lightcurve(f"TIC {target_id}", mission="TESS", sector=sector)
    lc = search.download().remove_nans()
    return lc

def load_fits_file(path):
    """
    Loads a raw FITS file from NASA/ESA archives.
    Returns the HDUList object.
    """
    path = Path(path)
    return fits.open(path)