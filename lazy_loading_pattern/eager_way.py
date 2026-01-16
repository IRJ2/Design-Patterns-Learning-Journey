class EagerLoader:
    def __init__(self, filename):
        self.data = self._load_data(filename)

    def _load_data(self, filename):
        print("Reading heavy data from file...")
        # simulate heavy data loading
        return [line for line in range(10000)]
    
# Usage:
loader = EagerLoader("heavy_data.txt")
print("EagerLoader initialized.")
# Data is already loaded during initialization
data = loader.data
print("Data accessed.")