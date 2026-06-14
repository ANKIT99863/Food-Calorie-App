
import sqlite3
import database

def get_calories(food_name):
    conn = sqlite3.connect("food_calories.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT calories FROM foods WHERE lower(food_name)=lower(?)",
        (food_name,)
    )

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None

while True:
    print("\n===== FOOD CALORIE APP =====")
    print("1. Check Calories")
    print("2. Add New Food")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        food = input("Food Name: ")
        calories = get_calories(food)

        if calories:
            qty = float(input("Quantity (100g units): "))
            print("Total Calories =", calories * qty)
        else:
            print("Food not found.")

    elif choice == "2":
        food = input("Food Name: ")
        calories = int(input("Calories per 100g: "))

        conn = sqlite3.connect("food_calories.db")
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO foods(food_name, calories) VALUES (?, ?)",
                (food, calories)
            )
            conn.commit()
            print("Food Added Successfully.")
        except:
            print("Food already exists.")

        conn.close()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
