### The Scenario: "The Frozen Dashboard"

You have been hired by a data analytics startup. They have a Python class called `LogAnalyzer` used to process server logs.

**The Problem:**

1. **Slow Startup:** When the app starts, it freezes for 3 seconds (simulating a connection).
2. **Memory Crash:** It tries to load "all logs" into a list immediately, which crashes the server when the file gets too big.
3. **CPU Waste:** Every time the dashboard refreshes the "Error Count", it recalculates it from scratch, wasting CPU cycles.

---

### 1. The "Bad" Code (Start Here)

Copy this code into a file named `challenge.py`. Run it to see how slow it is.

```python
import time
import random

class LogAnalyzer:
    def __init__(self):
        print("--- System Starting ---")
        
        # PROBLEM 1: This simulates a heavy configuration loading
        # It blocks the app initialization for 3 seconds.
        print("Loading heavy config...", end="", flush=True)
        time.sleep(3) 
        self.config = {"region": "US-East", "retention": 365}
        print("Done!")

        # PROBLEM 2: This loads ALL data into memory at once.
        # In real life, this would be 50GB of text.
        print("Reading all logs into memory...")
        self.logs = self._read_logs()

    def _read_logs(self):
        # Simulates reading a massive file
        data = []
        for i in range(1000000): # 1 million simulated logs
            data.append(f"Log line {i} - Status: {random.choice(['OK', 'ERROR'])}")
        return data

    def get_error_count(self):
        # PROBLEM 3: This runs a heavy loop every single time you call it.
        print("Calculating error count...")
        count = 0
        for log in self.logs:
            if "ERROR" in log:
                count += 1
        return count

# --- Testing the Class ---
start_time = time.time()

# 1. Initialize
analyzer = LogAnalyzer() 

# 2. Get Statistics (Simulate refreshing dashboard twice)
print(f"Errors: {analyzer.get_error_count()}")
print(f"Errors: {analyzer.get_error_count()}")

print(f"Total Time Taken: {time.time() - start_time:.2f} seconds")

```

---

### 2. Your Mission

Refactor the class above into a new class called `SmartLogAnalyzer`. You must achieve the following **three objectives**:

#### **Step 1: Lazy Load the Config**

* **Goal:** The `__init__` method should finish **instantly**.
* **Task:** Move the configuration loading (the `time.sleep(3)` part) so it only happens the *first* time someone actually accesses `analyzer.config`.
* **Hint:** Use the `@property` decorator.

#### **Step 2: Stream the Logs (Generator)**

* **Goal:** Drastically reduce memory usage.
* **Task:** Change `_read_logs` so it does **not** create a list `[]`. It should `yield` one log line at a time.
* *Note: You will need to adjust `get_error_count` to loop over this generator.*

#### **Step 3: Cache the Result**

* **Goal:** The second time we print the error count, it should be instant and not print "Calculating error count...".
* **Task:** Use `functools` to cache the result of `get_error_count`.
* *Constraint:* Since you cannot easily cache a generator result directly (because generators get exhausted), you might need to structure your logic carefully. *Simpler Alternative:* For this specific step, assume `_read_logs` might still return a list, OR cache the *calculation* logic specifically if possible.
* *Self-Correction for Step 3:* If you switch to a pure generator in Step 2, you can't iterate over it twice (to count errors twice). For this exercise, you can either:
1. Keep the generator for the *raw data*, but accept that `get_error_count` consumes it once (and perhaps cache the integer result).
2. **Better Approach:** Create a cached property `error_count` that consumes the generator *once* and stores the final number.



---

### 3. Acceptance Criteria

When you run your **new** code:

1. **Immediate Output:** You should see `--- System Starting ---` immediately, without the 3-second pause.
2. **Delayed Config:** The "Loading heavy config..." message should only appear if you print `analyzer.config`.
3. **Fast Second Call:** The second `print(f"Errors: ...")` should be instant.

**Go ahead and try to write the solution!** Paste your refactored code here when you are done (or if you get stuck), and I will review it.