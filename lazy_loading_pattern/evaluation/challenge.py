import time
import random
from functools import cache

class SmartLogAnalyzer:
    def __init__(self):
        print("--- System Starting ---")
        self._config= None
        print("Reading all logs into memory...")
        self.logs = self._read_logs()

    @property
    def config(self):
        if self._config is None:
            print("Loading heavy config...", end="", flush=True)
            time.sleep(3) 
            self._config = {"region": "US-East", "retention": 365}
            print("Done!")
        return self._config

    def _read_logs(self):
        for i in range(1000000): # 1 million simulated logs
            yield f"Log line {i} - Status: {random.choice(['OK', 'ERROR'])}"

    @cache
    def get_error_count(self):
        print("Calculating error count...")
        count = 0
        for log in self.logs:
            if "ERROR" in log:
                count += 1
        return count

# --- Testing the Class ---
start_time = time.time()

# 1. Initialize
analyzer = SmartLogAnalyzer() 

# 2. Get Statistics (Simulate refreshing dashboard twice)
print(f"Errors: {analyzer.get_error_count()}")
print(f"Errors: {analyzer.get_error_count()}")

print(f"Total Time Taken: {time.time() - start_time:.2f} seconds")