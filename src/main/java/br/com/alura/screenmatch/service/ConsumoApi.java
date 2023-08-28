package br.com.alura.screenmatch.service;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ConsumoApi {

  // Método obterDados => Retorna um arquivo JSON em formato de String
  // e precisa receber como parametro uma string que é um endereço web
  public String obterDados(String endereco) {
    // HttpClient é como se fosse o cliente
    HttpClient client = HttpClient.newHttpClient();
    // HttpRequest => eu crio uma URI para dizer para qual endereço vou fazer uma
    // requisição
    HttpRequest request = HttpRequest.newBuilder().uri(URI.create(endereco)).build();

    HttpResponse<String> response = null;

    // Meu cliente vai mandar essa rquisição e eu vou tentar receber essa resposta
    try {
      response = client.send(request, HttpResponse.BodyHandlers.ofString());
    } catch (IOException e) {
      throw new RuntimeException(e);
    } catch (InterruptedException e) {
      throw new RuntimeException(e);
    }

    // Corpo da resposta
    String json = response.body();
    return json;
  }
}
