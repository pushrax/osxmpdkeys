==========
osxmpdkeys
==========

Control mpd with the OS X media keys.

Installation
------------

To install osxmpdkeys with pip, use:

.. code:: bash

    $ pip install osxmpdkeys

Usage
-----

In the simplest case, just run ``mpdkeys``. The default mpd host address is ``localhost:6600``.

.. code::

    usage: mpdkeys [-h] [--host HOST] [--port PORT]

    optional arguments:
    --host HOST  mpd host address
    --port PORT  mpd host port

If you want to have mpdkeys start automatically upon login,
you can create a LaunchAgent like so:

.. code::

  $ cat <<EOF> ~/Library/LaunchAgents/com.github.pushrax.osxmpdkeys.plist

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

Next time you log in, launchd will pick up the configuration automatically.
