#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


configurations = {
    "version": "1.0",
    "email": "susan_tony_li@163.com",
    "name": "GitHub HOST",
    "website": "https://github.com/susan0909/GitHubHOST",
    "issue": "https://github.com/susan0909/GitHubHOST/issues",
    "manual": "https://github.com/susan0909/GitHubHOST/blob/main/README.md",
    "assets": "resources",
    "domains": [
        "github.com",
        "api.github.com",
        "assets-cdn.github.com",
        "avatars.githubusercontent.com",
        "avatars0.githubusercontent.com",
        "camo.githubusercontent.com",
        "cloud.githubusercontent.com",
        "codeload.github.com",
        "favicons.githubusercontent.com",
        "gist.github.com",
        "gist.githubusercontent.com",
        "github.githubassets.com",
        "marketplace-screenshots.githubusercontent.com",
        "octocaptcha.com",
        "raw.githubusercontent.com",
        "repository-images.githubusercontent.com",
        "uploads.github.com",
        "user-images.githubusercontent.com",
        "github.global.ssl.fastly.net"
    ]
}


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


class Config:

    def get(self, key, default=None):

        return configurations.get(key, default)

    def isWindows(self):

        return "win" == GetOS()
