movie = input()
packet = input()
ticket_count = int(input())

if movie == "John Wick":
    if packet == "Drink":
        ticket_price = 12
    elif packet == "Popcorn":
        ticket_price = 15
    elif packet == "Menu":
        ticket_price = 19
elif movie == "Star Wars":
    if packet == "Drink":
        ticket_price = 18
    elif packet == "Popcorn":
        ticket_price = 25
    elif packet == "Menu":
        ticket_price = 30
elif movie == "Jumanji":
    if packet == "Drink":
        ticket_price = 9
    elif packet == "Popcorn":
        ticket_price = 11
    elif packet == "Menu":
        ticket_price = 14

price = ticket_price * ticket_count

if movie == "Star Wars":
    if ticket_count >= 4:
        price *= 0.7

if movie == "Jumanji":
    if ticket_count == 2:
        price *= 0.85

print(f"Your bill is {price:.2f} leva.")




