import osxmmkeys
from mpd import MPDClient


class Client(object):
    def __init__(self, host='localhost', port=6600):
        self.client = MPDClient()
        self.client.timeout = 10
        self.host = host
        self.port = port

    def run(self):
        self.client.connect(self.host, self.port)

        tap = osxmmkeys.Tap()
        tap.on('play_pause', self.play_pause)
        tap.on('next_track', self.next_track)
        tap.on('prev_track', self.prev_track)
        tap.run()

    def stop(self):
        self.client.close()
        self.client.disconnect()

    def play_pause(self):
        self.client.pause()
        return False

    def next_track(self):
        self.client.next()
        return False

    def prev_track(self):
        self.client.previous()
        return False

