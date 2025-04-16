# DSA-HW01---UniqueInt

🧾 Instructions to Run the Program
This program reads all .txt input files from the sample_inputs/ directory, removes duplicates, skips invalid and repeated entries, sorts the integers manually (without using built-in functions), and writes the sorted unique integers into the sample_results/ directory.

📁 Project Folder Structure
Make sure your project is organized as follows:

css
Copy
Edit
/dsa/hw01/
│
├── code/
│   └── src/
│       └── unique_int.py         ← Main program file
│
├── sample_inputs/                ← All  input .txt files here
│   ├── sample_input_01.txt
│   └── sample_input_02.txt
│
└── sample_results/               ← This is where result files will be saved
⚙️ How to Run the Program
Open your terminal (or PowerShell on Windows).

Navigate to the folder containing unique_int.py:

bash
Copy
Edit
cd path/to/dsa/hw01/code/src
For example:

bash
Copy
Edit
cd "C:\Users\YourName\Desktop\dsa\hw01\code\src"
Run the program:

bash
Copy
Edit
python unique_int.py
✅ You’ll see success messages like:

yaml
Copy
Edit
✅ Output written to: ../../sample_results/sample_input_01.txt_results.txt
⏱️ Runtime: 1.0 ms
📦 Estimated memory used: 2075 bytes
🧪 How It Works
Reads from: All .txt files in sample_inputs/

Validates each line: Skips lines with:

More than one number

Empty lines

Non-integer values

Removes duplicates

Sorts manually using Bubble Sort (no built-in .sort() or sorted())

Writes output to sample_results/ with filenames like:

Copy
Edit
sample_input_01.txt_results.txt
📌 Notes
The program handles integers in the range of -1023 to 1023 only.

You can add as many .txt files as you want into the sample_inputs/ folder. The program will process each one automatically.

