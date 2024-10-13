#kmp_search2

# Preprocess the pattern to create the longest prefix suffix (LPS) array
def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pattern, text):
    lps = compute_lps_array(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            # print(f"Found pattern at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage
# text = "ABABDABACDABABCABAB"
# pattern = "ABABCABAB"

with open('стаття_2.txt', 'r', encoding='utf-8') as file:
# Read the entire file content into a string
    text = file.read()

pattern = "Визначаються предмети, які буде рекомендовано"
kmp_search(pattern, text)