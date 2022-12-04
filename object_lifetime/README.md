This directory contains an example of how to get Python to interact nicely with
a C++ library that requires an initialization and finalization call before it
is used (as do MPI and Kokkos, for example).

It uses a context manager to control the initialization and finalization, and
to ensure that one can only interact with the library after it has been
initialized.

