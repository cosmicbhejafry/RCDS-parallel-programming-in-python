To enable CUDA support, UCX requires the CUDA Runtime library (libcudart).            
The library can be installed with the appropriate command below:                      
                                           
* For CUDA 11, run:    conda install cudatoolkit cuda-version=11                      
* For CUDA 12, run:    conda install cuda-cudart cuda-version=12


\ 
To enable CUDA support, please follow UCX's instruction above.

To additionally enable NCCL support, run:    conda install nccl


| 
On Linux, Open MPI is built with CUDA awareness but it is disabled by default.
To enable it, please set the environment variable
OMPI_MCA_opal_cuda_support=true
before launching your MPI processes.
Equivalently, you can set the MCA parameter in the command line:
mpiexec --mca opal_cuda_support 1 ...
Note that you might also need to set UCX_MEMTYPE_CACHE=n for CUDA awareness via