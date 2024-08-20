import tkinter as tk
from tkinter import messagebox, ttk


def calculate_buying_costs(property_price, down_payment, mortgage_rate, mortgage_term, property_tax_rate, maintenance_rate, appreciation_rate, years):
    loan_amount = property_price - down_payment
    monthly_mortgage_rate = mortgage_rate / 12 / 100
    number_of_payments = mortgage_term * 12
    monthly_payment = loan_amount * (monthly_mortgage_rate * (1 + monthly_mortgage_rate) ** number_of_payments) / ((1 + monthly_mortgage_rate) ** number_of_payments - 1)
    total_mortgage_paid = monthly_payment * years * 12
    total_property_tax = property_price * (property_tax_rate / 100) * years
    total_maintenance_cost = property_price * (maintenance_rate / 100) * years
    future_property_value = property_price * ((1 + appreciation_rate / 100) ** years)
    total_cost = total_mortgage_paid + total_property_tax + total_maintenance_cost - (future_property_value - property_price)
    return total_cost

def calculate_renting_costs(rent_cost, investment_return_rate, down_payment, years):
    total_rent_paid = rent_cost * 12 * years
    future_investment_value = down_payment * ((1 + investment_return_rate / 100) ** years)
    total_cost = total_rent_paid - future_investment_value
    return total_cost

def calculate():
    try:
        property_price = float(entry_property_price.get())
        down_payment = float(entry_down_payment.get())
        mortgage_rate = float(entry_mortgage_rate.get())
        mortgage_term = int(entry_mortgage_term.get())
        property_tax_rate = float(entry_property_tax_rate.get())
        maintenance_rate = float(entry_maintenance_rate.get())
        appreciation_rate = float(entry_appreciation_rate.get())
        rent_cost = float(entry_rent_cost.get())
        investment_return_rate = float(entry_investment_return_rate.get())
        years = int(entry_years.get())

        buying_cost = calculate_buying_costs(property_price, down_payment, mortgage_rate, mortgage_term, property_tax_rate, maintenance_rate, appreciation_rate, years)
        renting_cost = calculate_renting_costs(rent_cost, investment_return_rate, down_payment, years)

        result_text = f"Total cost of buying over {years} years: ${buying_cost:,.2f}\n"
        result_text += f"Total cost of renting over {years} years: ${renting_cost:,.2f}\n\n"
        if buying_cost < renting_cost:
            result_text += "Buying is a better financial decision."
        else:
            result_text += "Renting is a better financial decision."
        
        result_label.config(text=result_text)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Rent vs Buy Calculator")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10))

input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, padx=10, pady=10)

ttk.Label(input_frame, text="Property Price ($):").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_property_price = ttk.Entry(input_frame, width=20)
entry_property_price.grid(row=0, column=1, pady=5)

ttk.Label(input_frame, text="Down Payment ($):").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_down_payment = ttk.Entry(input_frame, width=20)
entry_down_payment.grid(row=1, column=1, pady=5)

ttk.Label(input_frame, text="Mortgage Rate (%):").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_mortgage_rate = ttk.Entry(input_frame, width=20)
entry_mortgage_rate.grid(row=2, column=1, pady=5)

ttk.Label(input_frame, text="Mortgage Term (years):").grid(row=3, column=0, sticky=tk.W, pady=5)
entry_mortgage_term = ttk.Entry(input_frame, width=20)
entry_mortgage_term.grid(row=3, column=1, pady=5)

ttk.Label(input_frame, text="Property Tax Rate (%):").grid(row=4, column=0, sticky=tk.W, pady=5)
entry_property_tax_rate = ttk.Entry(input_frame, width=20)
entry_property_tax_rate.grid(row=4, column=1, pady=5)

ttk.Label(input_frame, text="Maintenance Cost Rate (%):").grid(row=5, column=0, sticky=tk.W, pady=5)
entry_maintenance_rate = ttk.Entry(input_frame, width=20)
entry_maintenance_rate.grid(row=5, column=1, pady=5)

ttk.Label(input_frame, text="Appreciation Rate (%):").grid(row=6, column=0, sticky=tk.W, pady=5)
entry_appreciation_rate = ttk.Entry(input_frame, width=20)
entry_appreciation_rate.grid(row=6, column=1, pady=5)

ttk.Label(input_frame, text="Monthly Rent ($):").grid(row=7, column=0, sticky=tk.W, pady=5)
entry_rent_cost = ttk.Entry(input_frame, width=20)
entry_rent_cost.grid(row=7, column=1, pady=5)

ttk.Label(input_frame, text="Investment Return Rate (%):").grid(row=8, column=0, sticky=tk.W, pady=5)
entry_investment_return_rate = ttk.Entry(input_frame, width=20)
entry_investment_return_rate.grid(row=8, column=1, pady=5)

ttk.Label(input_frame, text="Years to Stay:").grid(row=9, column=0, sticky=tk.W, pady=5)
entry_years = ttk.Entry(input_frame, width=20)
entry_years.grid(row=9, column=1, pady=5)

calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate)
calculate_button.grid(row=10, column=0, columnspan=2, pady=10)

result_frame = ttk.Frame(root, padding="10")
result_frame.grid(row=1, column=0, padx=10, pady=10)

result_label = ttk.Label(result_frame, text="", justify=tk.LEFT, font=("Arial", 12, "bold"))
result_label.grid(row=0, column=0)

root.mainloop()
