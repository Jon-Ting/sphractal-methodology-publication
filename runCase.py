from os import getcwd, listdir
from os.path import isdir
import sys
from time import time

# from natsort import natsorted
from sphractal.boxCnt import runBoxCnt


testCaseName, voxelSurf, exactSurf = 'benchmark', True, False
radType, trimLen, alphaMult, calcBL, minSample, confLvl = 'atomic', True, 2.0, False, 5, 95
vis, figType, saveFig, showPlot, writeBox, rmInSurf, verbose = True, 'paper', True, False, True, False, True
gridNum, numSpherePoint, findSurfAlg, genPCD = 1024, 10000, 'alphaShape', False
minLenMult, maxLenMult, bufferDist, numBoxLen, numCPUs = 0.25/20, 1/1.69, 5.0, 20, int(sys.argv[1])
numRepeat = 1

PROJECT_DIR = getcwd()
FASTBC = f"{PROJECT_DIR}/sphractal/src/fastbc/3DbinImBCcpu.exe"
OUTPUT_DIR = f"{PROJECT_DIR}/outputs{sys.argv[2]}"


if __name__ == '__main__':
    testCases = []
    for NPname in listdir(f"testCases/{testCaseName}"):
        if not isdir(f"testCases/{testCaseName}/{NPname}"): testCases.append(f"testCases/{testCaseName}/{NPname}")
        else: testCases.extend([f"testCases/{NPname}/{i}" for i in listdir(f"testCases/{NPname}")])
        # else: testCases.extend(natsorted([f"testCases/{NPname}/{i}" for i in listdir(f"testCases/{NPname}")]))

    print('Running once for JIT compilation...')
    _ = runBoxCnt('testCases/PtAu20THL12_286/PtAu20THL12S2min.0.xyz', vis=False, outDir=OUTPUT_DIR, exePath=FASTBC, gridNum=1024, numPoints=300, writeBox=False)
    print('Done!')

    # for testCase in natsorted(testCases):
    for testCase in testCases:
        # if f"Pd{sys.argv[2]}SP" not in testCase: continue  # Debugging
        if "single" not in testCase: continue  # Debugging
        totalDuration = 0
        for i in range(numRepeat):
            start = time()
            _ = runBoxCnt(testCase, radType, calcBL, findSurfAlg, alphaMult, 
                          OUTPUT_DIR, trimLen, minSample, confLvl,
                          rmInSurf, vis, figType, saveFig, showPlot, verbose,
                          voxelSurf, numSpherePoint, gridNum, FASTBC, genPCD, 
                          exactSurf, minLenMult, maxLenMult, numCPUs, numBoxLen, bufferDist, writeBox)
            # Recommend maxLenMult = 2 for 'full'
            end = time()
            duration = end - start
            totalDuration += duration
            print(f"  Run {i}: {duration:.4f} s")
        # avgDuration = totalDuration / numRepeat
        # print(f"  Avg Duration:\t{avgDuration:.4f} s")