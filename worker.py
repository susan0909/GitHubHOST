#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from PyQt5.QtCore import QThread, pyqtSignal

from host import HostDNS


class CleanerThread(QThread):

    signal = pyqtSignal(bool)

    def __init__(self):
        super(CleanerThread, self).__init__()

    def run(self) -> None:

        time.sleep(3)
        self.signal.emit(True)


class WorkerThread(QThread):

    signal = pyqtSignal(tuple)

    def __init__(self, domains: list):
        super(WorkerThread, self).__init__()
        self.domains = domains

    def run(self) -> None:

        host = HostDNS()
        total = len(self.domains)
        counter = 0
        for domain in self.domains:
            counter += 1
            time.sleep(1)
            self.signal.emit(('begin', domain, None, 0, False))
            ip, secs = host.getDomainIp(domain)
            # time.sleep(1)
            # ip = '127.0.0.1'
            # secs = 388
            self.signal.emit(('end', domain, ip, secs, counter == total))
