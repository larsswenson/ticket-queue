import queue
import time
import random

class Ticket:
    def __init__(self, number):
        self.number = number
        self.timestamp = time.time()

# Generate new ticket & add to queue w/ random time between tickets
def generate_tickets(ticket_queue):
    ticket_number = 1
    while True:
        ticket = Ticket(ticket_number)
        ticket_queue.put(ticket)
        print(f"Customer {ticket.number} took a ticket at {time.strftime('%H:%M:%S', time.localtime(ticket.timestamp))}")
        ticket_number += 1
        time.sleep(random.uniform(1, 3))

# Get next ticket in queue
def process_tickets(ticket_queue):
    while True:
        if not ticket_queue.empty():
            ticket = ticket_queue.get()
            time.sleep(random.uniform(2, 5))

# Initialize ticket queue, generate & process tickets
def main():
    ticket_queue = queue.Queue()

    generate_tickets(ticket_queue)
    process_tickets(ticket_queue)

if __name__ == "__main__":
    main()

