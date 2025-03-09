# 🕹️ The Higher Lower Game

## 📜 Descrierea Proiectului

Acest proiect este un joc interactiv creat cu **Python** și **Pygame**, bazat pe conceptul "Higher Lower". Scopul jocului este de a compara populațiile a două țări și de a ghici dacă a doua țară are o populație mai mare sau mai mică decât prima.

### Caracteristici principale:
- Interfață grafică prietenoasă utilizând **Pygame**.
- Bază de date cu țări și populațiile acestora încărcată dintr-un fișier **Excel**.
- Sistem de scor care salvează cel mai bun rezultat atins.
- Elemente vizuale atractive, inclusiv steagurile țărilor și fundaluri tematice.
- Butoane interactive pentru selecția utilizatorului.

## 📁 Structura Proiectului

Proiectul include următoarele fișiere și directoare:

- `main.py` - Codul sursă principal al jocului.
- `lista_tarilor.xlsx` - Fișierul Excel care conține numele țărilor și populațiile acestora.
- `images/` - Conține imagini utilizate în joc:
  - `lower_higher.png` - Fundal principal al jocului.
  - `poza_fundal.png` - Fundal pentru interfața grafică.
  - `gameover.png` - Imagine afișată la sfârșitul jocului.
  - `tari/` - Folder care conține steagurile țărilor.

## 🔧 Instrucțiuni pentru Utilizare

### 1. **Instalarea Dependențelor**
Asigură-te că ai **Python 3.x** instalat, apoi instalează modulele necesare:
```sh
pip install pygame pandas openpyxl
```

### 2. **Rularea Jocului**
Pentru a porni jocul, rulează următoarea comandă în terminal:
```sh
python main.py
```

### 3. **Cum se joacă**
- Apasă pe butonul **PLAY** pentru a începe jocul.
- Vei vedea două țări afișate cu steagurile și populația primei țări.
- Alege dacă a doua țară are o populație **mai mare** sau **mai mică**.
- Dacă ghicești corect, primești un punct și jocul continuă.
- Dacă greșești, jocul se termină și îți poți vedea scorul.

## 🖼️ Capturi de Ecran

1. **Ecranul principal**
   ![Ecran principal](images/lower_higher.png)

2. **Joc în desfășurare**
   ![Joc](images/poza_fundal.png)

3. **Ecran Game Over**
   ![Game Over](images/gameover.png)

## ⚙️ Cerințe Tehnice

- **Limbaj de programare:** Python 3.x
- **Biblioteci utilizate:**
  - `pygame` - pentru interfața grafică
  - `pandas` - pentru manipularea fișierului Excel
  - `random` - pentru alegerea aleatorie a țărilor
- **Sistem de operare:** Windows, Linux, macOS

## 📌 Funcționalități viitoare
- Adăugarea unui sistem de **leaderboard** pentru a salva scorurile maxime.
- Integrarea unui **timer** pentru a crește dificultatea jocului.
- Posibilitatea de a selecta **moduri de dificultate**.

## 👨‍💻 Autor
- **Nume:** Catalin Voicu
- **Email:** catavoicu01@gmail.com
- Proiect realizat ca parte a cursului: Programarea calculatoarelor și limbaje de programare 3 - Proiect Python.
- **Universitate:** Facultatea de Electronică, Telecomunicații și Tehnologia Informației, Universitatea Politehnica București

---
📌 *Acest proiect este open-source! Orice contribuție este binevenită!* 🚀

