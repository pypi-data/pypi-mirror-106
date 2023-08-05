import numpy as np
from scipy.stats import norm

# Calculation of RWA accoring to article 154 from CRR2.
# https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/100916


class RiskWeightCalculation:
    def __init__(self, pd, lgd, ead):
        self.pd = pd
        self.lgd = lgd
        self.ead = ead

    def expected_loss_as_percentage(self):
        """Represents the Expected Loss (EL) as a percentile value."""
        expected_loss = self.pd * self.lgd
        return expected_loss

    def asset_correlation_rho(self):
        """Calculates the Asset Correlation (rho)"""
        rho = 0.03 * ((1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0)) + 0.16 * (1 - (1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0))))
        return rho

    def capital_requirement(self):
        """Calculates the Capital Requirement(Unexpected Loss) `k`."""
        expected_loss = self.pd * self.lgd
        rho = 0.03 * ((1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0)) + 0.16 * (1 - (1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0))))
        probability_density = norm.cdf(norm.ppf(self.pd) + rho ** 0.5 * norm.ppf(0.999) / (1.0 - rho) ** 0.5)
        conditional_expected_loss = (self.lgd * probability_density)
        k = (conditional_expected_loss - expected_loss)
        return k

    def risk_weighted_exposure_amount(self):
        expected_loss = self.pd * self.lgd
        rho = 0.03 * ((1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0)) + 0.16 * (1 - (1 - np.exp(-35.0 * self.pd) / 1 - np.exp(-35.0))))
        probability_density = norm.cdf(norm.ppf(self.pd) + rho ** 0.5 * norm.ppf(0.999) / (1.0 - rho) ** 0.5)
        conditional_expected_loss = (self.lgd * probability_density)
        k = (conditional_expected_loss - expected_loss)
        rwa = k * 12.5 * 1.06 * self.ead
        return round(rwa)

