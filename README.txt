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


### Test Accounts

These are pre-defined test accounts for development and testing (login, transfers, multi-account features, etc.).

| First Name | Last Name | Username     | Email                     | Password       | Notes / Suggested Accounts to Create                  |
|------------|-----------|--------------|---------------------------|----------------|-------------------------------------------------------|
| John       | Doe       | johndoe      | john.doe@example.com      | Password123    | Primary test user – create Checking + Savings         |
| Jane       | Smith     | janesmith    | jane.smith@example.com    | SecurePass2025 | Second user for inter-user transfers – create Checking|
| Alex       | Rivera    | alexrivera   | alex.rivera@example.com   | MyBankTest!    | Create multiple Checking accounts for same-user testing |
| Maria      | Garcia    | mariagarcia  | maria.g@example.com       | Garcia2025     | Good for testing email uniqueness                     |
| Robert     | Chen      | robchen      | robert.chen@example.com   | ChenPass123    | Create a Credit account for variety                   |
| Emily      | Taylor    | emilyt       | emily.taylor@example.com  | Taylor!2025    | Backup user for edge-case logins                      |
| Michael    | Brown     | mbrown       | michael.brown@example.com | BrownSecure    | Use for failed login tests (wrong password attempts)  |
| Sarah      | Wilson    | sarahw       | sarah.wilson@example.com  | WilsonPass99   | Extra user for testing many accounts                  |

#### Tips for Using These Accounts
- Create **John Doe** and **Jane Smith** first — ideal for testing transfers between different users.
- Give **Alex Rivera** 2–3 Checking accounts to test handling multiple accounts of the same type.
- All passwords meet the ≥8 character requirement and pass basic validation.
- Use **Michael Brown** when deliberately testing failed login attempts.
