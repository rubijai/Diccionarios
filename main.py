# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Jaime Ramirez')
l1 = []
n_l1 = [n*n for n in range(1,11) if n % 2 == 0]
suma = sum(n_l1)
print(f'suma = {suma}')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
