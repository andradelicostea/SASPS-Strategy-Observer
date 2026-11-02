# SASPS - Milestone 1: Arhitectura Inițială și Identificarea Anti-Pattern-urilor (Săptămâna 8)

**Membri Echipă:**
- **DELICOSTEA Andra-Simona** | Grupa ABD2 | delicosteaandra@gmail.com | ID Teams: 125024
- **BARBUCANU Teodor** | Grupa SAS2 | barbuceanuteodor10@gmail.com | ID Teams: 125017
- **MAGETZ Radu-Mihai** | Grupa SAS2 | radu.magetz@gmail.com | ID Teams: 125016

---


# Studiu comparativ: Strategy și Observer

## Descriere

Acest proiect analizează comparativ impactul modelelor de proiectare **Strategy** și **Observer** asupra mentenabilității, extensibilității și testabilității unei aplicații software.

Aplicația este un sistem simplificat de procesare a comenzilor. Aceasta permite plasarea unei comenzi, selectarea unei metode de plată și trimiterea unor notificări simulate. Comparăm o implementare directă, bazată pe condiții și componente strâns legate, cu o implementare care folosește modelele Strategy și Observer.

Proiectul urmărește să evidențieze atât avantajele modelelor, cât și situațiile în care acestea pot adăuga complexitate inutilă.

## Obiective

- Prezentarea modelelor de proiectare Strategy și Observer.
- Compararea implementării directe cu cea bazată pe modele.
- Evaluarea ușurinței de adăugare a unor funcționalități noi.
- Analizarea mentenabilității, extensibilității și testabilității codului.
- Compararea rezultatelor testelor și, opțional, a performanței.

## Modele și abordări analizate

### Strategy

Strategy permite definirea unor comportamente alternative și selectarea lor fără modificarea codului care le utilizează.

În proiect, modelul este folosit pentru metode de plată simulate, precum plata cu cardul sau plata la livrare.

**Comparație:** selectarea metodei de plată prin condiții `if/switch` versus folosirea unor strategii separate.

### Observer

Observer permite notificarea componentelor interesate atunci când are loc un eveniment.

În proiect, modelul este folosit pentru a trimite notificări simulate după plasarea unei comenzi, de exemplu prin e-mail sau SMS.

**Comparație:** apelarea directă a serviciilor de notificare versus notificarea observatorilor abonați la eveniment.

## Funcționalități

- Plasarea unei comenzi.
- Selectarea și simularea unei metode de plată.
- Trimiterea notificărilor după plasarea comenzii.
- Implementarea unei variante fără modele de proiectare.
- Implementarea unei variante cu Strategy și Observer.
- Testarea și compararea celor două variante.

> Plățile și notificările sunt simulate. Aplicația nu procesează tranzacții reale și nu trimite mesaje către servicii externe.

## Tehnologii

- **Python 3.10+**
- **FastAPI** – pentru API-ul aplicației
- **Uvicorn** – pentru rularea serverului
- **pytest** – pentru testele automate
- **Git și GitHub** – pentru versionarea codului

Metodologie de evaluare
Cele două variante sunt comparate folosind aceleași cerințe funcționale. Evaluarea poate include:

- numărul de clase și fișiere modificate pentru o funcționalitate nouă;
- ușurința adăugării unei metode de plată sau a unui canal de notificare;
- complexitatea și cuplarea codului;
- testabilitatea și rezultatele testelor;
- timpul de răspuns și consumul de resurse, dacă sunt realizate teste de performanță.



##  Obiectivul Milestone-ului 1
Milestone-ul 1 este dedicat analizei variantei **monolitice inițiale** a sistemului de procesare a comenzilor (`order_system_v1.py`). Scopul principal este identificarea problemelor arhitecturale, a antipattern-urilor de proiectare și evaluarea inițială a complexității codului înainte de refactorizare.

---

##  Structura Fișierelor din Milestone 1

| Nume Fișier | Tip | Descriere |
| :--- | :--- | :--- |
| `order_system_v1.py` | Cod Sursă Python | Implementarea monolitică de la care se pornește. |
| `SASPS_Raport_Milestone_1_AntiPattern.docx` | Document Word | Raportul scris oficial pentru Milestone 1 (Săptămâna 8). |
| `SASPS_Raport_Milestone_1_AntiPattern.md` | Document Markdown | Versiunea text/markdown a raportului pentru Săptămâna 8. |

---

##  Anti-Pattern-uri Identificate în v1.0

1. **God Object (Clasă Gigant)**:
   - Clasa `MonolithicOrderProcessor` concentrează toate responsabilitățile sistemului: validare, calcul discount, calcul transport, procesare plată, gestiune stocuri și trimitere de notificări Email/SMS.
   - Violarea directă a principiului **Single Responsibility Principle (SRP)**.

2. **Hardcoded Notification Logic (Cuplare Strânsă)**:
   - Trimiterea mesajelor de confirmare prin Email și SMS este hardcodată direct în metoda de procesare.
   - Imposibilitatea adăugării de noi canale de notificare (ex: WhatsApp, Push Notifications) fără modificarea codului sursă.

3. **Rigid Conditional Switch (Violare Open/Closed Principle - OCP)**:
   - Calculul discount-urilor și al taxelor de transport se bazează pe instrucțiuni `if-elif-else` lungi și rigide.
   - Orice tip nou de discount (ex: campanie de Black Friday) necesită modificarea metodei monolitice, crescând riscul de regresie și introducere de bug-uri.

---

## Metrici Evaluat în Milestone 1
- **Complexitate Ciclomatică Maxima (McCabe)**: **22** (în metoda `process_order`).
- **Complexitate Ciclomatică Medie**: **11.5**.
- **Grad de Cuplare**: Extrem de ridicat (Tight Coupling).
- **Testabilitate**: Scăzută (necesită mock-uri complexe sau procesarea întregului flux pentru un simplu calcul).

---

## Instrucțiuni de Rulare în PyCharm / Terminal

### Cerințe:
- Python 3.10+ installed.

### Execuție:
1. Deschideți proiectul în **PyCharm**.
2. Rulați fișierul `order_system_v1.py`:
   ```bash
   python order_system_v1.py
   ```
3. În consolă se va afișa simularea procesării comenzii prin sistemul monolitic, evidențiind modul în care notificările și calculele sunt executate secvențial și rigid.
