// Utilize if/else para escrever um código que retorne o maior de três números.
// Defina, no começo do seu código, três variáveis com os valores que serão comparados.

const biggestNumber = (num1, num2, num3) => {
  const biggestNum1 = num1 > num2 && num1 > num3
  const biggestNum2 = num2 > num1 && num2 > num3

  if (biggestNum1) return num1;
  if (biggestNum2) return num2;
  return num3
}
