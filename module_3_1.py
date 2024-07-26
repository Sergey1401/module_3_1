calls = 0

# Задача "Счётчик вызовов":
def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    a = []
    a.append(len(string))
    a.append(string.upper())
    a.append(string.lower())
    count_calls(1)
    return a


def is_contains(string, list_to_search):
    string.lower()
    new_list_to_search = []
    count_calls(1)
    for i in list_to_search:
        new_list_to_search.append(i.lower())
    return (string.lower() in new_list_to_search)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
