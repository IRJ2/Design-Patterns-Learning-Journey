from functools import cache

class SmartLoader:
    @property
    @cache
    def heavy_calculation(self):
        print("Computing...")
        return sum(i * i for i in range(10000))

# First access: Prints "Computing..."
# Second access: Instant result, no print
loader = SmartLoader()
print(loader.heavy_calculation)
print(loader.heavy_calculation)