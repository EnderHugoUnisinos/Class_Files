from process import Process
class WritingProcess(Process):
    def __init__(self, expression) -> None:
        super().__init__()
        self.expression = expression
    def __str__(self) -> str:
        return super().__str__()
    def __repr__(self) -> str:
        return f"WritingProcess({self.get_pid})"
    def serialize(self):
        pass
    def deserialize(self):
        pass

    def execute(self, path):
        try:
            with open(path, "a") as file:
                file.write(self.expression)
            return True
        except: 
            return False