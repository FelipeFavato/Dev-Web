package br.com.alura.screenmatch.service;

public interface IConverteDados {
  // Generics => Nesse caso, vai me retornar algo
  // que eu nao sei ainda oque é e ai eu passo como 
  // segundo parametro essa Class do tipo generics 
  <T> T obterDados(String json, Class<T> classe);
}
