from process import Process
from computing_process import ComputingProcess

class ReadingProcess(Process):
    def __init__(self, process_list, path) -> None:
        super().__init__()
        self.process_list = process_list
        self.path = path
    def __str__(self) -> str:
        return f"{super().__str__()}, Type: ReadingProcess"
    def __repr__(self) -> str:
        return f"ReadingProcess({self.get_pid()})"
    def serialize(self):
        pass
    def deserialize(self):
        pass
    
    def execute(self):
        with open(self.path, "r+") as file:
            string_list = file.readlines()
            file.truncate(0)
        for i in string_list:
            self.process_list.append(ComputingProcess(i))