import time
import osxmmkeys
from mpd import MPDClient


class Client(object):
    def __init__(self, host='localhost', port=6600):
        self._mpd_client = MPDClient()
        self._mpd_client.timeout = 10

        self._host = host
        self._port = port

        tap = self._tap = osxmmkeys.Tap()
        tap.on('play_pause', self._play_pause)
        tap.on('next_track', self._next_track)
        tap.on('prev_track', self._prev_track)

    def start(self):
        self._mpd_client.connect(self._host, self._port)
        self._tap.start()

        while True:
            self._mpd_client.status()  # Keep connection alive.
            time.sleep(1)

    def stop(self):
        self._mpd_client.close()
        self._mpd_client.disconnect()
        self._tap.stop()

    def _play_pause(self):
        self._mpd_client.pause()
        return False

    def _next_track(self):
        self._mpd_client.next()
        return False

    def _prev_track(self):
        self._mpd_client.previous()
        return False

