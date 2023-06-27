// Crie a pasta unix_tests_skills e navegue até ela.
//   mkdir unix_tests_skills
//   cd /home/joaozinho/unix_tests_skills
//   pwd

// Crie um arquivo de texto pelo terminal com o nome skills2.txt e adicione os valores Internet, Unix e Bash, cada um em sua linha.
//   touch skills2.txt
//   echo "Internet" >> skills2.txt
//   echo "Unix" >> skills2.txt
//   echo "Bash" >> skills2.txt

// Adicione mais 5 itens à sua lista de skills e, depois, imprima a lista ordenada no terminal.
//   echo "HTML" >> skills2.txt
//   echo "CSS" >> skills2.txt
//   echo "JavaScript" >> skills2.txt
//   echo "React" >> skills2.txt
//   echo "SQL" >> skills2.txt
//   sort < skills2.txt

// Conte o número de linhas do arquivo skills2.txt.
//   cat skills2.txt | wc -l

// Crie um arquivo chamado top_skills.txt usando o skills2.txt. Ele deve conter as 3 primeiras skills em ordem alfabética.
//   sort < skills2.txt | head -n 3 > top_skills.txt

// Crie um novo arquivo chamado phrases2.txt pelo terminal e adicione algumas frases de sua escolha.
//   touch phrases2.txt
//   echo "The quick brown fox jumps over the lazy dog." > phrases2.txt
//   echo "Quick fox jumps nightly above wizard." >> phrases2.txt
//   echo "The quick onyx goblin jumps over the lazy dwarf." >> phrases2.txt

// Conte o número de linhas que contêm as letras br.
//   grep br phrases2.txt | wc -l

// Conte o número de linhas que não contêm as letras br.
//   grep -v br phrases2.txt | wc -l

// Adicione dois nomes de países ao final do arquivo phrases2.txt.
//   echo "Japão" >> phrases2.txt
//   echo "Austrália" >> phrases2.txt

// Crie um novo arquivo chamado bunch_of_things.txt com os conteúdos dos arquivos phrases2.txt e countries.txt.
//   cp countries.txt bunch_of_things.txt
//   cat phrases2.txt >> bunch_of_things.txt

// Ordene o arquivo bunch_of_things.txt.
//   sort bunch_of_things.txt -o bunch_of_things.txt