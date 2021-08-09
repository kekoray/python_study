import re


class CheckUserInfo():
    def check_pwd_len(self, pwd):
        """密码长度不超过 8 位"""
        return len(pwd) >= 8

    def check_pwd_contain_leter(self, pwd):
        """密码包含大小写英文字母"""
        flag = False
        pattern = re.compile('[A-Z][a-z]+')
        match = pattern.findall(pwd)
        if match:
            flag = True
        return flag
