import random
import time

class User:
    def __init__(self, name, location=(0, 0)):
        self.name = name
        self.location = location

    def move(self):
        new_x = self.location[0] + random.randint(-1, 1)
        new_y = self.location[1] + random.randint(-1, 1)
        self.location = (new_x, new_y)

    def get_location(self):
        return self.location

class MonitoringSystem:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def monitor_movement(self):
        while True:
            for user in self.users:
                user.move()
                print(f"{user.name} moved to {user.get_location()}")
            time.sleep(1)

if __name__ == "__main__":
    user1 = User("Alice", location=(0, 0))
    user2 = User("Bob", location=(5, 5))

    monitoring_system = MonitoringSystem()
    monitoring_system.add_user(user1)
    monitoring_system.add_user(user2)

    try:
        monitoring_system.monitor_movement()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
