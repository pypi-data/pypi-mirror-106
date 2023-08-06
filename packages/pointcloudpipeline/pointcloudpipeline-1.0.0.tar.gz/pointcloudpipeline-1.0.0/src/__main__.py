import sys
import click
import os
from .pipeline_worker import convertToLaz, convertFromLaz, convertLazToEPTLaz, convertLAZTo2D

@click.group()
@click.version_option("1.0.0")
def main():
    """A Piontcloudmanagement Tool"""
    pass

@main.command()
@click.option('--file', required=True, help='File to convert to LAZ')
@click.option('--directoryTo', default=os.getcwd(), help='Directory to save LAZ')
def converttolaz(file, directoryto):
    """Convert a pointcloud to LAZ and save it."""
    pointcloudMetadata = convertToLaz(file, directoryto)
    print(pointcloudMetadata)
    return pointcloudMetadata

@main.command()
@click.option('--lazFile', required=True, help='LAZ-file to convert')
@click.option('--directoryTo', default=os.getcwd(), help='Directory to save converted file')
@click.option('--typeOut', default="laz", help='Desired filetype')
def convertfromlaz(lazfile, directoryto, typeout):
    """Convert a LAZ-pointcloud to desired type."""
    pointcloudMetadata = convertFromLaz(lazfile, directoryto, typeout)
    print(pointcloudMetadata)
    return pointcloudMetadata

@main.command()
@click.option('--lazFile', required=True, help='LazFile to convert')
@click.option('--directoryTo', default=os.getcwd(), help='Directory to save')
@click.option('--untwinePath', default=os.getcwd(), help='Path to untwine')
def convertlaztoeptlaz(lazfile, directoryto, untwinepath):
    """Convert a pointcloud from LAZ to EPT-LAZ."""
    convertedLaz = convertLazToEPTLaz(lazfile, directoryto, untwinepath)
    print(convertedLaz)
    return convertedLaz


@main.command()
@click.option('--lazFile', required=True, help='LazFile to convert')
@click.option('--directoryTo', default=os.getcwd(), help='Directory to save')
def convertlazto2d(lazfile, directoryto):
    """Convert LAZ to a top rasterview in 2D."""
    metadata2D = convertLAZTo2D(lazfile, directoryto)
    print(metadata2D)
    return metadata2D

if __name__ == '__main__':
    main()
