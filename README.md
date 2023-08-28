# Sphractal Methodology Publication 

This is a repository containing the extra written code and data generated for the work on Sphractal. 

## Features Under Development
- Optional input argument of surface atoms (to guarantee accurate box counts).
- Transformation of xyz coordinates when atoms are read in to avoid using minXYZ repetitively in `scanAtom()`.
- Integration of C++ code for point cloud surface representation into the package. Planning to use [pybind11](https://pybind11.readthedocs.io/en/latest/classes.html).

## Notes on Choices  
- Choices of parameters for findNN() and alphaShape():
    - radius:
        - should be able to find all 1st NN, but not 2nd NN
        - default: NN_RAD_MULT 1.0, recommend 120% ATOMIC_RAD, probably no need to remove inner points
        - If users want smaller radius, we provide capability of remove inner points, but NN_RAD_MULT needs to be tuned to get the right 1 NNs
        - e.g. for 100% ATOMIC_RAD, recommend NN_RAD_MULT 1.2; for METALLIC_RAD, recommend NN_RAD_MULT 1.5
    - alpha: should be able to find surface atoms accurately
        - large enough to avoid inner surface (pores within), small enough to find concave atoms
        - default: 2 * 100% ATOMIC_RAD == 5/3 * 120% ATOMIC_RAD ~= METALLIC_RAD * 2.5

