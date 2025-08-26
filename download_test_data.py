# download_test_data.py
"""
Download standard test datasets
Everyone gets the same data - no excuses
"""

def download_wikipedia(size_gb):
    """Download Wikipedia subset"""
    url = f"https://dumps.wikimedia.org/subset_{size_gb}gb.xml"
    print(f"Downloading {size_gb}GB test set...")
    # Download and convert to JSON