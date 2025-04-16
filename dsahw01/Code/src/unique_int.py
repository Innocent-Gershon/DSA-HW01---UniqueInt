import os
import time
import tracemalloc

class UniqueInt:
    def __init__(self):
        self.seen = [False] * 2047  # -1023 to 1023 mapped to 0–2046
        self.unique_numbers = []

    def map_index(self, num):
        return num + 1023

    def custom_sort(self, arr):
        # Manual implementation of Bubble Sort
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def reset(self):
        self.seen = [False] * 2047
        self.unique_numbers = []

    def is_valid_line(self, line):
        tokens = line.strip().split()
        if len(tokens) != 1:
            return False
        try:
            int(tokens[0])
            return True
        except:
            return False

    def processFile(self, inputFilePath, outputFilePath):
        self.reset()
        try:
            with open(inputFilePath, 'r') as infile:
                for line in infile:
                    if not self.is_valid_line(line):
                        continue
                    num = int(line.strip())
                    idx = self.map_index(num)
                    if not self.seen[idx]:
                        self.seen[idx] = True
                        self.unique_numbers.append(num)
        except FileNotFoundError:
            print(f"❌ File not found: {inputFilePath}")
            return

        self.custom_sort(self.unique_numbers)

        with open(outputFilePath, 'w') as outfile:
            for num in self.unique_numbers:
                outfile.write(f"{num}\n")

        print(f"✅ Output written to: {outputFilePath}")

if __name__ == "__main__":
    import_path = os.path.abspath(os.path.join(__file__, "../../sample_inputs"))
    export_path = os.path.abspath(os.path.join(__file__, "../../sample_results"))

    processor = UniqueInt()

    for filename in os.listdir(import_path):
        if filename.endswith(".txt"):
            input_file = os.path.join(import_path, filename)
            result_file = os.path.join(export_path, f"{filename}_results.txt")

            tracemalloc.start()
            start_time = time.time()

            processor.processFile(input_file, result_file)

            end_time = time.time()
            current, _ = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"⏱️ Runtime: {round((end_time - start_time) * 1000, 2)} ms")
            print(f"📦 Estimated memory used: {current} bytes\n")
