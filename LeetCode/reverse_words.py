"""
151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""

# split sentence by spaces
# turn in to array
# reverse array
# join array and convert to string
def reverseWords(s: str) -> str:
    s_list = s.split(" ")
    
    no_blank_s_list = list(filter(None ,s_list))
    reverse_s_list = no_blank_s_list[::-1]
    return " ".join(reverse_s_list)

if __name__ == "__main__":
    print(reverseWords("the sky is blue"))
    print(reverseWords("  hello world  "))
    print(reverseWords("a good   example"))