# Regular Expression

In this project, I have explored the world of regular expressions while working with Ruby's Oniguruma library.

## Tasks :page_with_curl:

_Note: Each Ruby script in the project operates by matching regular expressions based on an argument supplied via the command line._

* **0. Simply matching School**
  * [0-simply_match_school.rb](./0-simply_match_school.rb): A Ruby script designed to match the regular expression `School`.

* **1. Repetition Token #0**
  * [1-repetition_token_0.rb](./1-repetition_token_0.rb): This Ruby script matches the regular expression `hbn` with 2-5 occurrences of `t` in between `hb` and `n`.

* **2. Repetition Token #1**
  * [2-repetition_token_1.rb](./2-repetition_token_1.rb): A Ruby script that matches the regular expression `hn` with 0 or 1 occurrence of `b` and 0 or 1 occurrence of `t` in between `h` and `n`.

* **3. Repetition Token #2**
  * [3-repetition_token_2.rb](./3-repetition_token_2.rb): This Ruby script matches the regular expression `hbn` with 1 or more occurrences of `t` in between `hb` and `n`.

* **4. Repetition Token #3**
  * [4-repetition_token_3.rb](./4-repetition_token_3.rb): A Ruby script that matches the regular expression `hbn` with 0 or more occurrences of `t` in between `hb` and `n`.

* **5. Not quite HBTN yet**
  * [5-beginning_and_end.rb](./5-beginning_and_end.rb): A Ruby script that matches a regular expression starting with `h` and ending with `n`, with any single character in between.

* **6. Call me maybe**
  * [6-phone_number.rb](./6-phone_number.rb): This Ruby script matches a regular expression representing a 10-digit phone number.

* **7. OMG WHY ARE YOU SHOUTING?**
  * [7-OMG_WHY_ARE_YOU_SHOUTING.rb](./7-OMG_WHY_ARE_YOU_SHOUTING.rb): A Ruby script that matches regular expressions for uppercase letters.

* **8. Textme**
  * [100-textme.rb](./100-textme.rb): A Ruby script for running statistics on TextMe app text message transactions.
  * Output Format: `[SENDER],[RECEIVER],[FLAGS]` where
    * `[SENDER]` represents the sender's phone number or name (including the country code if present).
    * `[RECEIVER]` represents the receiver's phone number or name (including the country code if present).
    * `[FLAGS]` denotes the flags used in the transaction.
