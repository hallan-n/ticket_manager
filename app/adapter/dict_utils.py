def clean_none(data: dict):
    for key, value in data.copy().items():
        if not value:
            del data[key]
    return data
