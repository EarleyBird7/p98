class Car(object):
    def __init__(self,model,speed_limit,color):
        self.color=color
        self.model=model
        self.speed_limit=speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerator(self):
        print("accelerating")

c1=Car("Prius", 45, "blue")
c1.accelerator()