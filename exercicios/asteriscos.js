const printSquareAsterisk = (size) => {
  const asterisk = '*'
  for (i = 0; i < size; i += 1) {
    console.log(asterisk.repeat(size))
  }
}

printSquareAsterisk(5)

let n = 5;
let symbol = '*';
let inputLine = '';

for (let lineIndex = 0; lineIndex < n; lineIndex += 1) {
  inputLine = inputLine + symbol;
};

for (let lineIndex = 0; lineIndex < n; lineIndex += 1) {
  console.log(inputLine);
};
