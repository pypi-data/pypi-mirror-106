from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'A simple commandline app for converting pointclouds and get 2D images out of them.'
LONG_DESCRIPTION = 'You can convert pointclouds into different formats. Example: Viewable Entwine format or 2D raster.'

setup (
    name='pointcloudpipeline',
    version=VERSION,
    author='Nadine Sennhauser and Denis Nauli',
    author_email='nadine.sennhauser@ost.ch',
    description=DESCRIPTION,
    packages = find_packages(),
    install_requires = ['click','numpy','cython','packaging','scikit-build','pdal'],
    keywords=['pointcloud','convert','pointcloudbrowser'],
    python_requires='>=3.1',
    scripts=['src/pipeline_worker.py'],
    entry_points='''
        [console_scripts]
        pointcloudpipeline=src.__main__:main
    ''',
    license='BSD-3',
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
