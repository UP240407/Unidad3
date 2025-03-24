# 1. Crear una tupla vacía
tupla_vacia = ()

# 2. Crear una tupla con los nombres de tus hermanas y hermanos (hermanos y hermanas imaginarios están bien)
hermanas = ('Isabella', 'Maria', 'Alejandra')  
hermanos = ('Jorge', 'Luis')  

# 3. Unir las tuplas de hermanos y hermanas y asignarla a la tupla 'siblings'
hermanos_y_hermanas = hermanas + hermanos
print(hermanos_y_hermanas)  

# 4. ¿Cuántos hermanos y hermanas tienes?
cantidad_siblings = len(hermanos_y_hermanas)
print(f"Tengo {cantidad_siblings} hermanos y hermanas.")  

# 5. Modificar la tupla 'siblings' para agregar el nombre de tu padre y madre, y asignarla a 'family_members'
padre = 'Jorge'
madre = 'Olivia'
familia = hermanos_y_hermanas + (padre, madre)
print(familia) 

### Exercises: Level 2

#1. Unpack siblings and parents from family_members
familia = ('Isabella', 'Maria', 'Alejandra', 'Jprge', 'Luis', 'Jorge', 'Olivia')
#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
hermanos_y_hermanas, padre, madre = familia[:-2], familia[-2], familia[-1]
print(f"Hermanos y hermanas: {hermanos_y_hermanas}")  
print(f"Padre: {padre}, Madre: {madre}")  

#3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
frutas = ('Manzana', 'Banana', 'Cereza')
vegetales = ('Zanahoria', 'Brócoli', 'Espinaca')
productos_animales = ('Leche', 'Huevo', 'Queso')
#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = frutas + vegetales + productos_animales
print(food_stuff_tp)  

#5. Slice out the first three items and the last three items from food_staff_lt list.
if len(food_stuff_lt) % 2 != 0:
    middle_item = food_stuff_lt[len(food_stuff_lt) // 2]
    print(f"Elemento del medio: {middle_item}") 
else:
    middle_items = food_stuff_lt[len(food_stuff_lt) // 2 - 1: len(food_stuff_lt) // 2 + 1]
    print(f"Elementos del medio: {middle_items}")  
#6. Delete the food_staff_tp tuple completely
primeros_tres_ultimos_tres = food_stuff_lt[:3] + food_stuff_lt[-3:]
print(f"Primeros tres y últimos tres elementos: {primeros_tres_ultimos_tres}")  # Salida: ['Manzana', 'Banana', 'Cereza', 'Leche', 'Huevo', 'Queso']

#17. Check if an item exists in  tuple:
del food_stuff_tp

#- Check if 'Estonia' is a nordic country
#- Check if 'Iceland' is a nordic country

nordic_countries = ('Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland')
print('Estonia' in nordic_countries)  
print('Iceland' in nordic_countries) 

