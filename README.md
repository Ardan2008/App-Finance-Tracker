# 💰 WebApp Finance Tracker

## 🧭 Project Description
**WebApp Finance Tracker** is a **Python Flask-based web application** designed to record, manage, and monitor personal finances easily and efficiently.  
The app features a **modern and responsive interface** built with **HTML, CSS, and Bootstrap**, and stores all transaction data **locally in a `data.json` file** — no external database required.

With a simple yet elegant system, users can add, view, and analyze their income and expenses in real time through a clean and professional web interface.

---

## 🌟 Key Features
- **Quick Transaction Recording**  
  Easily add income and expenses with flexible descriptions and amounts.  
- **Automatic Financial Summary**  
  Instantly view total balance with indicators showing financial health (safe, deficit, etc.).  
- **Local JSON Data Storage**  
  All transactions are stored in `data.json` for easy access and modification.  
- **Modern & Responsive Design**  
  Styled with *glassmorphism* and *gradient themes* for a sleek, elegant appearance.  
- **Database-Free Operation**  
  Lightweight, fast, and simple to run on any local environment.  

---

## 📂 Project Structure

| Folder / File           | Description |
|--------------------------|-------------|
| `.venv/`                 | Virtual environment for local Python dependencies. |
| `.vscode/`               | VS Code editor configuration folder (optional). |
| `static/`                | Contains static files such as CSS, JS, and images. |
| └── `style.css`          | Main stylesheet for the web app’s interface. |
| `templates/`             | Contains HTML templates used by the Flask framework. |
| ├── `base.html`          | Base layout template for consistent page design. |
| └── `index.html`         | Main page that displays the list of transactions. |
| `app.py`                 | The main Flask application file that handles routing and logic. |
| `data.json`              | JSON file used for storing transaction data locally. |

---

> 💡 **Note:**  
> This project structure is organized to ensure a clean separation between backend logic, frontend design, and local data storage, making the Flask app easy to maintain and extend.
