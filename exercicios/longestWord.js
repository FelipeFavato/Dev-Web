function getLongestWord(words) {
  let longestWord = words[0];

  for (let index = 0; index < words.length; index += 1) {
    const currentWord = words[index];

    if (longestWord.length < currentWord.length) {
      longestWord = currentWord;
    }
  }

  return longestWord;
}