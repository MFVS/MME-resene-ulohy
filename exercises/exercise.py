class Exercise:
    def subchapter_number(self):
        raise NotImplementedError(f"You must define a subchapter_number(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def chapter_name(self):
        raise NotImplementedError(f"You must define a chapter_name(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def __str__(self) -> str:
        raise NotImplementedError(f"You must define a __str__(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def render_body(self):
        raise NotImplementedError(f"You must define a render_body(self) for the class {self.__class__.__name__} to be able to use it in the app.")
