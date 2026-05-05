import os
import gc
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
import pandas as pd
import lightkurve as lk
from lightkurve import search_lightcurve


def plotLightCurveFromDF(df: pd.DataFrame, kic: int, with_error: bool = True):
    """
    Plots the light curve for a given KIC from a DataFrame.
    Assumes KIC is the index of the input DataFrame 'df'.
    """
    # 1. Retrieve the entire row using the index label 'kic'
    # This returns a Pandas Series object, which is what we want.
    try:
        row_series = df.loc[kic]
    except KeyError:
        raise ValueError(f"KIC {kic} not found in DataFrame index.")
    
    # Check if the retrieved row is empty (though KeyError should handle most missing cases)
    if row_series.empty:
        raise ValueError(f"KIC {kic} resulted in an empty record in the DataFrame.")

    # 2. Access data directly using string keys on the Series
    t = row_series["time"]
    f = row_series["flux"]
    e = row_series.get("flux_err", None)

    # 3. Plotting
    plt.figure(figsize=(20, 5))
    if with_error and e is not None:
        plt.errorbar(t, f, yerr=e, fmt='-', linewidth=1)
    else:
        plt.plot(t, f, linewidth=1)
        
    plt.xlabel("Time")
    plt.ylabel(r"Normalized Flux (e$^{-}$ s$^{-1}$)")
    plt.title(f"KIC {kic} Light Curve")
    plt.show()
    
    plt.close()

    
def saveLightCurveFromDF(df: pd.DataFrame, kic: int, outputDirectory = r'./'):
    """
    Plots the light curve for a given KIC from a DataFrame.
    Assumes KIC is the index of the input DataFrame 'df'.
    """
    try:
        row_series = df.loc[kic]
    except KeyError:
        raise ValueError(f"KIC {kic} not found in DataFrame index.")
    
    if row_series.empty:
        raise ValueError(f"KIC {kic} resulted in an empty record in the DataFrame.")

    t = row_series["time"]
    f = row_series["flux"]
    e = row_series.get("flux_err", None)

    plt.figure(figsize=(20, 5))
    plt.plot(t, f, linewidth=1)
    
    plt.xlabel("Time")
    plt.ylabel(r"Normalized Flux (e$^{-}$ s$^{-1}$)")
    plt.title(f"KIC {kic} Light Curve")
    
    # filename = f"light_curve_{kic}.png"
    # plt.savefig(filename)

    # --- Saving the Figure ---
    try:
        # 1. Ensure the output directory exists
        os.makedirs(outputDirectory, exist_ok=True)
        
        # 2. Construct the full file path
        filename = f"lightcurve_ID_{target_id}.png"
        save_path = os.path.join(outputDirectory, filename)
        
        # 3. Save the figure
        plt.savefig(save_path)
        print(f"\n✅ Success! Lightcurve for ID {kic} successfully saved to: {save_path}")
    
    except Exception as e:
        print(f"\n❌ Failed to save the figure to {outputDirectory}. Error: {e}")
    finally:
        # Always close the figure to free up memory
        plt.close()

    # plt.close()


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