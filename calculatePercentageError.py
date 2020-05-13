import numpy as np
import nibabel as nib
import glob

caseList = ["003", "005", "006", "008", "010",
            "011", "012", "013", "014", "016",
            "017", "018", "019", "022", "023",
            "024", "025", "026", "027", "028"]

def getSUV(filePath, segData):
    niiPath = glob.glob(filePath)[0]
    niiData = nib.load(niiPath).get_fdata()
    segValue = np.multiply(niiData, segData)
    return(np.mean(segValue))

for caseName in caseList:
    segPath = "../seg/full_"+caseName+"seg_s.nii.gz"
    segData = nib.load(segPath).get_fdata()

    fullPath = "../fulldose/mre"+caseName+"_5min.nii.gz"
    lowPath = "../lowdose/mre"+caseName+"_1min.nii.gz"
    petPath = "../PET-only/PET-ONLY_*_mre"+caseName+"*.nii.gz"
    mrPath = "../MR-only/MRI-ONLY_*_mre"+caseName+"*.nii.gz"
    mixPath = "../PET-MR/PET-MRI_*_mre"+caseName+"*.nii.gz"

    print(caseName, " ",end="")
    for path in [fullPath, lowPath, petPath, mrPath, mixPath]:
        print(getSUV(path, segData), " ", end="")
    print("")