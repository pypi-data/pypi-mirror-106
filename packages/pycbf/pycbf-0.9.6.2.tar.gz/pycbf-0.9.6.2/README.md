# `pycbf` - CBFlib for python

This repository builds the `pycbf` portion of [CBFlib] only, as a [manylinux]
binary wheel installable through `pip install pycbf`.

In order to do this, it has some limitations compared to the full build of CBFlib:

-   No HDF5 bindings
-   No (custom) libTiff bindings
-   No CBF regex capabilities
-   No header files included - this is not intended to be used as a linking
    target

In addition to the base 0.9.6, this has the following alterations:

| Version                | Changes                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| 0.9.6.0                | Regenerated SWIG bindings for Python 3 compatibility. Compiled with `SWIG_PYTHON_STRICT_BYTE_CHAR`.        |
| ~~0.9.6.1~~            | This was an unreleased internal version.                                                                   |

[cbflib]: https://github.com/yayahjb/cbflib
[manylinux]: https://www.python.org/dev/peps/pep-0571/
[`yayahjb/cbflib#19`]: https://github.com/yayahjb/cbflib/pull/19
