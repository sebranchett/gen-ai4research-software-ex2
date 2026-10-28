import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import os
import matplotlib.pyplot as plt


def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Loads experimental spectrum data from a CSV file and drops invalid rows.

    Parameters
    ----------
    filepath : str
        Path to the experimental CSV file.

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe with numeric columns.
    """
    # BUG 1: Naive parsing. It doesn't coerce errors when converting types,
    # meaning the 'CORRUPTED_SIGNAL' string string will cause a ValueError
    # if not handled, or it will leave the column as an 'object' type which
    # breaks numerical fitting downstream.
    df = pd.read_csv(filepath)

    # Intentionally naive cleanup: only drops explicit NaNs, misses string
    # corruptions
    df = df.dropna()
    return df


def baseline_subtraction(
    intensity: np.ndarray, background: np.ndarray
) -> np.ndarray:
    """
    Subtracts instrument background noise from the measured intensity signal.

    Parameters
    ----------
    intensity : np.ndarray
        Raw measured intensity array.
    background : np.ndarray
        Background noise reference array.

    Returns
    -------
    np.ndarray
        Corrected intensity spectrum.
    """
    # BUG 2: Physical Violation. Subtracting random noise fluctuations can
    # yield negative intensity values. It forgets to clip or bound negative
    # results to 0.0, causing physical impossibilities downstream.
    return intensity - background


def fit_gaussian_peak(wavelength: np.ndarray, intensity: np.ndarray) -> tuple:
    """
    Fits a single Gaussian peak profile to the spectrum data to find the
    center wavelength.
    Model: y = Amplitude * exp(-(x - Center)^2 / (2 * Sigma^2))

    Parameters
    ----------
    wavelength : np.ndarray
        Independent variable wavelength values.
    intensity : np.ndarray
        Dependent corrected intensity values.

    Returns
    -------
    tuple
        Optimized fit parameters (amplitude, center, sigma).
    """
    def gaussian(x, amplitude, center, sigma):
        return amplitude * np.exp(-((x - center) ** 2) / (2 * sigma ** 2))

    # BUG 3: Unscaled Initial Guesses. Hardcoding a center guess of 0.0 for
    # data that lives between 400nm and 700nm causes curve_fit to diverge or
    # fail entirely unless reasonable, data-driven initial guesses (p0) are
    # supplied.
    initial_guesses = [1.0, 0.0, 1.0]

    popt, _ = curve_fit(gaussian, wavelength, intensity, p0=initial_guesses)
    return float(popt[0]), float(popt[1]), float(popt[2])


def generate_publication_plot(
    wavelength: np.ndarray,
    intensity: np.ndarray,
    fit_y: np.ndarray,
    output_dir: str = "plots",
) -> str:
    """
    Generates a publication-quality visualization and saves it to disk.
    """
    # BUG 4: Missing directory creation. If the 'plots/' directory does not
    # exist, plt.savefig raises a FileNotFoundError and crashes the script
    # pipeline.
    out_path = os.path.join(output_dir, "spectrum_fit.png")

    plt.figure(figsize=(6, 4))
    plt.plot(wavelength, intensity, 'k.', label="Experimental Data")
    plt.plot(wavelength, fit_y, 'r-', linewidth=2, label="Gaussian Fit")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity (a.u.)")
    plt.legend()
    plt.tight_layout()

    plt.savefig(out_path, dpi=300)
    plt.close()
    return out_path
