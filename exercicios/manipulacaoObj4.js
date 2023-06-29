const basket = [
  'Melancia', 'Abacate', 'Melancia', 'Melancia', 'Uva', 'Laranja',
  'Jaca', 'Pera', 'Melancia', 'Uva', 'Laranja', 'Melancia',
  'Banana', 'Uva', 'Pera', 'Abacate', 'Laranja', 'Abacate',
  'Banana', 'Melancia', 'Laranja', 'Laranja', 'Jaca', 'Uva',
  'Banana', 'Uva', 'Laranja', 'Pera', 'Melancia', 'Uva',
  'Jaca', 'Banana', 'Pera', 'Abacate', 'Melancia', 'Melancia',
  'Laranja', 'Pera', 'Banana', 'Jaca', 'Laranja', 'Melancia',
  'Abacate', 'Abacate', 'Pera', 'Melancia', 'Banana', 'Banana',
  'Abacate', 'Uva', 'Laranja', 'Banana', 'Abacate', 'Uva',
  'Uva', 'Abacate', 'Abacate', 'Melancia', 'Uva', 'Jaca',
  'Uva', 'Banana', 'Abacate', 'Banana', 'Uva', 'Banana',
  'Laranja', 'Laranja', 'Jaca', 'Jaca', 'Abacate', 'Jaca',
  'Laranja', 'Melancia', 'Pera', 'Jaca', 'Melancia', 'Uva',
  'Abacate', 'Jaca', 'Jaca', 'Abacate', 'Uva', 'Laranja',
  'Pera', 'Melancia', 'Jaca', 'Pera', 'Laranja', 'Jaca',
  'Pera', 'Melancia', 'Jaca', 'Banana', 'Laranja', 'Jaca',
  'Banana', 'Pera', 'Abacate', 'Uva',
];

const countMelancias = (array) => {
  total = 0;
  for (i = 0; i < array.length; i += 1) {
    if (array[i] === 'Melancia') {
      total += 1
    }
  }

  return total;
};

const countAbacates = (array) => {
  total = 0;
  for (i = 0; i < array.length; i += 1) {
    if (array[i] === 'Abacate') {
      total += 1
    }
  }

  return total;
}

const countUvas = (array) => {
  total = 0;
  for (i = 0; i < array.length; i += 1) {
    if (array[i] === 'Uva') {
      total += 1
    }
  }

  return total;
}

const countElements = (array) => {
  const countedBasket = {
    Melancia: countMelancias(array),
    Abacate: countAbacates(array),
    Uva: countUvas(array),
  }

  return `Sua cesta possui ${countedBasket.Melancia} Melancias, ${countedBasket.Abacate} Abacates e ${countedBasket.Uva} Uvas.`
}

// Alternativa geral
// Criação de objeto
const result = {};

// Loop que irá contar quantas vezes cada fruta aparece no array basket
for (let index = 0; index < basket.length; index += 1) {
  let fruit = basket[index];
  // Se a propriedade com o nome da fruta ainda não existir, então ela será criada com o valor 1. Caso ela já exista, vamos incrementar o valor.
  if (!result[fruit]) {
    result[fruit] = 1;
  } else {
    result[fruit] += 1;
  }
};

// Convertemos o objeto result em um array
const entries = Object.entries(result);
console.log(entries)

// Criação de um novo array
let newArray = [];

// Loop que irá verificar se o número de frutas é maior ou não do que 1. Caso seja maior, adicionamos a letra "s".
for (let index = 0; index < entries.length; index += 1) {
  if (entries[index][1] > 1) {
    newArray.push(`${entries[index][1]} ${entries[index][0]}s`);
  } else {
    newArray.push(`${entries[index][1]} ${entries[index][0]}`);
  }
};

// Exibimos a string juntando os valores do array "newArray" com uma vírgula e um espaço em branco.
console.log(`Sua cesta possui: ${newArray.join(', ')}.`);
