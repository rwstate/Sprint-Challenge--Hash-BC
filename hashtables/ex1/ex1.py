#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    if length == 1:
        return None
    ht = HashTable(16)

    for i, weight in enumerate(weights):
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        complement = limit - weight
        answer = hash_table_retrieve(ht, complement)
        if answer and i != answer:
            if i > answer:
                return (i, answer)
            else:
                return (answer, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
