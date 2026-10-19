# SASPS-Strategy-Observer

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

