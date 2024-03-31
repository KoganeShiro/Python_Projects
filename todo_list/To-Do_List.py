import os, time

to_do_list = []


def clean():
  time.sleep(1)
  os.system("clear")


def pretty_print():
  print()
  if len(to_do_list) > 0:
    print("  Index  |    Task    |    Date    |  Priority  ")
    print("-----------------------------------------------")
    for index, task_details in enumerate(to_do_list):
      task_index = index
      task = task_details[0]
      date = task_details[1]
      priority = task_details[2]
      print(f"   {task_index:^5}  |  {task:^5} |  {date:^5} |  {priority:^5}")
      print("-----------------------------------------------")
  else:
    print("No tasks found.")
  print()


filtered_tasks = []


def filtre_tasks():
  # Filtering tasks by priority
  if what_priority == 1:
    filtered_tasks = [
      task_details for task_details in to_do_list if task_details[2] == "Low"
    ]
  elif what_priority == 2:
    filtered_tasks = [
      task_details for task_details in to_do_list
      if task_details[2] == "Medium"
    ]
  elif what_priority == 3:
    filtered_tasks = [
      task_details for task_details in to_do_list if task_details[2] == "High"
    ]


def display_filtre_tasks():
  # Display filtered tasks
  for task_details in filtered_tasks:
    print("Task: ", task_details[0])
    print("Date: ", task_details[1])
    print("Priority: ", task_details[2])
    print("--------------------")


def delete_index():
  matching_tasks = []
  for index, task_details in enumerate(to_do_list):
    if task_details[0] == remove_task:
      matching_tasks.append((index, task_details))
      # Stores the index and details of matching tasks in the matching_tasks list

    if len(matching_tasks) > 0:
      print("Matching tasks:")
      for index, task_details in matching_tasks:
        print(
          f"Index:{index}\n Task: {task_details[0]}\n Date: {task_details[1]}\n Priority: {task_details[2]}"
        )


def delete_confirmation():
  # Displays the matching tasks with their corresponding indexes

  confirm_index = input(
    "Enter the index of the task to remove (or 'cancel' to cancel): ")
  if confirm_index == 'cancel':
    print("Task removal canceled.")
  else:
    try:
      confirm_index = int(confirm_index)
      if confirm_index >= 1 and confirm_index <= len(matching_tasks):
        index_to_remove = matching_tasks[confirm_index - 1][0]
        # Retrieves the index of the task to remove from the matching_tasks list
        to_do_list.pop(index_to_remove)
        print("Task removed successfully!")
      else:
        print("Invalid index. Task removal canceled.")
    except ValueError:
      print("Invalid input. Task removal canceled.")
    else:
      print("No matching tasks found.")


print("  === Welcome to your upgrade to do list ! ===")
while True:
  try:
    menu = int(
      input("""
    1 : Add
    2 : View
    3 : Remove
    4 : Edit
    any other numbers : Exit
    --> """))

  except ValueError:
    print("Please type numbers")

  if menu == 1:
    clean()
    task = input("What is the task ? > ")
    date = input("When is it due by ? > ")
    priority = input("What is the priority ? (High, Medium, Low) > "
                     ).capitalize()  #on peut mettre ce que l'on veut ici
    task_details = [task, date, priority]
    to_do_list.append(task_details)

  elif menu == 2:
    clean()
    try:
      view_choice = int(
        input("""
    1 : View All
    2 : View by priority
    --> """))
    except ValueError:
      print("Please type numbers")

    if view_choice == 1:
      pretty_print()
      enter = input("input anything to go back to the menu ")
      clean()

    elif view_choice == 2:
      try:
        what_priority = int(
          input("""With what priority do you wish to view ?
        1 : Low
        2 : Medium
        3 : High
        --> """))
      except ValueError:
        print("Please type numbers")
#don't work....
      filtered_tasks = [
        task_details for task_details in to_do_list
        if what_priority == task_details[2]
      ]

      if filtered_tasks:
        print("Filtered tasks:")
        for task_details in filtered_tasks:
          print("Task:", task_details[0])
          print("Date:", task_details[1])
          print("Priority:", task_details[2])
          print("--------------------")
      else:
        print("No tasks found with the selected priority.")
      print()

  elif menu == 3:
    pretty_print()
    remove_task = input("Enter the task you want to remove: ")
    clean()
    for task_details in to_do_list:
      if remove_task in task_details:
        confirmation = input(
          "Are you sure you want to delete this task ? (No cheating...) Yes/No "
        )
        if confirmation.lower() == "yes":
          to_do_list.remove(task_details)
          print("Task remove successfully, Good Job !")
        else:
          print("Your task is still there")

  elif menu == 4:
    pretty_print()
    edit_task = input("Enter the name of the task you want to edit: ")

    # Create a list to store matching tasks and their indexes
    matching_tasks = []

    # Iterate over each task_details sublist in the to_do_list
    for index, task_details in enumerate(to_do_list):
      # Check if the task name matches the task the user wants to edit
      if task_details[0] == edit_task:
        # If there is a match, append the index and task_details to the matching_tasks list
        matching_tasks.append((index, task_details))

    # Check if any matching tasks were found
    if len(matching_tasks) > 0:
      print("Matching tasks:")
      # Print the matching tasks along with their indexes
      for index, task_details in matching_tasks:
        print(
          f"{index}: Task: {task_details[0]}, Date: {task_details[1]}, Priority: {task_details[2]}"
        )

    # Check if there is only one matching task
      if len(matching_tasks) == 1:
        index_to_edit = matching_tasks[0][0]
        task_details = to_do_list[index_to_edit]

        print("Current task details:")
        print("Task:", task_details[0])
        print("Date:", task_details[1])
        print("Priority:", task_details[2])

        # Prompt the user to choose what aspect of the task they want to update
        update_choice = input(
          "What do you want to update? (task, date, priority, all): ")
        update_choice = update_choice.lower()

        # Update the task name if the user chose "task" or "all"
        if update_choice == "task" or update_choice == "all":
          new_task = input("Enter the updated task: ")
          task_details[0] = new_task

        # Update the task date if the user chose "date" or "all"
        if update_choice == "date" or update_choice == "all":
          new_date = input("Enter the updated date: ")
          task_details[1] = new_date

        # Update the task priority if the user chose "priority" or "all"
        if update_choice == "priority" or update_choice == "all":
          new_priority = input("Enter the updated priority: ")
          task_details[2] = new_priority

          print("Task edited successfully!")
          clean()

    else:
      print("No matching tasks found.")
      continue

  else:
    print("See ya !\n Work smarter and hard 💪😘")
    break
