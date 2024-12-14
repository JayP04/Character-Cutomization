## Character-Cutomization  --- 510 Project
A program which validates the character customization by using formal langauge and automaton transition rules.




**PUBG Character Customization Language**

**Part 1 - Formal Language Design**

**Intent and Purpose behind project**

This language models the valid paths a user can take while customizing a character during the initial setup phase in the game *Players Unknown BattleGrounds (PUBG)*. The goal is to ensure a structured, stepwise flow through character customization, enforses logical expression and constraints while allowing flexibility such as backtracking. 

The language captures this process, providing a formal structure to represent valid choices and their sequences.

**Structure and Rules of my project**

The customization process starts at the initial state, where users choose a gender, which determines the subsequent path. Each path involves selecting a face type, followed by hair type, and finally hair color. After selecting hair color, the user completes the customization and transitions to the final accepting state, at which point further actions are restricted.

- **Mandatory Selection**: Gender selection (Male or Female) is required to proceed.

- **Sequential Progression**: Users follow a strict sequence: Face → Hair → Hair Color.
- **Backtracking**: Users can backtrack to the previous state but cannot backtrack from the final state.
- **Acceptance**: Only strings that follow the structure and end in the final state are valid.

**Rules**:

I - Users will have to follow a strict sequence of the progression, which is as follows - Face → Hair → Hair Color.

II - NO users will be allowed to go further into the machine if intial steps are not done (i.e. state of choosing gender)

III - For the users to use Backtraking, they should use sign 'B' to procedd.

IV - If the usage of B is done in an invalid/incomplete string, it simply will reject the string.

         i) Users should understand the usage of B from the example strings to ensure correct usage of B. 
        ii) B shall be used multiple times in a string, until unless its not followed by or after a B.
        
V  - Users cannot go further back from the start state for obvious reasons, but user shall also not be able to go back once reached final state (q7). 

VI - Valid are the only strings which obeys the strucuture of the machine and is indeed complete.



**Alphabets in this language**

- **Gender Selection**: `{M, F}`
- **Male Path**:
  - Face: `{MF1, MF2, MF3}`
  - Hair: `{MH1, MH2, MH3, MH4, MH5}`
  - Hair Color: `{HCM1, HCM2, HCM3, HCM4, HCM5}`
- **Female Path**:
  - Face: `{FF1, FF2, FF3}`
  - Hair: `{FH1, FH2, FH3, FH4, FH5}`
  - Hair Color: `{HCF1, HCF2, HCF3, HCF4, HCF5}`
- **Backtracking**: `{B}`



**Examples of Valid Strings**

1. `M MF1 MH3 HCM2` — Male → Face 1 → Hair 3 → Hair Color 2 → Final.
2. `F FF2 FH5 HCF1` — Female → Face 2 → Hair 5 → Hair Color 1 → Final.
3. `M MF3 MH4 B MF1 MH2 HCM5` — Male → Face 3 → Hair 4 → Back → Face 1 → Hair 2 → Hair Color 5 → Final.
4. `F FF1 FH3 B FF3 FH1 HCF4` — Female → Face 1 → Hair 3 → Back → Face 3 → Hair 1 → Hair Color 4 → Final.

---

**Part 2 - Grammar**

The grammar for the PUBG Character Customization Language is defined as follows:

**Start Symbol**: `S`

**Production Rules**:

1. `S → M | F`
2. `M → MF`
3. `MF → MF1 | MF2 | MF3 | MH`
4. `MH → MH1 | MH2 | MH3 | MH4 | MH5 | HCM | B MF`
5. `HCM → HCM1 | HCM2 | HCM3 | HCM4 | HCM5 | B MH`
6. `F → FF`
7. `FF → FF1 | FF2 | FF3 | FH`
8. `FH → FH1 | FH2 | FH3 | FH4 | FH5 | HCF | B FF`
9. `HCF → HCF1 | HCF2 | HCF3 | HCF4 | HCF5 | B FH`
10. `B → λ`

**Explanation**

- `S` represents the start state. - Gender Selection
- `M` and `F` represent male and female pathways, respectively.
- Each pathway branches into sequential choices for face, hair, and hair color.
- Backtracking (`B`) allows transitions to previous states, resetting to earlier stages of the sequence.
- `λ`Lamda allows for optional backtracking or termination of a state sequence.

---

**Part 3- Automaton**

- For the source code see main.tex file. This files contains the latex code of the DFA. You can simply use overleaf to see it. 

But here is the image of that specific code:

![Character Customization Screenshot](Screenshot%202024-12-12%20210040.png)

- I apologise if the screenshot doesnt appear, github has been acting funny. you can also view the structure in the 
files -> DFA.png


---


**Part 4 - Data Structure**

- For the data structure, I have used python to implement the functionality of the machine. You can find the test cases to test the machine in the examples in language (1), and you find the edge cases of the machine in test cases. 

---

**Part 5 - Testing**

- To run this program, I have made it even simpler for anyone to just test it out by using jypter notebook style code. 

- Clone the repository, or copy paste code into existing testing file as this code is just one file it should not a hassle. 

- After cloning, make sure you have python installed and then simply use VSCode to open the ipynb file or the python file (your choice) and then hit the run symbol in either file. 

- Ipynb: you should be seeing an pop up on the top of your VS code and in that input your string to test. It will say rejected if invalid, or will accept it giving accepeted and character details as output. 

- Python file: Since its a simple one python class file, you should be fine running it with the run symbol, if not use the instructions below to run it manually in terminal. 

Here are the steps:

Open the integrated terminal in VS Code by selecting View > Terminal from the menu or by pressing Ctrl+` .
Navigate to the directory containing your Python file using the cd command. For example:

- cd path/to/your/directory/Character-Customization/

Run the Python file by typing:

- python main.py

This will execute the Python script in the terminal.








**Edge Cases**

For the automaton and data structure:

1. **Edge Case 1: Early Backtracking**
   - Input: `M B`
   - Expectation: Rejected as no valid selection has been made.

2. **Edge Case 2: Missing Final State**
   - Input: `F FF2 FH3`
   - Expectation: Rejected as it does not reach the final state.

3. **Edge Case 3: Double Backtracking**
   - Input: `M MF1 MH3 B B`
   - Expectation: Accepted as valid backtracking.

4. **Edge Case 4: Invalid Sequence**
   - Input: `M MF1 MH1 HCF1`
   - Expectation: Rejected as mixing male and female paths is invalid.

5. **Edge Case 5: Final State Backtracking**
   - Input: `F FF3 FH2 HCF4 B`
   - Expectation: Rejected as backtracking from the final state is not allowed.

6. **Edge Case 6: Complete Valid Path**
   - Input: `M MF3 MH4 HCM5`
   - Expectation: Accepted as it follows the valid structure and terminates at the final state.

