import time
import osxmmkeys
import mpd
import socket
import collections


class Client(object):
    def __init__(self, host='localhost', port=6600):
        mpdc = self._mpd_client = mpd.MPDClient()
        mpdc.timeout = 3

        def perform(fn):
            try:
                fn() if self._connected else self._queue.append(fn)
            except mpd.MPDError as exc:
                print(
                    "Got an exception while executing command '%s': %s" % (
                        fn.__name__, exc
                    )
                )
            return False

        def play_pause():
            status = mpdc.status()

            if status and status['state'] == 'stop':
                mpdc.play(status.get('song', 0))
            else:
                mpdc.pause()

        self._connected = False
        self._queue = collections.deque()
        self._host = host
        self._port = port

        tap = self._tap = osxmmkeys.Tap()
        tap.on('play_pause', lambda: perform(play_pause))
        tap.on('next_track', lambda: perform(mpdc.next))
        tap.on('prev_track', lambda: perform(mpdc.previous))

    def start(self):
        self._tap.start()
        self._running = True

        self._retries = 0
        print('Connecting...')

        while self._running:
            self._connect_and_run()

    def stop(self):
        self._running = False
        self._mpd_client.close()
        self._mpd_client.disconnect()
        self._tap.stop()

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
        time.sleep(self._retries if self._retries < 30 else 30)

    def _run(self):
        while len(self._queue) > 0:
            fn = self._queue.popleft()
            try:
                fn()
            except mpd.MPDError as exc:
                print(
                    "Got an exception while executing command '%s': %s" % (
                        fn.__name__, exc
                    )
                )

        while self._running:
            self._mpd_client.status()  # Keep connection alive.
            time.sleep(1)

