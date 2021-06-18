// import 'dart:math';
import 'dart:io';

void main() {
  print("\nLet's Get Started !\n");
  print("---------------------------------");
  print("|  Created By iThACK Community  |");
  print("---------------------------------");

  var lower_alpha = "qwertyuioplkjhgfdsazxcvbnm";
  var upper_alpha = "MNBVCXZASDFGHJKLPOIUYTREWQ";
  var punch = "!@#%^&*()_+=-|}{\\][:';?></.,'";
  var num = "0123456789";
  stdout.write("\nPassword Length ==>> ");

  var passlenINPUT = stdin.readLineSync();
  var passlen = int.tryParse(passlenINPUT ?? "");

  List<String> charectors = num.split("") + lower_alpha.split("") + upper_alpha.split("") + punch.split("");
  charectors.shuffle();

  List<String> password = charectors.sublist(0, passlen);
  var firstPassword = password.join();

  password.shuffle();
  var secondPassword = password.join();

  print("\n---------------------------------\n");
  print("Your 1th Password : $firstPassword");
  print("Your 2nd Password : $secondPassword");
}
