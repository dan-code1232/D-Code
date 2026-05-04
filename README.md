# D-Code

D-Code is a custom programming language built from scratch in Python. It is designed as an educational project to explore how programming languages work internally, including lexical analysis, parsing, and interpretation.

Unlike traditional languages that assume prior knowledge, D-Code is designed to act as a bridge between beginner-friendly visual programming environments (like Scratch) and real-world text-based programming languages (like Python).

---

## Aim

The main aim of D-Code is to bridge the gap between block-based beginner programming and traditional text-based coding. Many learners struggle when transitioning from visual tools like Scratch to real programming languages due to syntax complexity and lack of understanding of how code is actually executed.

D-Code attempts to solve this by providing a simple, readable language that gradually introduces real programming language concepts. It exposes the internal structure of programming languages through a full interpreter pipeline (lexer → parser → AST → interpreter), helping learners understand not just how to code, but how programming languages themselves are built.

The long-term goal is to make programming more intuitive and less intimidating by allowing users to move naturally from simple commands to more advanced concepts without losing clarity.

---

## features

- Custom lexer(tokenises raw source code)
- Recursive Descent Parser
- Abstract Syntax Tree (AST)
- Interpreter-based execution
- Variable assignment and access
- Arithmetic operations (`+`, `-`, `*`, `/`)
- Output using `say`
- Looping with `repeat number  whatever end

---

##example Syntax

x = 5
y = 10

say x + y

repeat 3
    say 'hello'
end