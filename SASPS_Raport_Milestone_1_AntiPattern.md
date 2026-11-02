# RAPORT MILESTONE 1 (SĂPTĂMÂNA 8)
## Analiza Arhitecturii Monolitice și a Anti-Pattern-urilor într-un Sistem de Procesare a Comenzilor

**Universitatea Națională de Știință și Tehnologie POLITEHNICA București**  
**Facultatea de Automatică și Calculatoare**  
**Disciplina:** Stiluri Arhitecturale și Șabloane de Proiectare Software (SASPS)  
**Profesor Titular:** Prof. Dr. Ing. Costin-Anton BOIANGIU  

### Informații Echipă
- **DELICOSTEA Andra-Simona** | Master ABD2 | ID Teams: 125024 | Email: delicosteaandra@gmail.com
- **BARBUCANU Teodor** | Master SAS2 | ID Teams: 125017 | Email: barbuceanuteodor10@gmail.com
- **MAGETZ Radu-Mihai** | Master SAS2 | ID Teams: 125016 | Email: radu.magetz@gmail.com

---

## 1. Introducere și Contextul Proiectului
Proiectul își propune evaluarea riguroasă a impactului modelelor de proiectare comportamentale **Strategy** și **Observer** asupra mentenabilității, extensibilității și scalabilității unui sistem software de procesare a comenzilor într-o platformă de e-commerce.

În cadrul primului Milestone (Săptămâna 8), obiectivul principal constă în proiectarea și implementarea variantei de referință **v1.0 (Monolit Anti-Pattern)**. Această variantă servește drept bază de comparație negativă, ilustrând problemele clasice ce apar în software-ul industrial atunci când se ignoră principiile fundamentale de proiectare orientată pe obiecte (SOLID).

## 2. Metodologia de Analiză și Criteriile de Evaluare
Metodologia adoptată combină analiza statică a codului cu analiza dinamică de performanță. Criteriile de selecție ale sistemului de procesare a comenzilor v1.0 au vizat identificarea celor mai frecvente anti-pattern-uri de proiectare întâlnite în practică:
- **God Object (Blob):** O singură clasă (`MonolithicOrderProcessor`) își asumă responsabilitatea pentru calculul prețurilor, discount-urilor, taxelor de transport, comisioanelor de plată, actualizarea stocurilor, trimiterea de notificări (Email, SMS) și generarea facturilor de audit.
- **Rigid Conditional Logic (Hardcoded Switch/If-Else):** Calculul discount-urilor și al costurilor de livrare este realizat prin ramificații succesive de tip `if-elif-else`, încălcând direct principiul **Open/Closed (OCP)**.
- **Tightly Coupled Observers:** Notificările sunt apelate hardcodat în cadrul metodei de procesare, împiedicând adăugarea sau eliminarea dinamică a canalelor de comunicare.

## 3. Schița Sistemului Monolitic v1.0
Codul sursă v1.0 (disponibil în `milestones/v1_monolith/order_system_v1.py`) încorporează o metodă unică `process_order()` ce execută secvențial:
1. Validarea existenței produselor și a stocului disponibil.
2. Calculul discount-ului printr-un bloc `if-elif-else` cu 6 ramuri distincte.
3. Calculul taxelor de livrare și a comisioanelor de plată prin blocuri condiționale secundare.
4. Scăderea stocului și generarea de alerte directe prin instrucțiuni `print()`.
5. Apelarea directă a logicii de trimitere Email și SMS.
6. Înregistrarea facturii într-o listă internă de audit.

## 4. Evaluarea Inițială a Complexității (Analiză Statică v1.0)
Analiza executată prin parser-ul AST indică o **Complexitate Ciclomatică McCabe de 22** pentru metoda `process_order()`, valoare ce depășește pragul de risc acceptat în ingineria software (recomandat < 10).

| Metrica Evaluată | Valoare Determinată (v1.0 Monolit) | Interpretare Tehnica |
| :--- | :---: | :--- |
| **SLOC (Source Lines of Code)** | 122 | Cod concentrat într-un singur fișier/clasă. |
| **Complexitate Ciclomatică Maxima** | **22** | Metoda `process_order` prezintă risc ridicat de erori. |
| **Număr Clase** | 1 | Coeziune scăzută, cuplare maximă. |
| **Efort de Testare Unitara** | Extrem de Ridicat | Imposibil de testat logica de discount separat de notificări. |

## 5. Planificarea Refactorizării pentru Milestone 2 (Săptămâna 12)
Pentru Milestone 2, sistemul va fi refactorizat după cum urmează:
1. **Izolarea Algoritmilor de Calcul:** Decuplarea calculelor financiare prin definirea interfeței `DiscountStrategy`, `ShippingStrategy` și `PaymentStrategy`.
2. **Decuplarea Notificărilor:** Implementarea interfeței `OrderObserver` și a subiectului `RefactoredOrderProcessor` pentru gestionarea dinamica a abonărilor `attach()` și `detach()`.
