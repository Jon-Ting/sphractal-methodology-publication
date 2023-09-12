# Sphractal Methodology Publication 

This is a repository containing the extra written code and data generated for the work on Sphractal. 

## Features Under Development
- Optional input argument of surface atoms (to guarantee accurate box counts).
- Transformation of xyz coordinates when atoms are read in to avoid using minXYZ repetitively in `scanAtom()`.
- Integration of C++ code for point cloud surface representation into the package. Planning to use [pybind11](https://pybind11.readthedocs.io/en/latest/classes.html).

## Notes on Choices  
- Choices of parameters for findNN() and alphaShape():
    - radMult:
        - Recommend 1.2 for atomic radii, 1.5 for metallic radii
        - Adjust bulkCN as required. e.g. To find the right surface planes on {100} surfaces, radMult needs to be large enough to identify {100} packed atoms as neighbours of each other, and bulkCN needs to be higher -- 14.
    - radType:
        - If radius used is large enough, no inner surface will be resulted.
    - alpha: should be able to find surface atoms accurately
        - large enough to avoid inner surface (pores within), small enough to find concave atoms
        - default: 2 * 100% ATOMIC_RAD == 5/3 * 120% ATOMIC_RAD ~= METALLIC_RAD * 2.5
        - Recommend to use the diameter of the smallest atom (could potentially consider bond contraction in future)

