def main():
    count = 0

    # Example string
    example_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:", end=' ')
    for char in example_string:
        print(char, end=' ')

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:", end=' ')
    print("[" + min(example_string) + "]")

    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:", end=' ')
    print(max(example_string))

    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':", end=' ')
    print(example_string.index('o'))

    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    print(list(example_string))

    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:", end=' ')
    for char in example_string:
        if char == 'o':
            count += 1
    print(count)


main()
