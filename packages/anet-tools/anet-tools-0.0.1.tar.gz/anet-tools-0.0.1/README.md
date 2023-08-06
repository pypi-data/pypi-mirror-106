# anet-tools

## Install

```
conda create -n anet python=3.7 -y
source activate anet
conda install pytorch==1.4.0 torchvision cudatoolkit=10.1 -c pytorch -y
conda install -c conda-forge opencv -y
cd anet_tools/features/flownet2/networks/correlation_package
rm -rf *_cuda.egg-info build dist __pycache__
python setup.py install --user
cd ../resample2d_package
rm -rf *_cuda.egg-info build dist __pycache__
python setup.py install --user
cd ../channelnorm_package
rm -rf *_cuda.egg-info build dist __pycache__
python setup.py install --user
cd ../../../../../
pip install -e .
```
