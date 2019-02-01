.. _obs_lsst_testing:

Testing the Package
===================

Unit Tests
----------

The unit tests for this package consist of butler (Gen 2) tests for each camera, and metadata translation tests.

Butler Tests
^^^^^^^^^^^^

The butler tests use the testing infrastructure from `lsst.obs.base` and there is a test file for each camera named ``tests/test_fooCam.py``.
There are additional tests in those files that are specific to the camera mappers in this package and that improve test coverage.
For these to run some test data must be ingested into the Butler directory.
New data can be added as follow:

-  Generate a raw test data file (or files) that is as small as possible.
   The butler tests will work even if the data array is empty so long as those
   dimensions are reflected in the butler tests. To retain the correct
   dimensional information one technique is to zero out the pixel array and
   compress with gzip.  Do not use a ``.gz`` extension as we still need the
   template strings to work to be able to locate the file. This file or files
   should be added to the test butler repository in ``data/input``. Create
   ``data/input/fooCam/`` if required and then run:

   .. code-block:: bash

      ingestImages.py ./data/input/fooCam --mode=copy fooCamtest.fits

   specifying the path to the test files. This will store them in the butler
   repository.
-  To test calibrated data butler access, if data are available,
   the individual image, mask, and variance planes, can be zeroed and put into
   the repository using the appropriate ``butler.put`` call. This writes the
   files as tile compressed by default.
-  Copy one of the ``tests/test_cam.py`` files most closely related to your
   camera.  You can include tests for processed data here but if you only
   have raw files with no calibrations it may be easiest to use
   ``test_ucd.py``.  These tests should be modified to reflect your test
   data dimensions and metadata.

Metadata Translation
^^^^^^^^^^^^^^^^^^^^

The `astro_metadata_translator` header translators (currently defined in `lsst.obs.lsst.translators`) are tested in ``tests/test_translator.py``.
There is a test method per camera and the reference headers are stored as YAML files in ``tests/headers``.
YAML is used to simplify the movement of these tests into `astro_metadata_translator` at some point in the future.
A header file can be generated in this format by running:

.. code-block:: bash

   translate_header -d testfile.fits > tests/headers/testfile.yaml

The gen 2 translators are tested in ``tests/test_parsetask.py``.
Again, there is a test method per camera and the test files are read directly from the ``data/input`` test data directory (not using a butler).

CI Tests
--------

Integration tests are run from within the `ci_lsst <https://github.com/lsst-dm/ci_lsst>`_ package.
