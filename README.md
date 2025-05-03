# DealVault  
A community-powered platform to share and discover the best local deals—across retail, grocery, dining, and more.

**Visit the Live Site** - https://dealvault-qoi9.onrender.com/ 

---

## Overview

**DealVault** enables users to:
- Post and browse local deals
- Like and explore the most popular offers
- Filter deals by category
- View insightful visualizations on trends
- Seamlessly register/login and manage profiles

Built with Flask and PostgreSQL, DealVault is a full-stack web application focused on community-driven savings and insights.

---

## Features

- **User Authentication**: Register and login securely
- **Deal Posting**: Add deals with details like store name, category, promo code, and description
- **Likes System**: Like deals, see most liked ones
- **Visualizations**: Explore insights with charts on category distribution, top stores, and more
- **Filtering**: Search and filter deals by store, category, or keywords

---

## Tech Stack

- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: HTML, Jinja2, Bootstrap
- **Auth**: Flask-Login, Flask-WTF
- **Visualizations**: Matplotlib, Seaborn
- **Hosting**: Render (Backend) + Railway (PostgreSQL DB)

---

## Directory Structure

```
DealVault/
│
├── app/                # Flask application package
│   ├── auth/           # Authentication blueprint
│   ├── main/           # Main routes (deals, dashboard, etc.)
│   ├── models.py       # SQLAlchemy models
│   ├── forms.py        # WTForms definitions
│   ├── templates/      # Jinja2 HTML templates
│   └── static/         # CSS, JS, images
│
├── .env                # Environment variables (not committed)
├── run.py              # Entry point for local dev
├── wsgi.py             # WSGI entry for production (Render)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/dealvault.git
   cd dealvault
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_postgres_connection_string
   ```

4. **Run the app**
   ```bash
   python run.py
   ```

---

## Deployment

- Backend hosted on **Render**
- PostgreSQL database on **Railway**
- Push to GitHub triggers auto-deploy via Render Git integration

---

## Future Improvements

- Integrating admin functionalities and dashboard for moderation
- Integrating Referral Postings 
