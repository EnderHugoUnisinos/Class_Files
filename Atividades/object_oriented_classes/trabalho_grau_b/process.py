import itertools
class Process():
    id_obj = itertools.count()
    
    def __init__(self) -> None:
        self.pid = next(Process.id_obj)
    def __str__(self) -> str:
        return f"PId: {self.pid}"
    def __repr__(self) -> str:
        return f"Process({self.pid})"
    
    def get_pid(self):
        return self.pid
    
    def execute(self):
        pass