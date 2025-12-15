# Murphy Bank – Console Banking System
**CSC 221 – Intro to Problem Solving & Programming Final Project**

A "full-featured" text-based banking application built entirely in Python with clean, modular, production-quality code.

## Features
- Create unlimited bank accounts with unique owner names and passwords
- Secure login with case-insensitive username matching
- Deposit, withdraw, and check balance with perfect decimal precision (`Decimal`)
- Transfer funds between any two existing accounts
- Pretty currency formatting ($1,234.56) and comma support on input
- "n" to cancel at any prompt – real UX polish
- Clean separation of concerns across five modules:
  - `bank_account.py` – core account logic
  - `screens.py`      – all menus and user flow
  - `accounts.py`     – global account registry
  - `utils.py`        – console helpers
  - `main.py`         – proper entry point
- Hierarchical control flow using `return` instead of trampoline calls (no deep call stacks)
- Type hints and detailed docstrings throughout
- No use of `float` for money – `Decimal` used everywhere for exact arithmetic

## How to Run
```bash
python main.py