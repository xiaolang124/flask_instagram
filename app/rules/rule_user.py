# -*- encoding=utf-8 -*-

import re


def verify_user(user_name):
    re_user = re.compile(r'[^0-9a-zA-Z]')
    if re.findall(re_user, user_name):
        return False
    return True
