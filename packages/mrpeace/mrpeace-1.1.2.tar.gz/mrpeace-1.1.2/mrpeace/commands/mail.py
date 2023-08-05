#!/usr/bin/env python3

import smtplib


class Mail:
    def __init__(self, account, password):
        self.account = account
        self.password = password

    def send(self):
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.account, self.password)
        server.sendmail(self.account, self.account, "this message is from python")
        server.quit()
