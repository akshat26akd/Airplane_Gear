class LandingGearFSM:
    def __init__(self):
        self.state = "retracted"

    def retract(self):
        if self.state == "extended":
            self.state = "retracting"
            print("Retracting landing gear...")
            # Logic for retracting the landing gear
            self.state = "retracted"
            print("Landing gear retracted.")
        else:
            print("Landing gear is already retracted.")

    def extend(self):
        if self.state == "retracted":
            self.state = "extending"
            print("Extending landing gear...")
            # Logic for extending the landing gear
            self.state = "extended"
            print("Landing gear extended.")
        else:
            print("Landing gear is already extended.")


if __name__ == "__main__":
    landing_gear = LandingGearFSM()
    landing_gear.extend()
    landing_gear.retract()
