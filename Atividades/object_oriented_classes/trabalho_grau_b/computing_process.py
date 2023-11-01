from process import Process
class ComputingProcess(Process):
    def __init__(self, expression) -> None:
        super().__init__()
        self.expression = expression
    def __str__(self) -> str:
        return f"{super().__str__()}, Expression: {self.expression}, Type: ComputingProcess"
    def __repr__(self) -> str:
        return f"ComputingProcess({self.get_pid()})"
    def serialize(self):
        pass
    def deserialize(self):
        pass
    
    def execute(self):
        result = eval(self.expression)
        print(result)