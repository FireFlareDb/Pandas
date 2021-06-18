import 'dart:io';

void main() {
  var pas = {1: ['this', 'is', 'password'], 2: ['me', 'and', 'Ipassword']};
  int start = 3;

  while (true) {
  stdout.write("\nName ==>> ");
  String name = stdin.readLineSync().toString();
  stdout.write("\nDescription ==>> ");
  String desc = stdin.readLineSync().toString();
  stdout.write("\npassword ==>> ");
  String password = stdin.readLineSync().toString();

  pas.addAll({start:[name, desc, password]});
  print(pas);
  start++;
  }
}