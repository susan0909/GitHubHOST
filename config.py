#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from configparser import ConfigParser, SectionProxy


def GetConfig(parser, section=None):
    """Get configuration values as dictionary"""

    if not section or not len(section):
        section = 'DEFAULT'

    if section != 'DEFAULT' and section not in parser.sections():
        return None

    if isinstance(parser[section], SectionProxy):
        data = {}
        for key in parser[section].keys():
            data[key] = parser[section].get(key)
        return data
    return None


class Config:

    def __init__(self, cfg, encoding="utf-8"):
        """Application configuration file"""

        self.parser = ConfigParser()
        self.parser.read(cfg, encoding=encoding)

    def get(self, key, section=None, default=None):
        data = GetConfig(self.parser, section)
        if not isinstance(data, dict):
            return None

        return data.get(key, default)
