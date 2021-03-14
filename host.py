#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

from bs4 import BeautifulSoup
from bs4.element import Tag
from collections import defaultdict
from ping3 import ping


class HostDNS:

    def getIpPing(self, ip):
        """Get ip ping delay ms"""

        try:
            seconds = ping(ip, timeout=10)
            return int(seconds * 1000)
        except Exception as e:
            # print(f"Ping ip:{ip} error: {e}")
            return 0

    def getBestIp(self, ips):
        """Ping ip speed"""

        if len(ips) < 1:
            return None
        elif len(ips) == 1:
            return ips[0]
        else:
            ms = 100000
            best_ip = ips[0]
            for ip in ips:
                _ms = self.getIpPing(ip)
                if _ms < ms:
                    best_ip = ip
                    ms = _ms
            return best_ip

    def parseIp(self, domain: str, html: str):
        """Parse IP from HTML"""

        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")
        dom = soup.select_one("#dnsinfo")
        data = []
        if dom and isinstance(dom, Tag):
            for tr in dom.children:
                if tr and isinstance(tr, Tag):
                    tds = tr.contents
                    if len(tds) == 3:
                        data.append((tds[0].text.lower().strip(), tds[1].text.lower().strip(), tds[2].text.lower().strip()))

        if not data:
            return None

        host_ip = defaultdict(list)
        host_names = {}
        for _name, _type, _ip in data:
            if "a" == _type:
                host_ip[_name].append(_ip)
            if "cname" == _type:
                host_names[_name] = _ip

        ips = None
        if not host_names:
            if domain in host_ip:
                ips = host_ip[domain]
            elif "@" in host_ip:
                ips = host_ip["@"]
        else:
            if domain in host_names:
                domain = host_names[domain]
                if domain in host_ip:
                    ips = host_ip[domain]
                elif "@" in host_ip:
                    ips = host_ip["@"]

        if not ips:
            return None

        best_ip = self.getBestIp(ips)
        if not best_ip:
            print(f"domain: {domain} has invalid ip: {best_ip}")
        return best_ip

    def getDomainResponse(self, domain: str):
        """Get Request Response"""

        if domain.lower().startswith('https://'):
            domain = domain.replace('https://', '')
        if domain.lower().startswith('http://'):
            domain = domain.replace('http://', '')

        if domain.find('/') > 0:
            domain = domain[0:domain.find('/')]

        api = "https://www.ipaddress.com/search/"
        payload = {"host": domain}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        }

        try:
            res = requests.post(api, data=payload, headers=headers, timeout=30)
            if res.status_code == requests.codes.ok:
                return res.text
        except Exception as e:
            # print(e)
            return None

    def getDomainIp(self, domain: str):
        """Get Domain IP address"""

        html = self.getDomainResponse(domain)
        return self.parseIp(domain, html)
