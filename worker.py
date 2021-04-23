#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal

from host import HostDNS


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
            self.signal.emit(('begin', domain, None, 0, False))
            ip, secs = host.getDomainIp(domain)
            self.signal.emit(('end', domain, ip, secs, counter == total))
