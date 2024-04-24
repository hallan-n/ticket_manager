from domain.models.chat import Chat


class ChatAdapter:
    def __init__(self, data: tuple) -> None:
        self.data = data

    def to_model(self):
        if isinstance(self.data[0], tuple):
            self.data = self.data[0]
        return Chat(id=self.data[0], update_at=self.data[1])
