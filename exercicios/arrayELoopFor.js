const numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27];

// Percorra o array imprimindo todos os valores contidos nele com a função console.log().
// for (i = 0; i < numbers.length; i += 1) {
//   console.log(numbers[i])
// }

// Some todos os valores contidos no array e imprima o resultado.
const sum = (array) => {
  let sum = 0
  for (i = 0; i < numbers.length; i += 1) {
    sum += numbers[i]
  }

  return sum
}

// Calcule e imprima a média aritmética dos valores contidos no array.
// A média aritmética é o resultado da soma de todos os elementos
// dividido pelo número total de elementos.
const media = (array) => {
  let sum = 0
  for (i = 0; i < array.length; i += 1) {
    sum += array[i]
  }

  return sum / array.length
}

// Com base no código que acabou de gerar, referente ao cálculo da média
// aritmética, faça com que: caso o valor final seja maior que 20,
// imprima a mensagem “O valor da média aritmética é maior que 20”;
// e, caso não seja maior que 20, imprima a mensagem “O valor da
// média aritmética é menor ou igual a 20”.
const comparisom = (array) => {
  const mediaAr = media(array);

  return mediaAr > 20 ?
  'O valor da média aritmética é maior que 20' :
  'O valor da média aritmética é menor ou igual a 20';
}

// Utilizando for, descubra o maior valor contido no array e imprima-o.
const biggestValue = (array) => {
  let biggestNumber = array[0];
  for(i = 0; i< array.length; i += 1) {
    biggestNumber < array[i] ? biggestNumber = array[i] : biggestNumber;
  }

  return biggestNumber;
}

// Descubra quantos valores ímpares existem no array e imprima o resultado.
// Caso não exista nenhum, imprima a mensagem: “Nenhum valor ímpar encontrado”.
const oddNumbers = (array) => {
  let oddTotal = 0;
  for(i = 0; i < array.length; i += 1) {
    array[i] % 2 !== 0 ? oddTotal += 1 : oddTotal;
  }

  return oddTotal === 0 ?
  'Nenhum valor impar encontrado' : oddTotal;
}
