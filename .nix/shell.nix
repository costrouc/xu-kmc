{ pkgs ? import <nixpkgs> { } }:

let kmc = import ./default.nix { };
in
pkgs.mkShell {
  buildInputs = [ kmc ];
}
