"""Separate module containing the dummy restaurant menu data."""
"""Separate module containing the dummy restaurant menu data.

Menu format (top-level `MENU`):

- `restaurant`: string
- `recommendations`: list of recommended item ids
- `menu`: object with category keys. Each category (except `Desserts`) has
  `veg` and `non_veg` lists. `Desserts` is a standalone list.
"""

MENU = [
    {
        "category": "Starters",
        "items": [
            {
                "id": 1,
                "name": "Garlic Bread",
                "price": 4.5,
                "description": "Toasted baguette slices with garlic butter and parsley.",
                "type": "starter",
                "diet": "veg",
                "spice_level": "mild",
                "recommended": False,
            },
            {
                "id": 2,
                "name": "Bruschetta",
                "price": 5.0,
                "description": "Grilled bread topped with tomato, basil, and olive oil.",
                "type": "starter",
                "diet": "veg",
                "spice_level": "mild",
                "recommended": False,
            },
            {
                "id": 3,
                "name": "Chicken Wings",
                "price": 7.5,
                "description": "Crispy wings tossed in a tangy BBQ sauce.",
                "type": "starter",
                "diet": "nonveg",
                "spice_level": "medium",
                "recommended": True,
            },
        ],
    },
    {
        "category": "Mains",
        "items": [
            {
                "id": 4,
                "name": "Margherita Pizza",
                "price": 11.0,
                "description": "Classic pizza with fresh tomato, mozzarella and basil.",
                "type": "main",
                "diet": "veg",
                "spice_level": "mild",
                "recommended": False,
            },
            {
                "id": 5,
                "name": "Penne Arrabbiata",
                "price": 10.5,
                "description": "Pasta in a spicy tomato sauce with garlic and chillies.",
                "type": "main",
                "diet": "veg",
                "spice_level": "hot",
                "recommended": True,
            },
            {
                "id": 6,
                "name": "Pasta Carbonara",
                "price": 12.5,
                "description": "Pasta with pancetta, egg, and pecorino cheese.",
                "type": "main",
                "diet": "egg",
                "spice_level": "mild",
                "recommended": False,
            },
            {
                "id": 7,
                "name": "Grilled Salmon",
                "price": 14.0,
                "description": "Pan-seared salmon with lemon butter and seasonal veg.",
                "type": "main",
                "diet": "nonveg",
                "spice_level": "mild",
                "recommended": True,
            },
        ],
    },
    {
        "category": "Desserts",
        "items": [
            {
                "id": 8,
                "name": "Tiramisu",
                "price": 6.0,
                "description": "Coffee-soaked ladyfingers layered with mascarpone cream.",
                "type": "dessert",
                "diet": "veg",
                "spice_level": "none",
                "recommended": False,
            },
            {
                "id": 9,
                "name": "Panna Cotta",
                "price": 5.5,
                "description": "Silky vanilla panna cotta topped with berry compote.",
                "type": "dessert",
                "diet": "veg",
                "spice_level": "none",
                "recommended": False,
            },
        ],
    },
    {
        "category": "Drinks",
        "items": [
            {
                "id": 10,
                "name": "Classic Mojito",
                "price": 7.5,
                "description": "White rum, fresh lime, mint, sugar and soda — bright and refreshing.",
                "type": "cocktail",
                "diet": "veg",
                "alcoholic": True,
                "spice_level": "none",
                "recommended": True,
            },
            {
                "id": 11,
                "name": "Spicy Mango Margarita",
                "price": 8.0,
                "description": "Tequila, mango purée and lime with a chili-salt rim for a spicy kick.",
                "type": "cocktail",
                "diet": "veg",
                "alcoholic": True,
                "spice_level": "medium",
                "recommended": False,
            },
            {
                "id": 12,
                "name": "Virgin Pina Colada",
                "price": 5.5,
                "description": "Pineapple juice, coconut cream and crushed ice — tropical and alcohol-free.",
                "type": "mocktail",
                "diet": "veg",
                "alcoholic": False,
                "spice_level": "none",
                "recommended": False,
            },
            {
                "id": 13,
                "name": "Ginger Lemon Fizz",
                "price": 4.5,
                "description": "Sparkling water with fresh lemon and ginger syrup — light and zesty.",
                "type": "mocktail",
                "diet": "veg",
                "alcoholic": False,
                "spice_level": "mild",
                "recommended": True,
            },
        ],
    },
]
