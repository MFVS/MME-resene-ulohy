class Exercise:
    def chapter_identifier(self):
        raise NotImplementedError(f"You must define a subchapter_number(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def __str__(self) -> str:
        raise NotImplementedError(f"You must define a __str__(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def render_body(self):
        raise NotImplementedError(f"You must define a render_body(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def enumerate(self):
        return enumerate(self.subchapters)
    def __getitem__(self, key):
        return self.subchapters[key]
    def get(self, key):
        return self.subchapters.get(key)
    def __setitem__(self, k, v):
        self.subchapters[k] = v
    def __init__(self) -> None:
        self.subchapters = {}
        print(self.chapter_identifier())
