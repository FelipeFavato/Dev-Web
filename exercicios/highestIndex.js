function getHighestIndex(numbers) {
  let highestIndex = 0;

  for (let index = 0; index < numbers.length; index += 1) {
    if (numbers[highestIndex] < numbers[index]) {
      highestIndex = index;
    }
  }

  return highestIndex;
}