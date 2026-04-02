# Rabbit Manager Dashboard

Rabbit Manager Dashboard is a powerful desktop application designed to simplify and optimize rabbit farm management. Built with Python and PySide6, it provides an all-in-one solution for tracking rabbits, managing customers, handling invoices, and visualizing breeding data.

---

## Description

Manage your rabbit farm with ease using **Rabbit Manager Dashboard**.  
This application centralizes all farm operations, allowing you to track rabbits, monitor breeding history, manage customers, generate invoices, and analyze your farm performance through an intuitive and modern interface.

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
git clone https://github.com/YOUR-USERNAME/Rabbit-Manager-Dashboard.git
cd Rabbit-Manager-Dashboard
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
