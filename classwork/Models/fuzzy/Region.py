from collections.abc import Collection
from Zone import Zone


class Region(Collection):

    def __init__(self, beg:float, end:float, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__begin, self.__end = sorted([beg, end])
        self.__contents = []

    def __len__(self):
        return len(self.__contents)

    def __iter__(self):
        yield from self.__contents

    def __contains__(self, item: Zone) -> bool:
        for z in self.__contents:
            if item in z:
                return True
        return False

    def append(self, item: Zone):
        ???????

    def __inv__(self):
        ???????

    def __call__(self, x: float) -> bool:
        ??????

    def __add__(self, other):
        ??????

