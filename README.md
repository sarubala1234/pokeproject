# 🐱 PokéProject - Django Pokédex System

🔗 **Live Website**:  
👉 [Click here to try PokéProject](https://pokeproject-ag3b.onrender.com)

---

## 📖 Overview
PokéProject is a **Django-based web application** that allows users to register, login, and explore Pokémon data using the PokéAPI.  
It demonstrates **full-stack development** with authentication, API integration, and responsive UI.

---

## ✨ Features

### 👤 User Features
- 🔐 **Register & Login**: Secure authentication system  
- 🔎 **Pokédex Search**: Search any Pokémon by name or ID  
- 📊 **Pokémon Details**: View stats, types, abilities, and images  
- 🗂 **Session Management**: Only logged-in users can access Pokédex  

### 🛠 Tech Stack
- **Backend**: Django, Python  
- **Frontend**: HTML, CSS, Bootstrap  
- **Database**: SQLite (development), PostgreSQL/MySQL (production-ready)  
- **API**: [PokéAPI](https://pokeapi.co/)  

---

## 🚀 Installation (Run Locally)

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# Clone repo
git clone https://github.com/sarubala1234/pokeproject.git
cd pokeproject

# Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
