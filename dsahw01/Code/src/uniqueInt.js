const fs = require('fs');
const path = require('path');

// Input and output paths relative to current file
const inputFileName = 'sample_input_01.txt';
const inputPath = path.join(__dirname, '..', '..', 'sample_inputs', inputFileName);
const outputFileName = `${inputFileName}_results.txt`;
const outputPath = path.join(__dirname, '..', '..', 'sample_results', outputFileName);

try {
  const start = process.hrtime();

  // Read the input file
  const inputData = fs.readFileSync(inputPath, 'utf8');
  const numbers = inputData.trim().split(/\s+/).map(Number);

  // Filter unique integers and sort them
  const uniqueSorted = [...new Set(numbers)].sort((a, b) => a - b);

  // Write to output file
  fs.writeFileSync(outputPath, uniqueSorted.join('\n'), 'utf8');

  const end = process.hrtime(start);
  const runtimeMs = (end[0] * 1e9 + end[1]) / 1e6;

  // Estimate memory usage
  const memoryBytes = Buffer.byteLength(uniqueSorted.join('\n'), 'utf8');

  console.log(`✅ Output written to: ${outputPath}`);
  console.log(`⏱️ Runtime: ${runtimeMs.toFixed(2)} ms`);
  console.log(`📦 Estimated memory used: ${memoryBytes} bytes`);
} catch (err) {
  console.error(`❌ Error reading or writing file:\n${err.message}`);
}
