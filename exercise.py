class Exercise:
    def chapter_identifier(self):
        raise NotImplementedError(
            f"You must define a subchapter_identifier(self) for the class {self.__class__.__name__} to be able to use it in the app."
        )

    def __str__(self) -> str:
        raise NotImplementedError(
            f"You must define a __str__(self) for the class {self.__class__.__name__} to be able to use it in the app."
        )

    def render_body(self):
        raise NotImplementedError(
            f"You must define a render_body(self) for the class {self.__class__.__name__} to be able to use it in the app."
        )

    def enumerate(self):
        return enumerate(self.subchapters)

    def __getitem__(self, k):
        assert type(self.subchapters) is dict
        assert type(k) is str, f"cannot set at index {k} because a string is expected"
        return self.subchapters[k]

    def keys(self):
        assert type(self.subchapters) is dict
        return self.subchapters.keys()

    def get(self, k):
        assert type(self.subchapters) is dict
        assert type(k) is str, f"cannot set at index {k} because a string is expected"
        return self.subchapters.get(k, None)

    def __setitem__(self, k, new_value):
        assert type(self.subchapters) is dict
        assert type(k) is str, f"cannot set at index {k} because a string is expected"
        assert type(new_value) is not str
        # if not issubclass(new_value.__class__, Exercise):
        #     raise Exception(f"cannot set value {new_value} because an Exercise subclass is expected")
        self.subchapters[k] = new_value

    def __init__(self) -> None:
        self.subchapters = {}
