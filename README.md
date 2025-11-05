# D0031N – REST Web Services med GUI (Flask + GitHub)

Detta projekt är en prototyp för **registrering av studieresultat**.  
Syftet är att visa hur flera REST-baserade webbtjänster (Epok, StudentITS och Ladok)  
kan integreras med ett webbaserat gränssnitt byggt i **Flask (Python)**.

---

## 🚀 Funktionalitet

Systemet består av fyra delar:

| Del | Beskrivning |
|-----|--------------|
| **Epok** | Tillhandahåller moduler för en kurs via `/epok/modul/<kurskod>` |
| **StudentITS** | Returnerar personnummer för en student via `/studentits/personnummer/<anvnamn>` |
| **Ladok** | Tar emot och sparar resultat via `POST /ladok/resultat` |
| **GUI (Frontend)** | Ett webbaserat gränssnitt där läraren kan registrera resultat |

---

## 🧱 Projektstruktur

D0031N/
│
├── app.py # Huvudfilen som startar Flask-servern
│
├── services/ # REST-tjänster
│ ├── epok_service.py
│ ├── studentits_service.py
│ └── ladok_service.py
│
├── templates/ # HTML-filer (frontend)
│ └── index.html
│
├── static/ # CSS och ev. JavaScript
│ └── style.css
│
├── data/ # Simulerad databas (JSON-filer)
│ ├── moduler.json
│ ├── studenter.json
│ └── resultat.json
│
└── requirements.txt # Lista med Python-bibliotek

---

## 🧩 Installation (för hela gruppen)

### 1️⃣ Klona projektet
```bash
git clone https://github.com/Olle-88/D0031N.git
cd D0031N

python -m venv venv
venv\Scripts\activate      # På Windows
source venv/bin/activate   # På Mac/Linux

pip install -r requirements.txt
python app.py

Öppna sedan webbläsaren och gå till:
👉 http://127.0.0.1:5000


Grupparbete & Branch-struktur

Varje delsystem utvecklas i sin egen branch:

Branch	Ansvar
gui-bas	Flask-grund & GUI
epok-service	API för kursmoduler
studentits-service	API för personnummer
ladok-service	API för resultatregistrering
Workflow:

Skapa ny branch:

git checkout -b <branch-namn>


Lägg till och committa dina ändringar:

git add .
git commit -m "Beskrivning av ändring"


Ladda upp till GitHub:

git push origin <branch-namn>


Skapa sedan en Pull Request på GitHub för att mergea till main.
