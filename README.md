# Secure Notes Manager

A secure, category-based notes application built using **Python Tkinter**, featuring **AES-encrypted note storage**, **password authentication**, and **dynamic light/dark themes**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![GUI](https://img.shields.io/badge/Tkinter-GUI-lightgrey)
![Encryption](https://img.shields.io/badge/Encryption-AES-green)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🚀 Features

* 🔐 Password-protected access
* 🔒 AES encryption for notes and credentials
* 🗂️ Category-based note filtering
* 🌃 Toggle between Dark and Light UI themes
* 📝 Create, Edit, Delete notes securely
* 📀 SQLite3-based local storage

---

## 🗂️ Project Structure

```
SecureNotes/
├── main.py           # Main GUI logic
├── dbfile.py         # Database (SQLite3) interaction logic
├── Encryption.py     # Encryption & decryption utilities
├── README.md         # This documentation
└── user.db           # SQLite database (auto-generated)
```

---

## 🔤️ GUI Layout

* **Login Screen**: Password input for access.
* **Dashboard**:

  * `Top Bar`: Navigation (Home | Add Note | Settings | Logout)
  * `Sidebar`: Dynamic categories list
  * `Main Area`:

    * `h1frame`: Note list (Treeview)
    * `h2frame`: Note view/edit
    * `h3frame`: Add category
    * `nframe`: Add note
    * `sframe`: Settings
    * `cpframe`: Change password
    * `lframe`: Logout screen

---

## ⚙️ Core Functionalities

### 🔐 Authentication

* `pw_check()`: Verifies user password by comparing against encrypted DB hash.
* `change_pass()`: Securely updates password using encryption.

### 📝 Notes Management

* `addnotes()`, `save_note()`, `edit_note()`, `delete_note()`
* `filter_notes(cat)`: Filters notes by category
* `on_select(event)`: Displays selected note's decrypted content

### 🗂️ Category Management

* Dynamically generated from the database
* `add_cat()`: Add new category & corresponding DB table

### 🎨 Theme Support

* `theme1()`: Dark mode (charcoal + turquoise)
* `theme2()`: Light mode (system defaults)
* `change_theme()`: Toggle function

### ⚙️ Settings & Navigation

* Easy navigation via top bar and sidebar
* Change password, logout, and return to home with one click

---

## 🔐 Data Flow

```text
[Login] -> [Dashboard]
    ↓
[Notes Encrypted] ↔ [SQLite DB]
    ↓
[Categories & Filtering]
    ↓
[Settings: Theme | Password Change]
```

---

## 💠 Tech Stack

| Component         | Description                                          |
| ----------------- | ---------------------------------------------------- |
| Python            | 3.8+                                                 |
| Tkinter           | GUI framework (standard with Python)                 |
| SQLite3           | Embedded DB for note storage                         |
| Custom Encryption | AES-based encryption using `cryptography` or similar |

---

## 📦 Requirements

Install Python dependencies (if encryption uses external library):

```bash
pip install cryptography
```

> ⚠️ Tkinter and SQLite3 are built into Python.

---

## 🧠 Future Enhancements

* 🔍 Add search bar
* ☁️ Enable cloud sync (Firebase/Drive)
* 📄 Markdown support in note editor
* 👥 Multi-user login support

---

## 📁 Notes on Dependencies

Ensure the following modules are present in your project:

* [`dbfile.py`](./dbfile.py): Handles DB creation, data CRUD, password storage.
* [`Encryption.py`](./Encryption.py): Encrypts/decrypts notes and credentials using a secure cipher.

If you'd like, share those files and I’ll add full schema and encryption walkthroughs here.

---

## 👤 Author

**Developed by [HR Clasher](#)**
🔗 Feel free to fork, modify, or contribute!

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
