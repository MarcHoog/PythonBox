from exceptions import UniqueTagsError


class CookingItem:

    def __init__(self, name, _id=None, description='', tags=None, recommendations=None):
        if tags is None:
            tags = []
        if recommendations is None:
            recommendations = []
        self.id = _id
        self.name: str = name
        self.description: str = description
        self.tags: list[dict] = tags
        self.recomendations: list = recommendations

    def __post_init__(self):
        # Removes _id if None so mongodb later creates its own that will be used as a unique identifier
        if self.id is None:
            delattr(self, 'id')

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags):
        for x in tags:
            if tags.count(x) > 1:
                raise UniqueTagsError('Tags must be unique and can only excist ones.')

        self._tags = tags

    def __iter__(self):
        for attr in ('id', 'name', 'description', 'tags', 'recomendations'):
            if getattr(self, attr) is not None:
                if attr == 'id':
                    yield '_id', str(getattr(self, attr))
                else:
                    yield attr, getattr(self, attr)

    def __repr__(self):
        return f'{self.__class__.__name__} : ( {self.name}) '

    def __eq__(self, other):
        return dict(self) == dict(other)

    async def get_tags(self, category) -> list[dict]:
        """
        returns a list of tags that match the category
        """
        return [tag for tag in self.tags if tag['type'] == category]
