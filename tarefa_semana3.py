def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price



price = float(input("Digite o preço original do item: "))
discount_percent = float(input("Digite a porcentagem de desconto: "))


final_price = calculate_discount(price, discount_percent)


if discount_percent >= 20:
    print(f"Desconto aplicado! O preço final é: {final_price:.2f}")
else:
    print(f"Nenhum desconto aplicado. O preço original é: {final_price:.2f}")
