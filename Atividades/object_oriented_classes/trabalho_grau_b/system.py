import json
class System():
    def __init__(self) -> None:
        self.config = self.fetch_config()
        self.process_list = []
    
    def menu(self):
        while True:
            print("[1] : Create process")
            print("[2] : Execute next process")
            print("[3] : Execute specific process")
            print("[4] : Save process queue")
            print("[5] : Load process queue from file")
            print("[0] : Exit")
            
            user_input = input()
            match user_input:
                case "0":
                    quit()
                case "1":
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    pass
                case "5":
                    pass
                case _:
                    pass
    
    def fetch_config(self):
        try:
            path = "config.json"
            with open(path, "r") as file:
                data = json.load(file)
            return data
        except: 
            return False   
        
    def execute_next(self):
        pass
    def execute_specific(self):
        pass
    def save_queue(self):
        pass
    def load_queue(self):
        pass