class Exercise:
    def render_navbar(self, sidebar):
        raise NotImplementedError(f"You must define a render_navbar(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def render_body(self):
        raise NotImplementedError(f"You must define a render_body(self) for the class {self.__class__.__name__} to be able to use it in the app.")
    def __str__(self) -> str:
        raise NotImplementedError(f"You must define a __str__(self) for the class {self.__class__.__name__} to be able to use it in the app.")
