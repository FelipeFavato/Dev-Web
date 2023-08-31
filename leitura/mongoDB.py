# Documento => Um registro no MongoDB
# Estrutura de dados composta por pares de chaves e valores
# Documentos embarcados => Documento dentro de documento
# Coleção => Equivalente a uma tabela no modelo relacional
# Conjunto de documentos

# Os documentos são armazenados em um formato chamado de BSON
# (Binary JSON), que é uma representação binária de documentos JSON

# Parametro query


# use trybnb
# Ao executar o comando acima, você receberá uma mensagem dizendo
# switched to db trybnb e o prompt do terminal mudará para trybnb>.
# Isso significa que o mongosh está operando a partir desse
# momento no banco de dados trybnb.


# db.places.find(query, projection)  ===   SELECT * FROM places
# db.places.find({ '_id': 7 })
# db.places.find({ 'address.country_code': 'BR' })
# db.places.find({ 'address.country_code': 'BR' }).count()
# db.places.find({ '_id': 7 }, { 'name': true })
# db.places.find({ '_id': 7 }, { 'name': true, 'address': true })
# db.places.find({ '_id': 7 }, { 'address': false, 'host': false }) contrario
# query => Criterio de seleção a ser utilizado em uma pesquisa de documentos
# projetion => Quais chaves devem ser retornadas ou nao
# A primeira pergunta que podemos realizar ao MongoDB sobre os dados
# do banco trybnb é: “quais são os imóveis cadastrados no trybnb?”.
# Essa pergunta é o equivalente a realizar uma busca por todos os
# documentos cadastrados na coleção places. Logo, podemos escrever
# o comando acima no mongosh


# db.places.countDocuments()
# Mostra quantos documentos tem nessa coleção places


# db.places.find().sort({'_id': -1})
# Ordena respostas de forma descrescente
# db.places.find().sort({'_id': 1})
# Ordena respostas de forma crescente


# Operadores de comparação
# db.places.find({price: {$gt: 100}}, {price; true})

# $eq => Condição de igualdade
# {<chave> { $eq: <valor> }}

# $ne => Condição de não igualdade
# {<chave> { $ne: <valor> }}

# $gt => Maior que
# {<chave> { $gt: <valor> }}

# $gte => Maior ou igual
# {<chave> { $gte: <valor> }}

# $lt => menor que
# {<chave> { $lt: <valor> }}

# $lte => menor ou igual
# {<chave> { $lte: <valor> }}


# Inserção de dados
# Método insertOne() => Insere apenas um documento
# db.places.insertOne(
#     {_id:100,  name:"Casa na Lua", description:"Uma vista unica da Terra"}
# )
# Método insertMany([{...}, {...}]) => Insere um array de documentos


# Operadores de consulta em arrays

# $all
# Verifica a presença de valores dentro de um array
# db.places.find({ amenities: { $all: ["Stove", "Refrigerator"] } })


# $elemMatch  (ou)
# db.places.find(
#   {amenities: {$elemMatch: {$in: ["TV"]}}}, {_id: true, amenities: true}
# )


# Método Update
# updateOne() => Altera apenas um valor
# db.places.updateOne({where}, {$set: { chave: "novo valor" }})
# db.places.updateOne({where}, {$unset: { chave: "valor" }}) => Apaga chave
# db.places.updateOne({_id: 101}, {$set: { name: "Apartamento em Marte" }})


# updateMany() => Altera varios valores
# db.places.updateMany({_id: {$gte: 100}}, {$set: {isFree: true} })


# Método Delete
# deleteOne() => Deleta apenas um documento
# db.places.deleteOne({ _id: 11 })

# deleteMany() => Deleta varios documentos
# db.places.deleteMany({ "host.host_identity_verified": { $eq: false } })
# db.places.deleteMany({}) => Remove todos
