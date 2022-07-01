import re


class Bracket:

    def __init__(self, index: int, type: str, inverted_bracket_index: int = 0):
        self.index = index
        self.type = type
        self.inverted_bracket_index = inverted_bracket_index

    def compare_to(self, other: "Bracket") -> bool:
        """Checks bracket is the inverse of self

        Args:
            bracket (Bracket): The second Bracket to compare the brackets against

        Returns:
            bool: True if the two brackets are inverses of each other
        """
        pairs = {
            "}": "{",
            "]": "[",
            ")": "(",
            "{": "}",
            "[": "]",
            "(": ")",
            "'": "'",
            '"': '"',
        }

        if str(self.type) in pairs.keys():
            if other.type == pairs[self.type]:
                return True
        return False

    def is_parenthesis(self):
        return self.type in ("'", '"')


def find_occurrences(regex: str, s: str) -> list:
    """Find statements in a string that match regex pattern.

    Args:
        regex (str): The regular expression to match against
        s (str): The string to match against

    Returns:
        list[int]: Returns a list of indexes of the characters after the ocurrences in the string
    """

    statements = []
    ocurrence_index = 0
    while True:
        ocurrence = re.search(regex, s[ocurrence_index:])
        if ocurrence:
            ocurrence_index += ocurrence.span()[1]
            statements.append(ocurrence_index)
        else:
            break
    return statements


def find_brackets(s: str) -> list:
    """Find brackets

    Args:
        s (str): the file to look for brackets

    Returns:
        list[tuple[int, str]]: list of indexes and of brackets found in the file
    """
    brackets = find_occurrences(
        r"(?<!\\)[\{\[\(\"\'\]\}\)]", s
    )  # find all brackets in string

    stack = []  # Stack of brackets
    result = []  # Result of the search expression without parentheses

    for bracket_index in brackets:
        bracket = Bracket(bracket_index, s[bracket_index - 1])
        if bracket.is_parenthesis() and bracket.type in map(lambda x: x.type, stack):
            #     # if the current bracket is a parentheses and is in the stack
            i = list(map(lambda x: x.type, stack)).index(bracket.type)
            stack = stack[
                : i
            ]  # remove everything from the stack from the index of the current bracket located in the stack
            while result[-1].type != bracket.type:
                result.pop()  # Ignore all brackets found inside parentheses
            result.pop()

            # do
            #   result.pop()
            # while result[-1][1] != bracket:
            # This is why we need a do while loop in python
        elif len(stack) > 0 and bracket.compare_to(stack[-1]):
            stack.pop()  # If the last bracket in the stack mathes the current bracket then remove it from the stack
            result.append(bracket)  # Add the current bracket to the result
        else:
            # Else append the the current bracket to the stack
            stack.append(bracket)
            result.append(bracket)  # Add the current bracket to the result
    return result
