const fatorial = (number) => {
  let result = 1;
  for (contador = number; contador > 0; contador -= 1) {
    result *= contador
  }

  return result;
}
