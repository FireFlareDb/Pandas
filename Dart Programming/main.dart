void main() {
  var name = "Abhi";
  var no = 12;
  print("My name is ${name}. And I'm ${no} years old.");
  double pi = 3.14;
  var list = [1, 2, 3];
  bool isValid = true;
  var student = {'A': 1, 'B': 2, 'C': 3};
  var heart_symbol = '\u2665';
  var laugh_symbol = '\u{1f600}';

  // ----------------------------------
  // print(no);
  // print(pi);
  // print(list);
  // print(isValid);
  // print(student);
  // print(heart_symbol);
  // print(laugh_symbol);

  // ----------------------------------

  // Convert Numberic Str Into Int
  var a = num.parse("35");
  var b = num.parse("34");
  print(a + b);

  String sd = "This";
  print(sd.codeUnits); // Will return list of UTF-16 code units
  print(sd.length);


  var list1 = [12, 34, 63, 3, 63];
  print(list1);
  list1.replaceRange(0, 3, [1, 3, 2, 4]);
  print(list1);
}