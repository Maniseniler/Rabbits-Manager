# Rabbit Manager Dashboard

Rabbit Manager Dashboard is a powerful desktop application designed to simplify and optimize rabbit farm management. Built with Python and PySide6, it provides an all-in-one solution for tracking rabbits, managing customers, handling invoices, and visualizing breeding data.

---

## Description

Manage your rabbit farm with ease using **Rabbit Manager Dashboard**.  
This application centralizes all farm operations, allowing you to track rabbits, monitor breeding history, manage customers, generate invoices, and analyze your farm performance through an intuitive and modern interface.
<img width="1605" height="1110" alt="image" src="https://github.com/user-attachments/assets/c52ffe87-84bd-4c6c-bfdd-e1d58e21218a" />

[![Watch Demo]](https://www.youtube.com/watch?v=abc123XYZ)

---

## Key Features

* 🐇 **Rabbit Management** – Store detailed information about each rabbit (breed, gender, birth date, health, etc.).
* 🌳 **Family Tree Visualization** – Automatically generate and explore rabbit lineage.
* 👥 **Customer Management** – Track customers, purchases, and contact details.
* 🧾 **Invoice System** – Create and manage invoices for every sale.
* 🔍 **Smart Search & Filtering** – Quickly find rabbits, cages, or customers.
* 🏠 **Cage Management** – Organize rabbits by cages efficiently.
* 📊 **Dashboard Analytics** – View statistics like profits, sales, and farm status.
* 💰 **Expenses Tracking** – Monitor farm costs and earnings.
* 📁 **Export Tools** – Export data to Excel and PDF.
* 🖼️ **Image Management** – Store and display rabbit and customer images.

---

## Tech Stack

- **Language:** Python
- **Framework:** PySide6 (Qt for Python)
- **Database:** SQLite
- **Libraries:**
  - pandas
  - reportlab
  - PyMuPDF
  - pyotp

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/Rabbit-Manager.git
cd Rabbit-Manager
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Requirements
Windows OS (recommended)
Python 3.10+

## Security Notes
This application includes:
  Local database storage (SQLite)
  File storage in system directories (APPDATA)
  Optional security features like hardware ID verification and 2FA
