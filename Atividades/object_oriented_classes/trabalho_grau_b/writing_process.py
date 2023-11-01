from process import Process
class WritingProcess(Process):
    def __init__(self, expression, path) -> None:
        super().__init__()
        self.expression = expression
        self.path = path
    def __str__(self) -> str:
        return f"{super().__str__()}, Type: WritingProcess"
    def __repr__(self) -> str:
        return f"WritingProcess({self.get_pid})"
    def serialize(self):
        pass
    def deserialize(self):
        pass

    def execute(self):
        try:
            with open(self.path, "a") as file:
                file.write(f"{self.expression}\n")
            return True
        except: 
            return False