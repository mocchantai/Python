def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        if s_list[left] in vowels and s_list[right] in vowels:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
        elif s_list[left] in vowels:
            right -= 1
        elif s_list[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1

    return ''.join(s_list)

if __name__ == '__main__':
    # Example usage for manual testing
    print(reverseVowels('hello'))  # Output: "holle"
    print(reverseVowels('leetcode'))  # Output: "leotcede"
