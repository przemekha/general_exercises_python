class Crazy:
    def __init__(self):
        self.seal = "foczka"


class Swayze:
    def __init__(self, name="Patric", middle_name="Tom"):
        self.name = name    #pole klasy
        self.middle_name = middle_name


if __name__ == '__main__':
    c = Crazy()
    print(c)
    print(c.seal)
    c2 = Crazy()
    print(c2)
    c2.seal = "singer"
    print(c2.seal)

    s = Swayze()
    print(s.name + s.middle_name)
    s1 = Swayze(middle_name="Hendrix", name="James")
    print(s1.name + s1.middle_name)
    # s2 = Swayze("Johnny", "Mnemonic")
    s2 = Swayze("Mnemonic", "Johnny")
    print(s2.name + s2.middle_name)