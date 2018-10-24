# Kinetic Monte Carlo (KMC)

[![Build Status](https://travis-ci.org/costrouc/xu-kmc.svg?branch=master)](https://travis-ci.org/costrouc/xu-kmc)

This is to serve as a template for starting KMC code development for
Dr. Xu's research group. Further description here.

# Documentation

[readthedocs](https://readthedocs.org/) is a great way to host
documentation. Fro now the [documentation is here](https://xu-kmc-example.readthedocs.io/en/latest/)

# Installation

## Conda 

Eventually conda images will be built for application.

## Docker Images

Eventually docker images will be build for application.

## Nixpkgs

[costrouc](https://github.com/costrouc/) is a contributor to
[nixpkgs](https://github.com/NixOS/nixpkgs) which is a novel way to
package applications and libraries. He will work to ensure that this
package is easily installable via `nix`.

 - building :: `nix-build .nix/default.nix`
 - virtualenv with package :: `nix-shell .nix/shell.nix`
 
# Development

For development `conda` is recommended.

```
conda env create -n kmc -f dev-environment.yml
source activate kmc
```

From here you will have all the necissary dependencies. You can run
all the tests, coverage, and style enforcement with the following command.

```
python setup.py test
```

Documentation is done with
[sphinx](http://www.sphinx-doc.org/en/stable/index.html). You will
need to get comfortable with using
[restructuredText](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). To
update the `api` documentation you will need to run `sphinx-apidoc` within the `doc` directory.


# License

Currently the
[Unlicense](https://choosealicense.com/licenses/unlicense/) is
used. This will allow for when the repo is transfered that there are
no issues with copyright.

# Contributions

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome!

