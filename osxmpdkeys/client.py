import time
import osxmmkeys
import mpd
import socket
import collections


class Client(object):
    def __init__(self, host='localhost', port=6600):
        mpd_client = self._mpd_client = mpd.MPDClient()
        mpd_client.timeout = 3

        def perform(fn):
            if self._connected:
                fn()
            else:
                self._queue.append(fn)
            return False

        def play_pause():
            return perform(mpd_client.pause)

        def next_track():
            return perform(mpd_client.next)

        def prev_track():
            return perform(mpd_client.previous)

        self._connected = False
        self._queue = collections.deque()
        self._host = host
        self._port = port

        tap = self._tap = osxmmkeys.Tap()
        tap.on('play_pause', play_pause)
        tap.on('next_track', next_track)
        tap.on('prev_track', prev_track)

    def start(self):
        self._tap.start()
        self._running = True

        self._retries = 0
        print('Connecting...')

        while self._running:
            self._connect_and_run()

    def _connect_and_run(self):
        try:
            self._mpd_client.connect(self._host, self._port)
            print('Connected.')

            self._connected = True
            self._retries = 0
            self._run()
        except (mpd.ConnectionError, socket.timeout, socket.error):
            if self._connected:
                print('Disconnected...')

        try:
            self._connected = False
            self._mpd_client.disconnect()
        except mpd.ConnectionError:
            pass

        self._retries += 1
        time.sleep(self._retries if self._retries < 20 else 20)

    def _run(self):
        while len(self._queue) > 0:
            self._queue.popleft()()

        while self._running:
            self._mpd_client.status()  # Keep connection alive.
            time.sleep(1)

    def stop(self):
        self._running = False
        self._mpd_client.close()
        self._mpd_client.disconnect()
        self._tap.stop()

