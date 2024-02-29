class LengthOfLastWord(object):
    def sliding_window_length_of_last_word(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        j = len(s) - 2
        while i > 0:
            if s[i].isalpha() and not s[i].isspace():
                counter += 1

            if s[j].isspace() and counter > 0:
                break
            i -= 1
            j -= 1

        return counter

    def sliding_window_length_of_last_word2(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        j = len(s) - 2
        while i > 0:
            if s[i].isalpha() and not s[i] == " ":
                counter += 1

            if s[j] == " " and counter > 0:
                break
            i -= 1
            j -= 1

        return counter

    def neet_length_of_last_world(self, s: str) -> int:
        i = len(s) -1
        length = 0

        while s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length


len_word = LengthOfLastWord()
# print(len_word.sliding_window_length_of_last_word("Hello world"))
# print(len_word.sliding_window_length_of_last_word("   fly me   to   the moon  "))
# print(len_word.sliding_window_length_of_last_word("luffy is still joyboy"))

# print(len_word.sliding_window_length_of_last_word2("Hello world"))
# print(len_word.sliding_window_length_of_last_word2("   fly me   to   the moon  "))
# print(len_word.sliding_window_length_of_last_word2("luffy is still joyboy"))


print(len_word.neet_length_of_last_world("Hello world"))
print(len_word.neet_length_of_last_world("   fly me   to   the moon  "))
print(len_word.neet_length_of_last_world("luffy is still joyboy"))