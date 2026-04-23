import gc
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import pandas as pd
import lightkurve as lk
from lightkurve import search_lightcurve


def plotLightCurve(df, kic, with_error=True):
    """
    Plot the light curve for a given KIC from a DataFrame.
    """
    row = df[df["KIC"] == kic]
    
    if row.empty:
        raise ValueError(f"KIC {kic} not found in DataFrame.")
    
    row = row.iloc[0]
    
    t = row["time"]
    f = row["flux"]
    e = row.get("flux_err", None)

    # Plot
    plt.figure(figsize=(20, 5))
    
    if with_error and e is not None:
        plt.errorbar(t, f, yerr=e, fmt='-', linewidth=1)
    else:
        plt.plot(t, f, linewidth=1)
    
    plt.xlabel("Time")
    plt.ylabel(r"Normalized Flux (e$^{-}$ s$^{-1}$)")
    plt.title(f"KIC {kic} Light Curve")
    plt.show()


def plotLightCurveFromFITS(fits_file_path):
    """
    Plots the light curve from a FITS file.
    
    Parameters:
        fits_file_path (str): The path to the FITS file.
        
    Returns:
        None
    
    Example usage:
        fits_file_path = "../assets/data/test-variable-lc.fits"
        plotLightCurveFromFITS(fits_file_path)
    """
    # Read the FITS file
    with fits.open(fits_file_path) as hdul:
        # Extract data from the FITS file
        data = hdul[1].data
        
        # Extract time, flux, and flux error data
        time = data["TIME"]
        flux = data["DETFLUX"]       # or data["APTFLUX"]
        flux_err = data["DETFLUX_ERR"]  # or data["APTFLUX_ERR"]
        
        # Create a mask to filter out invalid data points
        mask = np.isfinite(time) & np.isfinite(flux)
        if flux_err is not None:
            mask &= np.isfinite(flux_err)
        
        # Apply the mask to filter the data
        time = time[mask]
        flux = flux[mask]
        flux_err = flux_err[mask] if flux_err is not None else None
        
        # Create a plot of the light curve
        plt.figure(figsize=(20, 5))
        plt.plot(time, flux, linewidth=0.8)
        plt.xlabel("Time")
        plt.ylabel("Flux")
        plt.title("Light Curve")
        
        if flux_err is not None:
            plt.fill_between(time, flux - flux_err, flux + flux_err, alpha=0.3)
        
        plt.show()
    
    # Free up memory
    del data, time, flux, flux_err
    gc.collect()



def sampleRandomKIC(df):
    """Samples a random KIC value from the DataFrame index."""
    return np.random.choice(df.index)