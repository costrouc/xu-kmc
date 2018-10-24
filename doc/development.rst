Development
===========

For development `conda` is recommended.

.. code-block:: shell

   conda env create -n kmc -f dev-environment.yml
   source activate kmc


From here you will have all the necissary dependencies. You can run
all the tests, coverage, and style enforcement with the following command.


.. code-block:: shell

   python setup.py test


Documentation is done with `sphinx
<http://www.sphinx-doc.org/en/stable/index.html>`_. You will need to
get comfortable with using `restructuredText
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_. To
update the ``api`` documentation you will need to run
``sphinx-apidoc`` within the ``doc`` directory.
