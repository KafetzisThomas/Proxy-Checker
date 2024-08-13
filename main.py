#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Proxy-Checker (https://github.com/KafetzisThomas/Proxy-Checker)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)
# License: GPLv3
# NOTE: By contributing to this project, you agree to the terms of the GPLv3 license, and agree to grant the project owner the right to also provide or sell this software, including your contribution, to anyone under any other license, with no compensation to you.

import os
import sys
import socket
import urllib.request
import urllib.error


def read_text_file():
    try:
        filepath = sys.argv[1]
        with open(filepath, "r") as file:
            content = file.read().splitlines()
    except IndexError:
        print("Usage: python3 main.py <filepath>")
        sys.exit()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit()
    return content


def is_bad_proxy(proxy):
    try:
        # Use the given proxy for HTTP requests
        proxy_handler = urllib.request.ProxyHandler({"http": proxy})
        opener = urllib.request.build_opener(proxy_handler)

        # Avoid blocks from servers that reject requests with no or unusual user-agent headers
        opener.addheaders = [("User-agent", "Mozilla/5.0")]
        urllib.request.install_opener(opener)

        # Attempt to open the url using the proxy
        req = urllib.request.Request("http://www.google.com")
        urllib.request.urlopen(req)
    except Exception:
        return True
    return False


def create_logs(filename, proxy):
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/{filename}", "a") as file:
        file.write(f"{proxy}\n")


def main():
    # Set a timeout to avoid hanging on slow proxies
    socket.setdefaulttimeout(120)

    proxyList = read_text_file()
    for proxy in proxyList:
        if is_bad_proxy(proxy):
            print(f"{proxy} isn't working")
            create_logs("bad_proxies.txt", proxy)
        else:
            print(f"{proxy} is working")
            create_logs("good_proxies.txt", proxy)


if __name__ == "__main__":
    main()
