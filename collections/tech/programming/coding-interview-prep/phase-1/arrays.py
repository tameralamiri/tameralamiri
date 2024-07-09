# Given a string and a substring, find the number of times the substring occurs in the string and count them only once
# Example: string = "ababababab", substring = "abab", output = 2
# Example: string = "11111", substring = "11", output = 2
def count_substring(string, substring):
    count = 0
    while substring in string:
        count += 1
        string = string.replace(substring, "", 1)
    return count

# Given a string and a substring, return the string with all occurrences of the substring removed.
# Example: string = "ababababab", substring = "ab", output = ""

def remove_substring(string, substring):
    while substring in string:
        string = string.replace(substring, "")
    return string

# Given a string, remove extra spaces from the string and return the string.
# Example: string = "  hello  world  ", output = "hello world"
def remove_extra_spaces(string):
    return " ".join(string.split())

# Given a string, capitalize all lowercase characters in the string.
# Example: string = "hello world", output = "HELLO WORLD"
def capitalize_string(string):
    return string.upper()

# write a function that takes a string as an input and returns it with only vowels reversed.
# Example: string = "hello world", output = "hollo werld"
def reverse_vowels(string):
    vowels = "aeiouAEIOU"
    string = list(string)
    i, j = 0, len(string) - 1

    while i < j:

        while string[i] not in vowels and i < j:
            i += 1

        while string[j] not in vowels and i < j:
            j -= 1

        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1

    return "".join(string)

# Given a string, reverse it by a block of k characters. without using the builtin reversed function
# Example: string = "abcdef", k = 2, output = "bacdfe"
def reverse_string_by_k(string, k):
    string = list(string)
    for i in range(0, len(string), k):
        string[i:i + k] = string[i:i + k][::-1]
    return "".join(string)


print(reverse_vowels("    hello     world wow 111"))





