class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

class Playground(object):

    def __init__(self):
        self.value = None

    def get_attempts(self, n):
        x = 0
        while x < n:
            print("keep going=", x)
            x += 1

        print(" x ", x, " n = ", n)
        return x

    def fizzBuzz(self, n):
        # Write your code here

        for i in range(1, n + 1):
            string = ""
            if i % 3 == 0:
                string = string + "Fizz"
            if i % 5 == 0:
                string = string + "Buzz"
            if i % 5 != 0 and i % 3 != 0:
                string = string + str(i)
            print(string)

    def compressWord(self, word, k):
        # Write your code here

        # get the length
        n = len(word)
        if (n == 0):
            return

        result = ""
        i = 0
        j = 0
        while (i < n):
            j = 0
            while j < k and j + i < n and word[j + i] == word[i]:
                j += 1

            if j == k:
                # skip consecutive
                i += j
            else:
                result = result + str(word[i])
                i += 1

        print(result)

    def nested_for_loops(self):
        for left in range(7):
            for right in range(left, 7):
                print("[" + str(left) + "|" + str(right) + "]", end=" ")
            print(left)

    def looping_string(self, string):
        my_string = string
        for i, character in my_string:
            print(character)

    def slicing_string(self, string, from_idx, to_idx):
        return string[from_idx:]

    def while_loo_decrease_each_five(self):
        number = 15  # Initialize the variable
        while number >= 5:  # Complete the while loop condition
            print(number, end=" ")
            number -= 5
            # Increment the variable

        # Should print 15 10 5

    def counter(self, start, stop):
        if start > stop:
            return_string = "Counting down: "
            while start >= stop:  # Complete the while loop
                return_string += str(start)  # Add the numbers to the "return_string"
                if start > stop:
                    return_string += ","
                start -= 1  # Increment the appropriate variable
        else:
            return_string = "Counting up: "
            while stop >= start:  # Complete the while loop
                return_string += str(start)  # Add the numbers to the "return_string"
                if start < stop:
                    return_string += ","
                start += 1  # Increment the appropriate variable
        return return_string

    def num_tog(self):
        x = 1
        sum = 0
        while x <= 10:
            sum += x
            x += 1
        print(sum)

    def sum_for_loop(self):
        # for sum in range(5):
        #     sum += sum
        #     print(sum)
        #
        # for x in range(10):
        #     for y in range(x):
        #         print(y)
        #
        #
        # for count in range(1, 6):
        #     print(count + 1)

        for outer_loop in range(2, 6 + 1):
            print("outer_loop=", outer_loop)
            for inner_loop in range(outer_loop):
                if inner_loop % 2 == 0:
                    print("inner_loop=" , inner_loop)

    def combine_lists(self, list1, list2):

        combined_list = []  # Initialize an empty list variable
        reversed_list1 = [list1[index-1] for index in range(len(list1), 0, -1)]  # Reverse the order of "list1"
        print(reversed_list1)
        # ___  # Combine the two lists
        combined_list = list2
        return combined_list

    def car_make(self):
        car_make = "Lamborghini"
        print(car_make[3:-5])
        print(car_make[-4:])
        print(car_make[:7])

    def get_event_date(self, event):
        return event.date

    def current_users(self, events):
        events.sort(key=get_event_date)
        machines = {}
        for event in events:
            if event.machine not in machines:
                machines[event.machine] = set()
            if event.type == "login":
                machines[event.machine].add(event.user)
            elif event.type == "logout" and event.user:
                machines[event.machine].remove(event.user)
        return machines

    def generate_report(machines):
        for machine, users in machines.items():
            if len(users) > 0:
                user_list = ", ".join(users)
                print("{}: {}".format(machine, user_list))

    def is_palindrome(input_string):
        # Two variables are initialized as string date types using empty
        # quotes: "reverse_string" to hold the "input_string" in reverse
        # order and "new_string" to hold the "input_string" minus the
        # spaces between words, if any are found.
        new_string = ""
        reverse_string = ""

        # Complete the for loop to iterate through each letter of the
        # "input_string"
        for letter in input_string:

            # The if-statement checks if the "letter" is not a space.
            if letter != " ":
                # If True, add the "letter" to the end of "new_string" and
                # to the front of "reverse_string". If False (if a space
                # is detected), no action is needed. Exit the if-block.
                new_string = new_string + letter
                # print("new string=" + new_string)
                reverse_string = letter + reverse_string
                # print("reverse=" + reverse_string)

        # Complete the if-statement to compare the "new_string" to the
        # "reverse_string". Remember that Python is case-sensitive when
        # creating the string comparison code.
        # print("new_string= "+ new_string + " reverse_string= "+ reverse_string)
        if new_string.lower() == reverse_string.lower():
            # If True, the "input_string" contains a palindrome.
            return True

        # Otherwise, return False.
        return False

    def replace_ending(self, sentence, old, new):
        # Check if the old substring is at the end of the sentence
        if sentence.endswith(old):
            # Using i as the slicing index, combine the part
            # of the sentence up to the matched string at the
            # end with the new string
            i = sentence.rindex(old)
            new_sentence = sentence[:i] + new
            return new_sentence

        # Return the original sentence if there is no match
        return sentence



compress = Playground()

#  Test
#  N = 3
# compress.compressWord("iiiiiceooookddeeee", 3)
# compress.compressWord("caaooooodeees", 2)
# compress.nested_for_loops()
# compress.looping_string("Loooping_string_for_practicing_python")
# print(compress.slicing_string("Loooping_string_for_practicing_python",  -6, 7))
# print(compress.while_loo_decrease_each_five())

# print(compress.counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(compress.counter(2, 1)) # Should be "Counting down: 2,1"
# print(compress.num_tog()) # Should be "Counting down: 2,1"
# print(compress.sum_for_loop()) # Should be "Counting down: 2,1"

# Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
# Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]

# print(compress.combine_lists(Jaimes_list, Drews_list))
# Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']

# print(compress.car_make())
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

print(compress.replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(compress.replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(compress.replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(compress.replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"
