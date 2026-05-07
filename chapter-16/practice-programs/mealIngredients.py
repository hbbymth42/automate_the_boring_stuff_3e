import sqlite3

conn = sqlite3.connect('meals.db', isolation_level=None)

while True:
    user_input = input('>').lower()
    if ':' in user_input:
        meal = user_input.split(':')[0]
        ingredients = user_input.split(':')[1].split(',')
        conn.execute(f'INSERT INTO meals VALUES ("{meal}")')
        meal_id = conn.execute(f'SELECT rowid FROM meals WHERE name = "{meal}"').fetchall()[0][0]
        for ingredient in ingredients:
            conn.execute(f'INSERT INTO ingredients VALUES ("{ingredient}", {meal_id})')
        print(f'Meal added: {meal}')
    elif user_input == 'quit':
        break
    else:
        if len(conn.execute(f'SELECT name FROM meals WHERE name = "{user_input}"').fetchall()) == 0:
            if len(conn.execute(f'SELECT m.name FROM meals m INNER JOIN ingredients i ON m.rowid = i.meal_id WHERE i.name = "{user_input}"').fetchall()) > 0:
                print(f'Meals that use {user_input}:')
                for meal in conn.execute(f'SELECT DISTINCT m.name FROM meals m INNER JOIN ingredients i ON m.rowid = i.meal_id WHERE i.name = "{user_input}"').fetchall():
                    print(meal[0])
            else:
                print('No meals found, please add a meal with ingredients!')
        else:
            print(f'Ingredients of {user_input}:')
            for ingredient in conn.execute(f'SELECT DISTINCT i.name FROM ingredients i INNER JOIN meals m ON i.meal_id = m.rowid WHERE m.name = "{user_input}"').fetchall():
                print(ingredient[0])
