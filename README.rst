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

You can create a LaunchAgent which automatically starts mpdkeys upon login:


.. code::

  $ cat <<EOF> ~/Library/LaunchAgents/com.github.pushrax.osxmpedkeys.plist

  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>com.github.pushrax.osxmpdkeys</string>
      <key>Program</key>
      <string>/usr/local/bin/mpdkeys</string>
      <key>RunAtLoad</key>
      <true/>
      <key>KeepAlive</key>
      <true/>
    </dict>
  </plist>
  EOF

