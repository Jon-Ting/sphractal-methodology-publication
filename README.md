# Sphractal Methodology Publication 

This is a repository containing the extra details on experiments 

## Features Under Development
- Optional input argument of surface atoms (to guarantee accurate box counts).
- Transformation of xyz coordinates when atoms are read in to avoid using minXYZ repetitively in `scanAtom()`.-
- Integration of C++ code for point cloud surface representation into the package. Planning to use pybind11 (https://pybind11.readthedocs.io/en/latest/classes.html).
- Add validation results, complexity analysis, and scaling test results notebooks to package.

## Notes on Choices  
- Choices of parameters:
    - radius:
        - should be able to find all 1st NN, but not 2nd NN
        - default: NN_RAD_MULT 1.0, recommend 120% ATOMIC_RAD, probably no need to remove inner points
        - If users want smaller radius, we provide capability of remove inner points, but NN_RAD_MULT needs to be tuned to get the right 1 NNs
        - e.g. for 100% ATOMIC_RAD, recommend NN_RAD_MULT 1.2; for METALLIC_RAD, recommend NN_RAD_MULT 1.5
    - alpha: should be able to find surface atoms accurately
        - large enough to avoid inner surface (pores within), small enough to find concave atoms
        - default: 2 * 100% ATOMIC_RAD == 5/3 * 120% ATOMIC_RAD ~= METALLIC_RAD * 2.5
- ALPHA values that match the results from the cone algorithm of the Network Characterisation Package (NCPac) using 55 degrees as input argument:
    - > 2.0 (most), 2.2-5.1 (DHSX1T000), 2.1-2.8 (RDSXT000, CUS1T000) for perfect polyhedron NPs
    - 2.1-2.7, 2.4-2.6 (1 atom diff), 2.5 (1 atom diff) for disordered NPs
    - 2.38 (maximum 12 atoms diff) for heated NPs (RDSXTX23, THSXTX23)
    - Recommend to use metallic diameter of the smallest atom (Could potentially consider bond contraction in future)
