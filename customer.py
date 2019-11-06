class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age
        self.list = [self.full_name(), str(self.age), str(self.entry_fee())]

    def full_name(self):
        self.full_name = f"{self.first_name} {self.family_name}"
        return self.full_name

    def age(self):
        return self.age

    def entry_fee(self):
        if 3 < self.age < 20:
            return 1000
        elif 20 <= self.age <= 65:
            return 1500
        elif 65 <= self.age < 75:
            return 1200
        elif 75 <= self.age:
            return 500
        elif self.age <= 3:
            return 0

    def info_csv(self):
        list_csv = ",".join(self.list)
        return list_csv

    def info_tab(self):
        list_tab = '\t'.join(self.list)
        return list_tab

    def info_pipe(self):
        list_pipe = '|'.join(self.list)
        return list_pipe

# C-1. フルネームを取得できる
# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken_full_name = ken.full_name()
# print(ken_full_name)

# C-2. 年齢という概念の追加
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken_age = ken.age  # 15 という値を返す
# print(ken_age)
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom_age = tom.age  # 57 という値を返す
# print(tom_age)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu_age = ieyasu.age  # 73 という値を返す
# print(ieyasu_age)

# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
#     料金の計算ルールこども料金(20歳未満): 1000円
#     おとな料金(20歳以上65歳未満): 1500円
#     シニア料金(65歳以上): 1200円
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# price = ken.entry_fee()  # 1000 という値を返す
# print(price)
#
# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# price = tom.entry_fee()  # 1500 という値を返す
# print(price)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# price = ieyasu.entry_fee()  # 1200 という値を返す
# print(price)

# C-4. 単一の顧客情報をCSV形式で取得できる
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken_information = ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
# print(ken_information)
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom_information = tom.info_csv()  # "Tom Ford,57,1500" という値を返す
# print(tom_information)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu_information = ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
# print(ieyasu_information)

# C-5. 3歳以下の入場料金の無料化
# children = Customer(first_name="子", family_name="共", age=1)
# children_information = children.info_csv()
# print(children_information)
#
# # C-6. 75歳以上の料金区分の追加
# old = Customer(first_name="老", family_name="人", age=100)
# old_information = old.info_csv()
# print(old_information)

# C-7. 単一顧客の情報取得形式の追加その1
# ken_tab = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken_tab_information = ken_tab.info_tab()
# print(ken_tab_information)

# tom_tab = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom_tab_information = tom_tab.info_tab()
# print(tom_tab_information)

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# tom_tab_information = ieyasu.info_tab()
# print(tom_tab_information)

# C - 8.単一顧客の情報取得形式の追加その2
ken_pipe = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken_pipe_information = ken_pipe.info_pipe()
print(ken_pipe_information)

tom_pipe = Customer(first_name="Tom", family_name="Ford", age=57)
tom_pipe_information = tom_pipe.info_pipe()
print(tom_pipe_information)

ieyasu_pipe = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyase_pipe_information = ieyasu_pipe.info_pipe()
print(ieyase_pipe_information)
