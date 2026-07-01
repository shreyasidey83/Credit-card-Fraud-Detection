"""
Download the script for the Credit Card Fraud dataset.

The raw CSV (~150MB) exceeds GitHub's 25MB web-upload limit,
so it isn't committed to this repo. Run this script instead
to fetch it locally before running Fraud_Detection.ipynb.
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

print("Path to dataset files:", path)
