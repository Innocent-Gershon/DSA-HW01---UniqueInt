const fs = require('fs');

// Helper function to read integers from the input file
function readNextItemFromFile(inputFileStream) {
    let line;
    try {
        line = inputFileStream.readLine();
        // If line contains only whitespace or is empty, return null
        if (!line || /^\s*$/.test(line)) {
            return null;
        }
        // Remove leading and trailing whitespace
        line = line.trim();

        // Check if the line contains a single integer
        if (/\s/.test(line)) {
            // If there are more than one integer, skip the line
            return null;
        }

        const num = parseInt(line);
        // If the number is NaN or it's a non-integer, skip the line
        if (isNaN(num)) {
            return null;
        }
        return num;

    } catch (err) {
        console.error('Error reading line:', err);
        return null;
    }
}

// Main function to process the file
function processFile(inputFilePath, outputFilePath) {
    // Read the input file
    const inputFileStream = fs.readFileSync(inputFilePath, 'utf-8').split('\n');
    const uniqueIntegers = new Set(); // Use a Set to ensure uniqueness

    // Read through each line of the input file
    for (let i = 0; i < inputFileStream.length; i++) {
        const number = readNextItemFromFile(inputFileStream[i]);
        if (number !== null) {
            uniqueIntegers.add(number); // Only add unique numbers
        }
    }

    // Convert the Set of unique integers to an array and sort it
    const sortedUniqueIntegers = Array.from(uniqueIntegers).sort((a, b) => a - b);

    // Write the sorted unique integers to the output file
    const result = sortedUniqueIntegers.join('\n');
    fs.writeFileSync(outputFilePath, result);
    console.log(`Output written to ${outputFilePath}`);
}

// Example usage
const inputFilePath = 'sample_inputs/sample_input_02.txt'; // Specify your input file path
const outputFilePath = 'sample_results/sample_input_02.txt_results.txt'; // Specify your output file path

processFile(inputFilePath, outputFilePath);
