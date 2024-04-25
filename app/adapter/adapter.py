from domain.models.chat import Chat
from domain.models.message import Message
from domain.models.ticket import Ticket
from domain.models.user import User


class ModelAdapter:
    def __init__(self, data: tuple, model: Chat | Message | User | Ticket) -> None:
        self.data = data
        self.model = model

    def to_model(self):
        data_dict = {}
        if isinstance(self.data[0], tuple):
            self.data = self.data[0]

        fields = list(vars(self.model)["model_fields"].keys())
        for index, field in enumerate(fields):
            data_dict.setdefault(field, self.data[index])

        return self.model(**data_dict)
