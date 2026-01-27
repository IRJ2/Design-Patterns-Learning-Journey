def lazy_stream_loader(filename):
    # This function returns a generator immediately
    # It does not read the whole file at once
    for i in range(10000):
        yield f"Line {i}"

# Usage
loader = lazy_stream_loader("demo.csv")
# The loop starts instantly; lines are loaded one by one
for line in loader:
    print(line)