function countHighestNumberMaxOccurrences(numbers) {
  if (numbers.length === 0) {
    return 0;
  }

  const highestIndex = getHighestIndex(numbers);
  const highestNumber = numbers[highestIndex];

  let occurrencesCounter = 0;

  for (let index = 0; index < numbers.length; index += 1) {
    const currentNumber = numbers[index];

    if (currentNumber === highestNumber) {
      occurrencesCounter += 1;
    }
  }

  return occurrencesCounter;
}