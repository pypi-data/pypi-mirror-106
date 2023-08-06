import os
import pdal
import numpy
import sys
import json
import subprocess

def convertLazToEPTLaz(lazFile, directoryTo, untwinePath):
    if not os.path.exists(lazFile):
        return lazFile + " does not exist."
    if not os.path.exists(untwinePath):
        return untwinePath + " does not exist."

    os.system(str(untwinePath) + ' --files=' + str(lazFile) + ' --output_dir=' + str(directoryTo) + '/' + os.path.splitext(os.path.basename(lazFile))[0])
    return str(untwinePath) + ' --files=' + str(lazFile) + ' --output_dir=' + str(directoryTo) + '/' + os.path.splitext(os.path.basename(lazFile))[0]

def convertToLaz(file, directoryTo):
    if os.path.exists(file):
        get = {
            "pipeline": [
            {
                "type" : "readers.las",
                "filename" : file
            },
            {
                "type" : "writers.las", 
                "compression":"laszip",
                "filename" : directoryTo + "/" + os.path.basename(file)
            }
        ]
        }
        pipeline = pdal.Pipeline(json.dumps(get))
        count = pipeline.execute()
        metadata = pipeline.metadata
        return metadata
    return file + " does not exist."

def convertFromLaz(lazFile, directoryTo, type):
    if os.path.exists(lazFile):
        get = {
            "pipeline": [
            {
                "type" : "readers.las",
                "filename" : lazFile
            },
            {
                "type" : "writers.las", 
                "compression":"laszip",
                "filename" : directoryTo + "/" + os.path.basename(lazFile)
            }
        ]
        }
        pipeline = pdal.Pipeline(json.dumps(get))
        count = pipeline.execute()
        metadata = pipeline.metadata
        return metadata
    return lazFile + " does not exist."

def convertLAZTo2D(lazFile, directoryTo):
    if os.path.exists(lazFile):
        get = {
            "pipeline": [
             lazFile,
            {
                "filename":directoryTo + "/" + os.path.splitext(os.path.basename(lazFile))[0] + ".tif",
                "gdaldriver":"GTiff",
                "output_type":"all",
                "resolution":"1",
                "type": "writers.gdal"
            }
            ]
        }
        pipeline = pdal.Pipeline(json.dumps(get))
        count = pipeline.execute()
        metadata = pipeline.metadata
        return metadata
    return lazFile + " does not exist."
