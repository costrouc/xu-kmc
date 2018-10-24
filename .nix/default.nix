{ pkgs ? import <nixpkgs> { }, pythonPackages ? pkgs.python3Packages }:

pythonPackages.buildPythonPackage rec {
  pname = "kmc";
  version = "0.0.1";

  src = ../.;

  buildInputs = with pythonPackages; [ pytestrunner ];
  checkInputs = with pythonPackages; [ pytest pytestcov pytest-flake8 sphinx sphinx_rtd_theme ];
  propagatedBuildInputs = with pythonPackages; [ numpy ];

  checkPhase = ''
    ${pythonPackages.python.interpreter} setup.py test

    cd doc
    make apidocs
    make html
    mkdir -p $out/share/kmc/html
    cp -r _build/html/* $out/share/kmc/html
  '';
}
