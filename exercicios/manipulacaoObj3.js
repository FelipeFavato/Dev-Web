const school = {
  lessons: [
    {
      course: 'Python',
      students: 20,
      professor: 'Carlos Patrício',
      shift: 'Manhã',
    },
    {
      course: 'Kotlin',
      students: 10,
      professor: 'Gabriel Oliva',
      shift: 'Noite',
    },
    {
      course: 'JavaScript',
      students: 738,
      professor: 'Gustavo Caetano',
      shift: 'Tarde',
    },
    {
      course: 'MongoDB',
      students: 50,
      shift: 'Noite',
    },
  ]
};

// Crie uma função que obtenha o valor da chave de acordo com sua posição no array.
// Essa função deve possuir dois parâmetros: o objeto e a posição no array.
const getValue = (obj, position) => Object.values(obj)[position]

// Crie uma função que retorne a soma do número total de estudantes em todos os cursos.
const totalStudents = (obj) => {
  const { lessons } = obj;
  total = 0;
  for (i = 0; i < lessons.length; i += 1) {
    total += lessons[i]['students']
  }

  return total
}

// Crie uma função que verifica se uma determinada chave existe em todos os elementos
// do array lessons. O retorno deve ser um booleano (true ou false).
// Essa função deve possuir dois parâmetros: o objeto e o nome da chave.
const verifyProp = (obj, key) => {
  const { lessons } = obj;
  for (let index = 0; index < lessons.length; index += 1) {
    if (lessons[index][key] === undefined) {
      return false;
    }
  }
  return true;
}

console.log(verifyProp(school, 'students')); // true

// Crie uma função para alterar o turno para noite no curso de Python.
// Essa função deve ter três parâmetros: a base de dados a ser modificada,
// o nome do curso e o novo valor da chave.

const changeKey = (obj, course, value) => {
  // Encontra o elemento que o course é igual a Python
  let findCourse;
  for (let index = 0; index < obj.lessons.length; index += 1) {
    let element = obj.lessons[index];
    if (element.course === course) {
      findCourse = element;
      break;
    }
  }

  // Condição para exibir o resultado. Caso o findCourse seja undefined, significa que o curso não foi encontrado.
  if (findCourse !== undefined) {
    findCourse.shift = value;
    return findCourse;
  } else {
    return 'Curso não encontrado.';
  }
};

console.log(changeKey(school, 'Python', 'Noite'));