==========
osxmpdkeys
==========

Control mpd with the OS X media keys.

Installation
------------

To install osxmpdkeys with pip, use:

.. code:: bash

    $ pip install pyobjc-core
    $ pip install osxmpdkeys

The extra install command is due to an issue_ in pyobjc.
It will work without it, but will be quite a bit slower.

.. _issue: https://bitbucket.org/ronaldoussoren/pyobjc/issue/21

Usage
-----

In the simplest case, just run ``mpdkeys``. The default address is ``localhost:6600``.

.. code::

    usage: mpdkeys [-h] [--host HOST] [--port PORT]

    optional arguments:
    --host HOST  mpd host address
    --port PORT  mpd host port
