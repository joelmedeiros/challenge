class Node(object):

    def __init__(self):
        self.children = {}
        self.words_in_subtree = 0


def IterativeBinaryInsert(new_name, contacts):
    current_position = contacts
    for letter in new_name:
        if not current_position.children.get(letter):
            current_position.children[letter] = Node()
        current_position.children[letter].words_in_subtree += 1
        current_position = current_position.children[letter]


def IterativeBinaryTreeSearch(search_term, contacts):
    current_position = contacts
    for letter in search_term:
        if not current_position.children.get(letter):
            return 0
        current_position = current_position.children.get(letter)
    return current_position.words_in_subtree


number_of_operations = int(raw_input().strip())
root = Node()

for i in xrange(number_of_operations):
    command_and_name = raw_input().lower().split(" ")
    command = command_and_name[0]
    name = command_and_name[1]
    if command == "add":
        IterativeBinaryInsert(name, root)
    elif command == "find":
        print(IterativeBinaryTreeSearch(name, root))
