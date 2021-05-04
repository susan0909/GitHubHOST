#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from os import path


configurations = {
    "version": "1.1",
    "email": "susan_tony_li@163.com",
    "name": "GitHub HOST",
    "website": "https://github.com/susan0909/GitHubHOST",
    "issue": "https://github.com/susan0909/GitHubHOST/issues",
    "manual": "https://github.com/susan0909/GitHubHOST/blob/main/README.md",
    "assets": "resources",
    "domains": [
        "github.com",
        "api.github.com",
        "central.github.com",
        "assets-cdn.github.com",
        "avatars.githubusercontent.com",
        "raw.githubusercontent.com",
        "github.global.ssl.fastly.net"
    ]
}


def ResourcePath(resource: str):
    """
    Return resource absolute path
    :param resource:
    :return:
    """

    # Application running in a PyInstaller bundle
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Windows: C:\Users\<User>\AppData\Local\Temp\_MEIXXXXX
        # Linux: /tmp/_MEIXXXXX
        bundle_dir = sys._MEIPASS
    else:
        bundle_dir = path.dirname(path.abspath(__file__))

    return path.join(bundle_dir, resource)


def GetOS():
    """Get the OS"""

    if sys.platform.lower().startswith('darwin'):
        return 'mac'
    elif sys.platform.lower().startswith('linux'):
        return 'linux'
    elif sys.platform.lower().startswith('win'):
        return 'win'
    else:
        return 'other'


def IsWindows():
    return sys.platform.lower().startswith('win')


def HostDirectory():
    if IsWindows():
        return r'C:\Windows\System32\drivers\etc'
    return r'/etc'


class Config:

    def get(self, key, default=None):

        return configurations.get(key, default)

    def isWindows(self):

        return "win" == GetOS()

    def hostDirectory(self):

        return HostDirectory()
