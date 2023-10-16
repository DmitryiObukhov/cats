cats = [False] * 100

for round in range(1, 101):
    for cat_number in range(round - 1, 100, round):
        cats[cat_number] = not cats[cat_number]

cats_with_hats = [i + 1 for i, has_hat in enumerate(cats) if has_hat]
cats_without_hats = [i + 1 for i, has_hat in enumerate(cats) if not has_hat]

print("Cats with hats:", cats_with_hats)
print("Cats without hats:", cats_without_hats)
