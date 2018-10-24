MINICONDA_URL="http://repo.continuum.io/miniconda"
CONDA_ENV_NAME=testenv

sudo apt-get update
# We do this conditionally because it saves us some downloading if the
# version is the same.
if [[ "$TRAVIS_PYTHON_VERSION" == "2.7" ]]; then
  wget $MINICONDA_URL/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh;
else
  wget $MINICONDA_URL/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
fi
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update -q conda
# Useful for debugging any issues with conda
conda info -a

# install development environment
sed -i -E 's/(python=)(.*)/\1'$TRAVIS_PYTHON_VERSION'/' ./dev-environment.yml
conda env create -n $CONDA_ENV_NAME -f dev-environment.yml
source activate $CONDA_ENV_NAME
