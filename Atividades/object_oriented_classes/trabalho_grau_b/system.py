import json
from printing_process import PrintingProcess
from reading_process import ReadingProcess
from computing_process import ComputingProcess
from writing_process import WritingProcess

class System():
    def __init__(self) -> None:
        self.config = self.fetch_config()
        self.process_queue = []
        self.load_queue()
    
    def menu(self):
        while True:
            self.save_queue()
            print("\n[1] : Create process")
            print("[2] : Execute next process")
            print("[3] : Execute specific process")
            #print("[4] : Save process queue")
            #print("[5] : Load process queue from file")
            print("[0] : Exit\n")
            
            user_input = input("Select one of the options written above: ")
            match user_input:
                case "0":
                    quit()
                case "1":
                    self.create_process()
                case "2":
                    self.execute_next()
                case "3":
                    self.execute_specific()
                #case "4":
                #    self.save_queue()
                #case "5":
                #    self.load_queue()
                case _:
                    self.error_message("Please select one of the given menu options.")
    
    def fetch_config(self):
        try:
            path = "assets/config.json"
            with open(path, "r") as file:
                data = json.load(file)
            return data
        except: 
            return False   
        
    def create_process(self):
        try:
            print("[C]: Computing process")
            print("[R]: Reading process")
            print("[W]: Writing process")
            print("[P]: Printing process")
            user_input = input("Select one of the process types: ")
            match user_input.upper():
                case "C":
                    self.process_queue.append(ComputingProcess(input("Insert expression: ")))
                case "R":
                    self.process_queue.append(ReadingProcess(self.process_queue, self.config["computation_path"]))
                case "W":
                    self.process_queue.append(WritingProcess(input("Insert expression: "), self.config["computation_path"]))
                case "P":
                    self.process_queue.append(PrintingProcess(self.process_queue))
                case _:
                    self.error_message("Invalid process type. Returning to main menu...")
        except:
            self.error_message("Something went wrong. Returning to main menu...")
    def execute_next(self):
        try:
            self.process_queue[0].execute()
            self.process_queue.pop(0)
        except:
            self.error_message("Something went wrong. Returning to main menu...")
    def execute_specific(self):
        try:
            user_input = input("Insert PId of process: ")
            index = self.find_by_pid(user_input)
            if index != None:
                self.process_queue[index].execute()
                self.process_queue.pop(index)
        except:
            self.error_message("Something went wrong. Returning to main menu...") 
    def save_queue(self):
        serialized_queue = []
        for i in self.process_queue:
            serialized_queue.append(i.serialize())
        try:
            with open(self.config["queue_path"], "w") as file:
                file.writelines(line + "\n" for line in serialized_queue)
        except: 
            self.error_message("Something went wrong.")
             
    def load_queue(self):
        self.process_queue = []
        with open(self.config["queue_path"], "r+") as file:
            serialized_queue = file.readlines()
            file.truncate(0)
        for i in serialized_queue:
            data = i.split(",")
            match data[0]:
                case "W":
                    self.process_queue.append(WritingProcess(data[1], self.config["computation_path"]))
                case "R":
                    self.process_queue.append(ReadingProcess(self.process_queue, self.config["computation_path"]))
                case "P":
                    self.process_queue.append(PrintingProcess(self.process_queue))
                case "C":
                    self.process_queue.append(ComputingProcess(data[1]))

    def find_by_pid(self, pid):
        try:
            for id, i in enumerate(self.process_queue):
                if i.get_pid() == int(pid):
                    return int(id)
            self.error_message("PId not found.")
            return None
        except:
            self.error_message("Something went wrong. Invalid PId.")
    def error_message(self, message):
        print(message)