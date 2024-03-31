import os, time


def clean():
  time.sleep(1)
  os.system("clear")


def save_file():
  inventory = []
  try:
    f = open("rpg.inventory", "r")
    inventory = f.read().splitlines()
    f.close()
  except Exception:
    print("Error, file not found")
  return inventory


def add(item, description, quantity):
  inventory = save_file()
  item_found = False

  # Check if the item is already in the inventory
  for i in range(0, len(inventory), 4):  # Items are listed every 4 lines
    if f"Item: {item}" in inventory[i]:
      with open("rpg.inventory", "r+") as f:
        lines = f.readlines()
        for j, line in enumerate(lines):
          if f"Item: {item}" in line:
            quantity_line = lines[j + 2]
            current_quantity = int(quantity_line.split()[-1])
            new_quantity = current_quantity + quantity
            lines[j + 2] = f"Quantity: {new_quantity}\n"
            if not lines[j + 1].strip().startswith("Description:"):
              lines[j + 1] = f"Description: {description}\n"
            f.seek(0)  # Move the cursor to the beginning of the file
            f.writelines(lines)  # Write the modified lines
            f.truncate()  # Remove any remaining content
            item_found = True
            print(f"{item}, has been added to your inventory.")
            _ = input("\n  Type anything to return to the menu\n> ")
            break

  if not item_found:
    with open("rpg.inventory", "a") as f:
      f.write(f"Item: {item}\n")
      f.write(f"Description: {description}\n")
      f.write(f"Quantity: {quantity}\n\n")
      print(f"{item}, has been added to your inventory.")


def view():
  inventory = save_file()

  #   for line in inventory:
  #       print(line.strip())
  #print all the information in the file

  # Print only the items
  items = []
  print()
  for i in range(0, len(inventory), 4):
    item_line = inventory[i].split(": ")[1]
    items.append(item_line)
    print(item_line)

  more = input("\nDo you want to see an item in detail? (y/n)\n> ").lower()
  if more == "y" or more == "yes":
    detail = input("\n  Which item do you want to view?\n> ").upper()
    found = False

    for i in range(0, len(inventory), 4):  # Items are listed every 4 lines
      if f"Item: {detail}" in inventory[i]:
        found = True
        quantity_line = inventory[i + 2].strip()
        description_line = inventory[i + 1].strip()
        quantity = quantity_line.split()[-1]
        description = description_line.split("Description: ")[1]
        print(f"Item: {detail}")
        print(f"Description: {description}")
        print(f"Quantity: {quantity}")
        _ = input("Type anything to return to the menu\n> ")
        break

    if not found:
      print(f"{detail} not found in inventory.")
  else:
    _ = input("Type anything to return to the menu\n> ")


def remove(item_to_remove, quantity_to_remove):
  inventory = save_file()
  found = False
  updated_lines = []

  with open("rpg.inventory", "r") as f:
    lines = f.readlines()
    for i in range(0, len(inventory), 4):  # Items are listed every 4 lines
      if f"Item: {item_to_remove}" in inventory[i]:
        found = True
        quantity_line = lines[i + 2]
        current_quantity = int(quantity_line.split()[-1])

        if quantity_to_remove >= current_quantity:
          confirm = input(
            f"Are you sure you want to remove all {current_quantity} {item_to_remove}(s)? (y/n)\n> "
          ).lower()
          if confirm == "y" or confirm == "yes":
            print(
              f"Removing all {current_quantity} {item_to_remove}(s) from your inventory."
            )
            # Skip this item (do not include it in updated_lines)
          else:
            updated_lines.extend(lines[i:i + 4])  # Keep the item in inventory
        else:
          confirm = input(
            f"Are you sure you want to remove {quantity_to_remove} {item_to_remove}(s)? (y/n)\n> "
          ).lower()
          if confirm == "y" or confirm == "yes":
            print(
              f"Removing {quantity_to_remove} {item_to_remove}(s) from your inventory."
            )
            lines[i +
                  2] = f"Quantity: {current_quantity - quantity_to_remove}\n"
          updated_lines.extend(lines[i:i + 4])
      else:
        updated_lines.extend(lines[i:i + 4])  # Keep other items in inventory

  if found:
    with open("rpg.inventory", "w") as f:
      f.writelines(updated_lines)
  else:
    print(f"{item_to_remove} not found in inventory.")


while True:
  clean()
  print("🧰 RPG Inventory 🧰")
  print(
    "\nWelcome to your inventory, what would you like to do ? (please type an integer)"
  )
  save_file()
  try:
    choice = int(input("1: Add\n2: View\n3: Remove\n4: Quit\n> "))
    if choice == 1:
      item = input("\ninput the item to add > ").upper()
      print()
      description = input(
        "\nWrite a short description about the item (you can leave it blank if you want\n> "
      ).title()
      print()
      try:
        quantity = int(input("How many ?\n> "))
      except:
        print("error, please type an integer")
      add(item, description, quantity)

    elif choice == 2:
      view()

    elif choice == 3:
      item_to_remove = input(
        "Enter the name of the item to remove:\n> ").upper()
      print()
      try:
        quantity_to_remove = int(input("How many ?\n> "))
      except:
        print("ERROR, please type an integer")
      remove(item_to_remove, quantity_to_remove)

    elif choice == 4:
      break
    else:
      print('Please type "1", "2" or "3", "4"')
  except ValueError:
    print('Please type "1", "2" or "3", "4"')
