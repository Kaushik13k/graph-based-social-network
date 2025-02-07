class Observer:
    def update(self, message: str):
        pass


class UserNotification(Observer):
    def update(self, message: str):
        print(f"🔔 Notification: {message}")


class GraphObserver:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)
