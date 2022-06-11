class Bank_acount:
    @property
    def password(self):
        return "password: 123"

andy = Bank_acount()
print(andy.password)

andy.password = "password: 456"
print(andy.password)