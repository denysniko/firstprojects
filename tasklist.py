# Creating a task list.

lst = list()


def add_task():
    title = input('Enter name task:')
    description = input('Enter des:')
    date_created = input('Enter date:')

    task = {
        'Name': title,
        'Description': description,
        'Data': date_created,
        'Done': False
    }

    lst.append(task)
    print(f"Task '{title}' has been added successfully!")


def view_task():
    print('Task list')
    for index, task in enumerate(lst, start=1):
        status = 'Done' if task['Done'] else 'Not done'
        print(f"{index}. {task['Name']} - {task['Description']} ({task['Data']}) - {status}")


def done_task():
    view_task()
    task_num = int(input('Enter the number of the task you want to mark as completed:'))

    if 0 <= task_num < len(lst):
        lst[task_num]['Done'] = True
        print(f"Task '{lst[task_num]['Done']}' is marked as completed.")
    else:
        print('Incorrect input')

def del_task():
    view_task()
    task_num = int(input('Enter the number of the task you want to delete:'))

    if 0 <= task_num < len(lst):
        deleted_task = lst.pop(task_num)
        print(f"Task '{deleted_task['Name']}' has been successfully deleted.")
    else:
        print('Incorrect input')


add_task()
add_task()
add_task()
view_task()
done_task()
del_task()
view_task()