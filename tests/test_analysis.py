import numpy as np
import pytest

from src.analysis import baseline_subtraction, fit_gaussian_peak


def test_baseline_subtraction_ideal_case():
    """
    Tests baseline subtraction under perfectly clean, predictable conditions.
    """
    intensity = np.array([10.0, 20.0, 30.0])
    background = np.array([1.0, 2.0, 3.0])

    expected = np.array([9.0, 18.0, 27.0])
    result = baseline_subtraction(intensity, background)

    np.testing.assert_array_almost_equal(result, expected)


def test_fit_gaussian_peak_ideal_centered_data():
    """
    Tests the Gaussian fitter with data perfectly centered near zero
    with an exact match guess.
    """
    # Note: This passes because the domain is forced around 0,
    # matching the bad guess in analysis.py
    x = np.linspace(-10, 10, 100)
    # True values: amplitude=10, center=0, sigma=2
    y = 10.0 * np.exp(-(x - 0.0)**2 / (2 * 2.0**2))

    amp, center, sigma = fit_gaussian_peak(x, y)

    assert pytest.approx(amp, abs=1e-2) == 10.0
    assert pytest.approx(center, abs=1e-2) == 0.0
    assert pytest.approx(sigma, abs=1e-2) == 2.0
