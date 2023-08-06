from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Tracks and analyzes the performance of stock(s)'
LONG_DESCRIPTION = 'Tracks and analyzes the performance of stock(s)'
# Setting up
setup(
    name="stock-wizard",
    version=VERSION,
    author="Hailu Teju",
    author_email="hailuteju@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(where='stock_tracker_app'),
    install_requires=['pandas', 'plotly', 'matplotlib', 'tqdm'],
    keywords=['python', 'stock', 'stock tracker', 'bollinger bands']
)
