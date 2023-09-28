class SomeModel:
    def predict(self, message: str) -> float:
        pass


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_threshold: float = 0.3,
        good_threshold: float = 0.8,
) -> str:
    prediction = model.predict(message)

    if prediction < bad_threshold:
        return "неуд"
    elif prediction > good_threshold:
        return "отл"
    return "норм"
