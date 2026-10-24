from datetime import datetime, time
from typing import Literal

class log_obj():
    logFile=None
    isWritinginFile=True
    def setFile(self, file):
        self.logFile=file
    def log(self, message, where: str, mesType: Literal["INFO", "ERROR", "WARNING", "DEBUG"] = "INFO"):
        if self.isWritinginFile:
            if self.logFile is not None:
                with open(self.logFile, 'a') as f:
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"[{timestamp}] [{mesType}] [FROM:{where}] {message}\n")
            else:
                print("Log file not set. Please set the log file using setFile() method.")
        else:
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"LOG> [{timestamp}] [{mesType}] [FROM:{where}] {message}")
    def __init__(self):
        if self.logFile is None:
            self.logFile=f"log{datetime.now().strftime('%Y%m%d')}.log"
