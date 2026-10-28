import os
import numpy as np
import pandas as pd

def generate_experimental_data(output_path: str = "data/experimental_spectra.csv", seed: int = 42) -> None:
    """
    Generates a realistic, slightly messy synthetic dataset for the AI workshop.
    Contains a Gaussian signal peak, a decaying background baseline, random noise,
    and a few data anomalies (NaNs and text strings) to test data cleaning.
    """
    np.random.seed(seed)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 1. Generate core independent variable (Wavelength in nm)
    n_points = 300
    wavelengths = np.linspace(400.0, 700.0, n_points)
    
    # 2. Generate decaying baseline background (e.g., source lamp decay)
    baseline = 50.0 * np.exp(-wavelengths / 550.0)
    
    # 3. Generate a true physical signal (Gaussian peak at 580 nm)
    true_peak_center = 580.0
    true_amplitude = 25.0
    true_sigma = 15.0
    signal = true_amplitude * np.exp(-((wavelengths - true_peak_center) ** 2) / (2 * true_sigma ** 2))
    
    # 4. Add random experimental Gaussian noise
    noise_amplitude = 1.2
    noise = np.random.normal(0, noise_amplitude, n_points)
    
    # 5. Combine to get measured intensity
    intensities = baseline + signal + noise
    
    # 6. Build the background noise reference column
    background_noise = np.random.normal(0.8, 0.1, n_points)
    
    # Create the DataFrame
    df = pd.DataFrame({
        "timestamp": pd.date_range(start="2026-10-28 10:00:00", periods=n_points, freq="s"),
        "wavelength": np.round(wavelengths, 2),
        "intensity": np.round(intensities, 4),
        "background_noise": np.round(background_noise, 4)
    })
    
    # --- Inject Intentional Postdoc Pipeline Hurdles ---
    # Hurdle A: A couple of missing/NaN values that load_and_clean_data must handle
    df.loc[45, "intensity"] = np.nan
    df.loc[180, "intensity"] = np.nan
    
    # Hurdle B: A corrupted string entry in a numeric column to break naive parsers.
    # pandas 3 refuses to put a string into a float64 column, so widen to object first.
    df["intensity"] = df["intensity"].astype(object)
    df.loc[120, "intensity"] = "CORRUPTED_SIGNAL"
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"Successfully generated realistic raw dataset at: {output_path}")

if __name__ == "__main__":
    generate_experimental_data()

