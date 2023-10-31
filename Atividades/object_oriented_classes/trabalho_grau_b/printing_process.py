from process import Process
class PrintingProcess(Process):
    def __init__(self) -> None:
        super().__init__()
    def __str__(self) -> str:
        return super().__str__()
    def __repr__(self) -> str:
        return f"PrintingProcess({self.get_pid()})"
    def serialize(self):
        pass
    def deserialize(self):
        pass
    
    def execute(self, process_list):
        for i in process_list:
            print(i)