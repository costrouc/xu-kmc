Installation
============

Conda
-----

Eventually conda images will be built for application.

Docker Images
-------------

Eventually docker images will be build for application.

Nixpkgs
-------

`costrouc <https://github.com/costrouc/>`_ is a contributor to
`nixpkgs <https://github.com/NixOS/nixpkgs>`_ which is a novel way to
package applications and libraries. He will work to ensure that this
package is easily installable via ``nix``.

 - building :: ``nix-build .nix/default.nix``
 - virtualenv with package :: ``nix-shell .nix/shell.nix``
