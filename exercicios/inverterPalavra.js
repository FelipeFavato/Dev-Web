let word = 'tryber';

const splited = word.split(''); // [ 't', 'r', 'y', 'b', 'e', 'r' ]

const reversed = splited.reverse(); // [ 'r', 'e', 'b', 'y', 'r', 't' ]

const joined = reversed.join(''); // rebyrt


const reverseWords = (string) => string.split('').reverse().join('');

console.log(reverseWords('Felipe'))