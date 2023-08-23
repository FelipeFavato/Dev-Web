// Variavel local, declarada dentro de um metodo ou construtor
// void metodo () {
//   // variavel local pode ser declarada aqui
// }

record construtor () {
  // variavel local pode ser declarada aqui
}

class Pessoa {
  // Variavel estatica pode ser acessada dentro de qualquer escopo
  static int id = 1;
  // variavel local pode ser declarada aqui
  // Metodo estatico pode acessas variaveis estaticas
  static void metodo() {
    System.out.println(id);
  }

  static int x = 0;
  public static void setX(int x) {
    Pessoa.x = x;
  }

  int y = 0;
  public void setY(int y) {
    this.y = y;
  }
}


// public class Teste {

//   // Variavel de instancia/Atributo ->
//   // Pode ser acessada em qualquer lugar dentro desse escopo
//   String nome;

//   public void m1() {
//     int x = 10;

//     System.out.println(x);
//   }

//   // public static void main(String[] args) {
//   //   Teste t = new Teste();
//   //   t.m1();
//   // }

//   public static void main(String[] args) {
//     Pessoa p = new Pessoa();
//     System.out.println(p.id);
//   }
// }