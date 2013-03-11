import os
import sys

thisdir = os.path.dirname(__file__)
srcdir = os.path.join(thisdir, '../src')
libdir = os.path.join(thisdir, '../lib/modules')
bindir = os.path.join(thisdir, '../bin')

if libdir not in sys.path:
    sys.path.insert(0, srcdir)
    sys.path.insert(0, libdir)
    sys.path.insert(0, bindir)



