def algorithm_luhn(card_number: str) -> bool:
    card_numbers = list(map(int, card_number))
    card_numbers = card_numbers[::-1]
    for i in range(1, len(card_numbers), 2):
        card_numbers[i] *= 2
        if card_numbers[i] > 9:
            card_numbers[i] = card_numbers[i] % 10 + card_numbers[i] // 10
    return sum(card_numbers) % 10 == 0