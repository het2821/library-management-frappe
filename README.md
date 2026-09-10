### Library Management

Library Management System built with frappe

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch version-16
bench install-app library_management
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade
### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit

# Library Management System - Frappe

A complete Library Management System built using the Frappe Framework v16.

## Features

### 📚 Book Management
- Book categories
- Book authors
- Book inventory
- Total and available copies
- Shelf location
- Active/inactive books

### 👥 Member Management
- Library member registration
- Membership types
- Membership status
- Membership expiry
- User-linked member profiles

### 📕 Book Issue
- Automatic issue date
- Automatic due date
- Book availability validation
- Duplicate issue prevention
- Automatic available-copy reduction
- Issue cancellation support

### 📗 Book Return
- Automatic member/book details
- Late-day calculation
- Automatic fine calculation
- Fine status management
- Automatic available-copy increase
- Automatic issue status update

### 📊 Dashboard
- Total Books
- Available Books
- Issued Books
- Overdue Books
- Total Members
- Pending Fines

### 📑 Reports
- Book Inventory Report
- Issued Books Report
- Overdue Books Report
- Fine Report

### 🔐 Security
- Administrator role
- Librarian role
- Library Member role
- User-specific Library Member access
- User-specific Book Issue access
- User-specific Book Return access

### 🚀 REST APIs

Available APIs:

```text
/api/method/library_management.api.get_library_summary
/api/method/library_management.api.get_available_books
/api/method/library_management.api.get_member_issued_books

Technology Stack
- Frappe Framework v16
- Python
- MariaDB
- JavaScript
- HTML/CSS
- REST API
Project Structure
library_management/
├── library_management/
│   ├── doctype/
│   │   ├── book_author/
│   │   ├── book_category/
│   │   ├── library_book/
│   │   ├── library_member/
│   │   ├── book_issue/
│   │   └── book_return/
│   ├── report/
│   ├── api.py
│   └── hooks.py
├── .github/
├── README.md
└── pyproject.toml
Installation
Create a Frappe v16 bench and get the application:
bench get-app https://github.com/het2821/library-management-frappe.git --branch version-16
Install it on your site:
bench --site your-site.local install-app library_management
Run migration:
bench --site your-site.local migrate
Clear cache:
bench --site your-site.local clear-cache
Start the bench:
bench start
Developer
Het Thakkar
B.Tech in Artificial Intelligence & Machine Learning
License
MIT

Save:

```text
Ctrl + O
Enter
Ctrl + X
