class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        self.full_name = f"{self.first_name} {self.family_name}"
        return self.full_name


# C-1. フルネームを取得できる
ken = Customer(first_name="Ken", family_name="Tanaka")
ken_full_name = ken.full_name()
print(ken_full_name)
