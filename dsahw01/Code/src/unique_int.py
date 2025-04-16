import time

class UniqueInt:
    def __init__(self):
        # Support for integers from -1023 to 1023 → index 0 to 2046
        self.offset = 1023
        self.seen = [False] * 2047
        self.unique_values = []

    def is_valid_line(self, line):
        line = line.strip()
        if not line:
            return False
        parts = line.split()
        if len(parts) != 1:
            return False
        try:
            int(parts[0])
            return True
        except ValueError:
            return False

    def add_integer(self, number):
        index = number + self.offset
        if not self.seen[index]:
            self.seen[index] = True
            self.unique_values.append(number)

    def bubble_sort(self):
        n = len(self.unique_values)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.unique_values[j] > self.unique_values[j + 1]:
                    self.unique_values[j], self.unique_values[j + 1] = self.unique_values[j + 1], self.unique_values[j]

    def processFile(self, inputFilePath, outputFilePath):
        start_time = time.time()
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                if self.is_valid_line(line):
                    number = int(line.strip())
                    self.add_integer(number)

        self.bubble_sort()

        with open(outputFilePath, 'w') as outfile:
            for number in self.unique_values:
                outfile.write(f"{number}\n")

        end_time = time.time()
        runtime = round((end_time - start_time) * 1000, 2)
        memory_used = 2047 + (4 * len(self.unique_values))  # estimate: bool array + int values

        print(f"✅ Output written to: {outputFilePath}")
        print(f"⏱️ Runtime: {runtime} ms")
        print(f"📦 Estimated memory used: {memory_used} bytes")

# Example usage
if __name__ == "__main__":
    input_path = "/mnt/data/dsa/hw01/sample_inputs/sample_input_01.txt"
    output_path = "/mnt/data/dsa/hw01/sample_results/sample_input_01.txt_results.txt"

    unique_ints = UniqueInt()
    unique_ints.processFile(input_path, output_path)
