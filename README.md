# D-Code

D-Code is a hybrid programming environment designed to bridge the gap between visual block-based programming and structured text-based programming.

The project focuses on helping beginner programmers transition from systems such as Scratch to languages such as Python by combining drag-and-drop programming with visible syntax and real programming logic.

---

# Table of Contents

- [Overview](#overview)
- [Goals](#goals)
- [Core Concept](#core-concept)
- [Features](#features)
- [Architecture](#architecture)
- [Language Design](#language-design)
- [Examples](#examples)
- [Current Progress](#current-progress)
- [Planned Features](#planned-features)
- [Design Principles](#design-principles)
- [Project Structure](#project-structure)
- [Development Roadmap](#development-roadmap)
- [Technologies](#technologies)
- [Project Aim](#project-aim)
- [Notes](#notes)

---

# Overview

Many beginner programmers start with visual programming languages such as Scratch or Blockly. These systems make programming accessible by removing syntax requirements and allowing users to drag and connect blocks visually.

However, transitioning from block-based systems to text-based languages such as Python is often difficult because beginners suddenly need to manage:

- Syntax
- Indentation
- Brackets
- Operators
- Variables
- Program structure

D-Code is designed to reduce this difficulty by introducing syntax gradually through structured, editable drag-and-drop blocks.

The system combines:

- Visual interaction
- Structured logic
- Real programming concepts
- Beginner-focused design

---

# Goals

The main goals of D-Code are:

- Help beginners transition into text-based programming
- Teach programming structure visually
- Reduce syntax-related frustration
- Provide immediate visual feedback
- Introduce real programming concepts gradually
- Create a scalable educational programming system

---

# Core Concept

D-Code uses a drag-and-drop interface where each block represents a structured programming instruction.

Instead of directly executing text, the system internally converts blocks into structured data and then into an Abstract Syntax Tree (AST), which is interpreted and executed.

Pipeline:

```text
Blocks (UI)
   ↓
Structured Data
   ↓
Abstract Syntax Tree (AST)
   ↓
Interpreter
   ↓
Output / Feedback
```

This architecture allows the system to separate:

- User interaction
- Program structure
- Program execution

---

# Features

## Core Features

- Drag-and-drop programming interface
- Editable values inside blocks
- Variables and assignment
- Arithmetic operations
- Loops and repetition
- Real-time program execution
- Error handling and validation
- Visual program structure

## Planned Advanced Features

- Step-by-step execution
- Execution highlighting
- Save/load support
- Custom `.dcode` project files
- User-friendly helper system
- Beginner and advanced modes
- Visual execution flow
- Function support

---

# Architecture

## Frontend

The frontend is responsible for:

- Rendering blocks
- Drag-and-drop interactions
- User input
- Visual feedback
- Error highlighting

## Structured Data Layer

Blocks are internally represented as structured objects.

Example:

```python
{
    "type": "repeat",
    "count": 5,
    "body": [...]
}
```

## AST Layer

Programs are converted into an Abstract Syntax Tree.

Example:

```text
RepeatNode
 ├── count: 5
 └── body:
      AssignNode(x, Add(x, 1))
```

The AST allows structured execution and simplifies interpretation.

## Interpreter

The interpreter traverses the AST and executes instructions.

Responsibilities include:

- Variable storage
- Arithmetic evaluation
- Loop execution
- Error checking
- Program flow control

---

# Language Design

D-Code is designed to remain simple while still introducing real programming concepts.

## Planned Commands

### Variable Assignment

```text
set x = 5
```

### Arithmetic

```text
math(add, 5, 2)
```

### Output

```text
say("Hello")
```

### Loops

```text
repeat 5 {
    say("Hi")
}
```

---

# Examples

## Example Program

```text
set x = 0

repeat 5 {
    set x = x + 1
    say(x)
}
```

## Example AST

```text
ProgramNode
 ├── AssignNode(x, 0)
 └── RepeatNode(5)
      ├── AssignNode(x, Add(x, 1))
      └── SayNode(x)
```

---

# Current Progress

## Completed

- Lexer implementation
- Token generation
- Number parsing
- Operator handling
- Whitespace handling
- Parser design
- AST planning
- Core interpreter design

## In Progress

- AST construction
- Interpreter implementation
- Variable system
- Loop system

## Planned

- Drag-and-drop UI
- GUI system
- Error handling system
- File handling
- Save/load support
- Execution visualisation

---

# Planned Features

## Educational Features

- Guided learning mode
- Visual syntax hints
- Beginner explanations
- Interactive feedback

## Technical Features

- AST visualisation
- Runtime diagnostics
- Program validation
- Modular block system

---

# Design Principles

## Separation of Concerns

The project separates:

- UI logic
- Program structure
- Execution logic

This improves maintainability and scalability.

## Beginner Accessibility

The system is designed to:

- Prevent invalid structures
- Reduce syntax frustration
- Encourage experimentation
- Provide immediate feedback

## Extensibility

The architecture is modular, allowing future additions such as:

- Functions
- Conditions
- Custom blocks
- Export systems

---

# Project Structure

```text
D-Code/
│
├── lexer/
├── parser/
├── interpreter/
├── ast/
├── ui/
├── blocks/
├── assets/
├── examples/
├── docs/
│
├── main.py
├── README.md
└── requirements.txt
```

---

# Development Roadmap

## Stage 1 — Calculator System

- Lexer
- Parser
- AST
- Arithmetic execution

## Stage 2 — Variables

- Variable storage
- Assignment
- Access

## Stage 3 — Control Flow

- Repeat loops
- Conditions
- Nested execution

## Stage 4 — GUI

- Block rendering
- Drag-and-drop system
- User interaction

## Stage 5 — Advanced Features

- Save/load
- Visual debugging
- Step execution
- Guidance system

---

# Technologies

Planned technologies include:

- Python
- Tkinter or custom GUI framework
- Object-Oriented Programming
- Recursive Descent Parsing
- Abstract Syntax Trees
- Interpreter-based execution

---

# Project Aim

The aim of D-Code is to create an educational programming environment that makes the transition from visual programming to text-based programming smoother, clearer, and more accessible for beginner programmers.

The system focuses on combining visual interaction with real programming structure to encourage progression into professional programming languages.

---

# Notes

This project is being developed as part of a Computer Science NEA.

The focus of the project is both:

- Technical implementation
- Educational usability

The system is intended to prioritise clarity, scalability, and beginner accessibility while still demonstrating advanced programming concepts internally.