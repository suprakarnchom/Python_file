def make_coffee(water, coffee_powder, milk=None, sugar=None):
    # Step 1: Boil water
    water = boil_water(water)

    # Step 2: Add coffee to cup
    cup = add_coffee(coffee_powder)

    # Step 3: Pour boiled water into cup
    cup = pour_water(cup, water)

    # Step 4: Stir the coffee
    cup = stir_coffee(cup)

    # Step 5: Check if milk or sugar is required
    if milk:
        # Step 5a: Add milk
        cup = add_milk(cup, milk)
    if sugar:
        # Step 5b: Add sugar
        cup = add_sugar(cup, sugar)

    # Step 6: Stir the coffee again
    cup = stir_coffee(cup)

    # Step 7: Serve the coffee
    return serve_coffee(cup)

make_coffee(1, 1, 1, 1) # psuedo code