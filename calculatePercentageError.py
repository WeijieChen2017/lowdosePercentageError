import numpy as np
import glob

caseList = ["003", "005", "006", "008", "010",
            "011", "012", "013", "014", "016",
            "017", "018", "019", "022", "023",
            "024", "025", "026", "027", "028"]

def getFile(filePath):
    path = glob.glob(filePath)[0]
    print(path)

for caseName in caseList:
    fullPath = "../fulldose/mre"+caseName+"_5min.nii.gz"
    lowPath = "../lowdose/mre"+caseName+"_1min.nii.gz"
    petPath = "../PET-only/PET-ONLY_*_mre"+caseName+"*.nii.gz"
    mrPath = "../MR-only/MRI-ONLY_*_mre"+caseName+"*.nii.gz"
    mixPath = "../PET-MR/PET-MRI_*_mre"+caseName+"*.nii.gz"

    for path in [fullPath, lowPath, petPath, mrPath, mixPath]:
        getFile(path)