from process import Process
class PrintingProcess(Process):
    def __init__(self, process_list) -> None:
        super().__init__()
        self.process_list = process_list
    def __str__(self) -> str:
        return f"{super().__str__()}, Type: PrintingProcess"
    def __repr__(self) -> str:
        return f"PrintingProcess({self.get_pid()})"
    def serialize(self):
        pass
    def deserialize(self):
        pass
    
    def execute(self):
        for i in self.process_list:
            print(i)