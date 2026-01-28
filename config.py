import os

# استخدام متغيرات البيئة بدلاً من ملف accs.txt
ACCOUNTS = []

def load_accounts_from_env():
    accounts = []
    accounts_str = os.environ.get("ACCOUNTS", "")
    for line in accounts_str.split(";"):
        if ":" in line:
            uid, pwd = line.split(":", 1)
            accounts.append({'id': uid.strip(), 'password': pwd.strip()})
    return accounts

ACCOUNTS = load_accounts_from_env()
