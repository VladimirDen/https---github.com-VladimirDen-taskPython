class Resume:
    def __init__(self, name, age, fav_prog_lang, сolloquial_lang):
        self.name = name
        self.age = age
        self.year = 2021 - age
        self.fav_prog_lang = fav_prog_lang
        self.сolloquial_lang = сolloquial_lang

    def __str__(self):
        return 

I = Resume(Vladimir, 36, Python, Russia)
