// mkdir unix_tests_search
// cd unix_tests_search
// curl -o countries.txt "https://gist.githubusercontent.com/kalinchernev/486393efcca01623b18d/raw/daa24c9fea66afb7d68f8d69f0c4b8eeb9406e83/countries"

// Mostre todo o conteúdo do arquivo countries.txt na tela.
//   cat countries.txt

// Mostre o conteúdo de countries.txt, página por página, até encontrar a Zambia.
//   less countries.txt
//   # ou...
//   more countries.txt

// Mostre novamente o conteúdo de countries.txt página por página, mas agora utilize um comando para buscar por Zambia.
//   less countries.txt
//   # ou...
//   more countries.txt
//   # Agora que você está dentro do arquivo, digite uma barra `/` e em seguida a palavra "Zambia".
//   # /Zambia
//   # Pressione *enter* para sair.

// Busque por Brazil no countries.txt.
//   grep Brazil countries.txt

// Busque novamente por brazil, mas agora utilize o lower case e não considere letras maiúsculas ou minúsculas.
//   grep -i brazil countries.txt

// -------------------------------------------------------------------------------------------------------------------------------

// De olho na dica 👀: Crie um novo arquivo chamado phrases.txt e adicione algumas frases à sua escolha.
// Não é necessário criar o arquivo pelo terminal.

// Busque pelas frases que não contenham a palavra fox.
//   grep -v fox phrases.txt

// Conte o número de palavras do arquivo phrases.txt.
//   wc -w phrases.txt

// Conte o número de linhas do arquivo phrases.txt.
//   wc -l phrases.txt


// De olho na dica 👀: Para contar o número de caracteres de um arquivo, não use wc -c, e sim wc -m.

// Crie os arquivos empty.tbt e empty.pdf.
//   touch empty.tbt
//   touch empty.pdf

// Liste todos os arquivos do diretório unix_tests_search.
//   ls

// Liste todos os arquivos que terminem com txt.
//   ls *txt

// Liste todos os arquivos que terminem com tbt ou txt.
//   ls *t?t

// Acesse o manual do comando ls.
//   man ls