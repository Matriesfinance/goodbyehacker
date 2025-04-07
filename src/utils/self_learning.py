class SelfLearningModel:
    def __init__(self):
        self.history = []

    def update_model(self, prediction, actual):
        error = abs(prediction - actual)
        self.history.append(error)
        if len(self.history) > 10:
            avg_error = sum(self.history[-10:]) / 10
            if avg_error < 0.05:
                print("Model improving!")
            else:
                print("Model needs adjustment!")
