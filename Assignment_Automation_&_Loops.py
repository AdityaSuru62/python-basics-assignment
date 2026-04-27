Theatre_Capacity = 350
remaining_seats = Theatre_Capacity
total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while True:
    print("Remaining Seats :", remaining_seats)                   #Total Remaining Seats
    
    tickets = int(input("Enter number of tickets : "))
    
    if tickets == 0:
        break

    if tickets > 15:                                              #Invalid Number of Tickets
        print("BOOKING REJECTED - INVALID NUMBER OF TICKETS")
        rejected_bookings = rejected_bookings+1
        continue

    if tickets > remaining_seats:                                 #Seats Not Available
        print("BOOKING REJECTED - NOT ENOUGH SEATS AVAILABLE")
        rejected_bookings = rejected_bookings+1
        continue

    ages = []                                                     #Age Restriction
    invalid_age = False
    
    for i in range(1,tickets+1):
        age = int(input(f"Enter age of person {i}: "))
        if age < 12:
            invalid_age = True
            continue

    if invalid_age:
        rejected_bookings = rejected_bookings+1
        print("BOOKING REJECTED - AGE RESTRICTION")
        continue
        
    print(f"BOOKING CONFIRMED - {tickets} tickets")
    total_bookings = total_bookings+1
    tickets_sold = tickets_sold+tickets
    remaining_seats = remaining_seats-tickets
    if remaining_seats == 0:
        print("Theatre is now FULL")
        break

print("Total Bookings:", total_bookings)
print("Total Tickets Sold:", tickets_sold)
print("Rejected Bookings:", rejected_bookings)
print("Remaining Seats:", remaining_seats)