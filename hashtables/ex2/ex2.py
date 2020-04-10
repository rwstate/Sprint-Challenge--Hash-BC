#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = []
    for ticket in tickets:
        if ticket.source != "NONE":
            hash_table_insert(ht, ticket.source, ticket.destination)
        else:
            route.append(ticket.destination)

    destination = route[0]
    while destination != "NONE":
        newDest = hash_table_retrieve(ht, destination)
        if newDest != "NONE":
            route.append(newDest)
        destination = newDest

    return route
