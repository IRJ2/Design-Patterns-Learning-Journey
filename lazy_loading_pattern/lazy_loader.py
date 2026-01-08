class LazyLoader:
    def __init__(self, filename):
        self.filename = filename
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("Loading heavy data from file...")
            self._data = [line for line in range(10000)]  # simulate heavy data loading
        return self._data
    
# Usage:
loader = LazyLoader("heavy_data.txt")
print("LazyLoader initialized.")
# Accessing data for the first time triggers loading
data = loader.data    