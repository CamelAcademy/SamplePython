class Chef:
    def make_chicken(self):
        print("Chicken is ready")
    def make_salad(self):
        print("Salad is ready")
    def make_bbq(self):
        print("BBQ is ready")

class ChineseChef(Chef):
    def make_bbq(self):
        print("Chinese BBQ is ready")
    def make_rice(self):
        print("Rice is ready")