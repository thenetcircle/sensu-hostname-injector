#!/usr/bin/python

import sys
import json
import socket


def main():
    data = json.load(sys.stdin)

    if "entity" not in data:
        print(data)
        return

    if "system" not in data["entity"]:
        data["entity"]["system"] = dict()

    if "hostname" not in data["entity"]["system"]:
        data["entity"]["system"]["hostname"] = socket.gethostname()

    print(data)


if __name__ == '__main__':
    main()
