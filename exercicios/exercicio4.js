// Utilize if...else para escrever um código que defina três variáveis
// com os valores dos três ângulos internos de um triângulo. Retorne
// true se os ângulos representarem os ângulos de um triângulo e false,
// caso contrário. Se algum ângulo for inválido, você deve retornar uma mensagem de erro.

// 👀 Dica: para os ângulos serem de um triângulo válido, a soma dos três
// ângulos deve ser 180 graus. Um ângulo será considerado inválido se não tiver um valor positivo.

const checkTriangle = (side1, side2, side3) => side1 + side2 + side3 === 180 && side1 > 0 && side2 > 0 && side3 > 0;
