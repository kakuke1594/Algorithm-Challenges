> This challenge from TFC events

# Question
Bạn được cho một chuỗi các ký tự in HOA bằng Tiếng Anh. Bạn có thể đánh dấu bất kỳ ký tự nào ( có thể 1 hoặc nhiều, tất cả hoặc không đánh dấu ký tự nào). Những ký tự được đánh dấu không cần phải nằm liền kề nhau. Chuỗi ký tự mới được tạo ra bằng cách xử lý những ký tự của chuỗi cho ban đầu từ trái sang phải: những ký tự không được đánh dấu được cộng 1 lần vào chuỗi ký tự mới, những ký tự đã được đánh dấu được cộng 2 lần vào chuỗi ký tự mới.

Ví dụ: HELLOWORLD -> HHELLLOWOORLLD
Trong ví dụ trên, nếu chuổi ký tự ban đầu là HELLOWORLD, bạn có thể đánh dấu ký tự H, ký tự L đầu tiên và cuối cùng, và ký tự O cuối cùng trong chuỗi để được: HELLOWORLD -> HHELLLOWOORLLD. Tương tự như vậy, nếu bạn không đánh dấu ký tự nào, bạn sẽ có chuỗi mới là: HELLOWORLD, và nếu bạn đánh dấu tất cả các ký tự, bạn sẽ có chuỗi mới là: HHEELLLLOOWWOORRLLDD. Chú ý là cho dù là cùng 1 ký tự giống nhau, nhưng nếu chúng ở vị trí khác nhau, chúng có thể được đánh dấu độc lập nhau.
 
Từ 1 chuỗi ký tự ban đầu, có nhiều chuỗi ký tự có thể được tạo ra bằng cách như trên, phụ thuộc vào việc bạn chọn đánh dấu ký tự nào. Trong tất cả những chuỗi ký tự được tạo ra, hãy xuất ra chuỗi ký tự đầu tiên theo thứ tự alphabetical (cũng được biết đến như lexicographical).

Chú ý: một chuỗi s xuất hiện trước một chuỗi t theo thứ tự alphabetical nếu s là một tiền tố (prefix) của t, hoặc s và t khác nhau và ký tự trong chuỗi s nằm trước ký tự trong chuỗi t theo thứ thự alphabet. Ví dụ, những chuỗi ký tự sau đây đã được sắp theo thứ tự alphabetical: CODE, HELLO, HI, HIM, HOME, JAM.

Input (stdin)
Dòng đầu tiên của input cho biết có bao nhiêu test cases, T. T test case nằm ở các dòng tiếp theo. Mỗi test case là một chuỗi ký tự S nằm ở 1 dòng.

Output (stdout)
Tương ứng mỗi test case, xuất ra 1 dòng theo format: Case #x: y, trong đó x là thứ tự của test case (bắt đầu từ 1), và y là chuỗi ký tự kết quả.

Limits:
- Giới hạn thời gian chạy code: 10 seconds.
- Giới bạn bộ nhớ: 1 GB.
1 <= T <= 100
Mỗi ký tự trong chuỗi S đều in HOA và nằm trong bảng chữ cái tiếng anh. Không có ký tự đặc biệt.

Ví dụ:

Input:
3
PEEL
AAAAAAAAAA
CODEJAMDAY

Output:
Case #1: PEEEEL
Case #2: AAAAAAAAAA
Case #3: CCODDEEJAAMDAAY

Trong ví dụ ở trên, ở test case #1, những chuỗi ký tự có thể được tạo ra theo thứ tự alphabetical là: PEEEEL, PEEEELL, PEEEL, PEEELL, PEEL, PEELL, PPEEEEL, PPEEEELL, PPEEEL, PPEEELL, PPEEL, và PPEELL.

Ở test case #2, tất cả các chuỗi ký tự có thể đưọc tạo ra đều chỉ có ký tự duy nhất là A với AAAAAAAAAA là tiền tố (prefix).

Ở test case #3, có tất cả 1024 chuỗi ký tự có thể được tạo ra, và chuỗi ký tự đầu tiên theo thứ tự alphabetical là CCODDEEJAAMDAAY.

# HOW TO RUN THIS PROGRAM
python3 double_letter.py
1. Input number of test cases
2. Input value of each test case

# HOW TO PLAY
Read the problem statement and submit your solutions in one of these programming language: You can use these programing languages: Bash, C (GCC), C# (Mono), C++17 (G++), Clojure, D (GDC), Dart, F# (Mono), Go 1.11.6, Groovy, Haskell (GHC), Java 11 (OpenJDK), JavaScript (Node.js), JavaScript (Node.js), Julia, Kotlin, Lisp (SBCL), Lua, OCaml, Objective-C (GNU), Octave, PHP, Pascal (FPC), Perl, PyPy 3, Python 3.7, R, Ruby,Rust, Scala,Swift, TypeScript (Node.js), Visual Basic (Mono)

# SUBMISSION
Submit a link to your code on GitHub to us. Each team can only submit one single time.

# EVALUATION RULE
Based on how many test cases your solution can pass and whether its performance is good or not. We will order the submission based on correctness, performance & submission time.
