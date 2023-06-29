function getSmallestIndex(numbers) {
  let smallestIndex = 0;

  for (let index = 0; index < numbers.length; index += 1) {
    if (numbers[smallestIndex] > numbers[index]) {
      smallestIndex = index;
    }
  }

  return smallestIndex;
}