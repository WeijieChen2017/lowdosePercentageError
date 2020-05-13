import numpy as np
import glob

caseList = glob.glob("../seg/*.nii.gz")
caseList.sort()
for caseName in caseList:
	print(caseName[13:15])
