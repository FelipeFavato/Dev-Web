package br.com.alura.screenmatch.model;

import com.fasterxml.jackson.annotation.JsonAlias;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

// id, url, width, heigth

// Quando JSON é serializado => Convertido de objetos Java para JSON
// Quando JSON é desserializado => Convertido de JSON para objetos Java


// JsonIgnoreProperties => Tudo que eu nao mapear no meu codigo sera
// ignorado pelas minhas classes e nao sera lido
// ignoreUnknown vem como false por default
@JsonIgnoreProperties(ignoreUnknown = true)
public record DadosSerie(
  // @JsonAlias => Vai ter no arquivo JSON uma chave chamada "id",
  // outra chave camada "url" e assim por diante todas as chaves e ai
  // vai trazer para virar ID ou URL ou oque for que eu coloque
  // Lê o arquivo Json e escreve oque eu pedir
  @JsonAlias("Title") String titulo,
  @JsonAlias("totalSeasons") Integer totalTemporadas,
  @JsonAlias("imdbRating") String avaliacao
  ) {}
