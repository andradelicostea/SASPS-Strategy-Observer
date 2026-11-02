"""
SASPS Project - Milestone 1 (v1.0 Anti-Pattern / Monolith)
Sistem Monolitic de Procesare a Comenzilor (Anti-Pattern: God Object, Hardcoded Switch, Tight Coupling)

Echipa:
- DELICOSTEA Andra-Simona (ABD2, ID: 125024)
- BARBUCANU Teodor (SAS2, ID: 125017)
- MAGETZ Radu-Mihai (SAS2, ID: 125016)
"""

import time
import datetime

class MonolithicOrderProcessor:
    """
    ANTI-PATTERN DEMONSTRATION: 'God Object' + 'Rigid Conditional Logic' + 'Spaghetti Notifications'
    Această clasă concentrează toate responsabilitățile sistemului:
    1. Calculul prețului, discount-ului și taxelor.
    2. Gestionarea stocului și a inventarului.
    3. Notificarea clienților (email, SMS).
    4. Jurnalizarea și generarea facturilor.
    """

    def __init__(self):
        self.inventory = {
            "Laptop Gaming": {"price": 5000.0, "stock": 10},
            "Smartphone 5G": {"price": 3000.0, "stock": 15},
            "Căști Wireless": {"price": 500.0, "stock": 50},
            "Monitor 4K": {"price": 2000.0, "stock": 5}
        }
        self.order_history = []
        self.notification_logs = []

    def process_order(self, customer_name, customer_email, customer_phone, items, discount_type, payment_method, shipping_type):
        """
        Metodă gigantică ce încalcă Single Responsibility Principle (SRP) și Open/Closed Principle (OCP).
        Complexitatea ciclomatică este extrem de ridicată din cauza ramificărilor 'if-elif-else' hardcodate.
        """
        print(f"\n[v1.0 Monolith] Procesare comandă pentru {customer_name}...")
        
        # 1. Calcul subtotal și verificare stoc
        subtotal = 0.0
        for item_name, quantity in items.items():
            if item_name not in self.inventory:
                raise ValueError(f"Produs necunoscut: {item_name}")
            if self.inventory[item_name]["stock"] < quantity:
                raise ValueError(f"Stoc insuficient pentru {item_name}!")
            
            unit_price = self.inventory[item_name]["price"]
            subtotal += unit_price * quantity
            
        # 2. Calcul discount (RIGID IF-ELIF SWITCH - Anti-Pattern Strategy)
        discount_amount = 0.0
        if discount_type == "NONE":
            discount_amount = 0.0
        elif discount_type == "PERCENTAGE_10":
            discount_amount = subtotal * 0.10
        elif discount_type == "PERCENTAGE_20":
            discount_amount = subtotal * 0.20
        elif discount_type == "FIXED_100":
            discount_amount = 100.0 if subtotal >= 100.0 else subtotal
        elif discount_type == "VIP_CUSTOMER":
            if subtotal > 1000:
                discount_amount = subtotal * 0.15 + 50.0
            else:
                discount_amount = subtotal * 0.05
        elif discount_type == "BLACK_FRIDAY":
            discount_amount = subtotal * 0.35
        else:
            print(f"Tip discount necunoscut '{discount_type}', se aplică 0.")
            discount_amount = 0.0

        subtotal_after_discount = max(0.0, subtotal - discount_amount)

        # 3. Calcul taxe și livrare (RIGID SWITCH - Anti-Pattern Strategy)
        shipping_cost = 0.0
        if shipping_type == "STANDARD":
            shipping_cost = 15.0 if subtotal_after_discount < 200 else 0.0
        elif shipping_type == "EXPRESS":
            shipping_cost = 35.0
        elif shipping_type == "SAME_DAY":
            shipping_cost = 60.0
        elif shipping_type == "INTERNATIONAL":
            shipping_cost = 150.0 + subtotal_after_discount * 0.05
        else:
            shipping_cost = 20.0

        # Taxe fixe de procesare plată
        payment_fee = 0.0
        if payment_method == "CARD":
            payment_fee = subtotal_after_discount * 0.01
        elif payment_method == "PAYPAL":
            payment_fee = subtotal_after_discount * 0.025
        elif payment_method == "CASH_ON_DELIVERY":
            payment_fee = 10.0
        elif payment_method == "CRYPTO":
            payment_fee = 5.0

        total_price = subtotal_after_discount + shipping_cost + payment_fee

        # 4. Actualizare stoc
        for item_name, quantity in items.items():
            self.inventory[item_name]["stock"] -= quantity

        # 5. Notificări TIGHTLY COUPLED (Anti-Pattern Observer)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Hardcoded Email Notification
        email_msg = f"[{timestamp}] EMAIL către {customer_email}: Comandă confirmată! Total: {total_price:.2f} RON."
        self.notification_logs.append(email_msg)
        print(email_msg)

        # Hardcoded SMS Notification
        sms_msg = f"[{timestamp}] SMS către {customer_phone}: Comanda dvs. în valoare de {total_price:.2f} RON a fost procesată."
        self.notification_logs.append(sms_msg)
        print(sms_msg)

        # Hardcoded Inventory Alert Notification
        for item_name, info in self.inventory.items():
            if info["stock"] < 3:
                alert = f"[{timestamp}] ALERTA STOC: Produsul '{item_name}' are doar {info['stock']} bucăți în stoc!"
                self.notification_logs.append(alert)
                print(alert)

        # Hardcoded Audit/Invoice Logging
        invoice_record = {
            "timestamp": timestamp,
            "customer": customer_name,
            "items": items,
            "subtotal": subtotal,
            "discount": discount_amount,
            "shipping": shipping_cost,
            "payment_fee": payment_fee,
            "total": total_price,
            "payment_method": payment_method
        }
        self.order_history.append(invoice_record)

        return invoice_record


if __name__ == "__main__":
    processor = MonolithicOrderProcessor()
    order = processor.process_order(
        customer_name="Andra Delicostea",
        customer_email="andra@example.com",
        customer_phone="0712345678",
        items={"Laptop Gaming": 1, "Căști Wireless": 2},
        discount_type="PERCENTAGE_10",
        payment_method="CARD",
        shipping_type="EXPRESS"
    )
    print("\nRezultat comandă monolit:", order)
