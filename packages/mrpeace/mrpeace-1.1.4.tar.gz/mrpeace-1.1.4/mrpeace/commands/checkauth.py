#!/usr/bin/env python3

import requests


class CheckAuth:
    def __init__(self, http_link) -> None:
        self.http_link = http_link
        self.request = requests.get(self.http_link)

    def json(self):
        return self.request.json()
