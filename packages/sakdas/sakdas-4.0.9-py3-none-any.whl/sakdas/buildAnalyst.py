import json
import uuid
import re
import pandas as pd
from datetime import datetime
from time import gmtime, strftime
import numpy as np
import tracemalloc
import os
import sys
from sys import platform
from .DataQualityMetric import *

def buildAnalyst(df, dfName, userPlatform):

    tracemalloc.start()
    path = ""
    if (platform == "win32"):
        path = os.path.abspath(pd.__file__).replace('pandas\\__init__.py','sakdas\\')
    else:
        path = os.path.abspath(pd.__file__).replace('pandas/__init__.py','sakdas/')

    with open('{}dataQualityConfig.json'.format(path)) as f:
        data = json.load(f)


    profile = {}
    sakdasVersion   = {"profile_engine" : "4.0.9"}
    profilingId     = {"profile_id" : str(uuid.uuid4())}
    dataName        = {"data_name" : dfName}
    profilingDateTime = {"profiling_datetime" : datetime.now().strftime("%Y-%m-%dT%H:%M:%S{}".format(strftime("%z", gmtime())))} 
    profile.update(sakdasVersion)
    profile.update(profilingId)
    profile.update(dataName)
    profile.update(profilingDateTime)

    for metric, func in data.items():
        func = globals()[func](df)
        new = {metric:func}
        profile.update(new)

    profiles = json.dumps(profile, indent=4)
    current, peak = tracemalloc.get_traced_memory()
    #print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    
    return profile

