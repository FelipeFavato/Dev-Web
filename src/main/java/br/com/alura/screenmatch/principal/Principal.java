package br.com.alura.screenmatch.principal;
import java.util.Scanner;

import br.com.alura.screenmatch.service.ConsumoApi;

public class Principal {

  // Constante estatica (pode ser acessada diretamente pela classe)
  public static final String EXEMPLO = "Exemplo";

  // Escaneia dados que forem digitados e enviados pela CLI
  private Scanner leitura = new Scanner(System.in);

  // Gera um atributo para a classe Principal usar como um todo
  private ConsumoApi consumo = new ConsumoApi();

  // Declarando constantes:
  // final => indica que esse dado nao ira mudar
  // LETRAS_MAIUSCULAS => Padrão de constantes
  private final String ENDERECO = "https://www.omdbapi.com/?t=";

  private final String API_KEY = "&apikey=6585022c";
  
  public void exibeMenu() {
    System.out.println("Digite o nome da série");
    // .nextLine() => É assim que captura uma string da saida do terminal
    var nomeSerie = leitura.nextLine();
    var json = consumo.obterDados(ENDERECO + nomeSerie.replace(" ", "+") + API_KEY);
    // replace(old, new) => Sempre que achar o old, troca pelo new
    // ENDERECO + nomeSerie.replace(" ", "+") + API_KEY;
    // "https://www.omdbapi.com/?t=gilmore+girls&apikey=6585022c"
  }
}
