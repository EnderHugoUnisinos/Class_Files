from process import Process
from computing_process import ComputingProcess

class ReadingProcess(Process):
    def __init__(self) -> None:
        super().__init__()
    def __str__(self) -> str:
        return super().__str__()
    def __repr__(self) -> str:
        return f"ReadingProcess({self.get_pid()})"
    def serialize(self):
        pass
    def deserialize(self):
        pass
    
    def execute(self, path, process_list):
        with open(path, "r+") as file:
            string_list = file.readlines()
            file.write("")
        for i in string_list:
            process_list.append(ComputingProcess(i))