function reverseWord(word) {
  // Inicia uma variavel vazia
  let reversedWord = '';

  // itera sobre o parametro, iniciando na ultima letra e terminando na primeira
  for (let index = word.length - 1; index >= 0; index -= 1) {
    // Adiciona a ultima letra da palavra
    reversedWord += word[index];
  }

  return reversedWord;
}

function verifyPalindrome(word) {
  const loweredCaseWord = word.toLowerCase();
  const reversedWord = reverseWord(loweredCaseWord);
  const isPalindrome = loweredCaseWord === reversedWord;

  return isPalindrome;
}

// Com Split
function verifyPalindrome (string) {
  const reverse = string.split('').reverse().join('');

  if (reverse === string) {
    return true;
  } else {
    return false;
  }
};