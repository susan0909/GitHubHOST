#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QThread, pyqtSignal

from host import HostDNS


class WorkerThread(QThread):

    signal = pyqtSignal(tuple)

    def __init__(self, domains: dict):
        super(WorkerThread, self).__init__()
        self.domains = domains

    def run(self) -> None:

        host = HostDNS()
        for domain in self.domains.keys():
            ip = host.getDomainIp(domain)
            self.signal.emit((domain, ip))
