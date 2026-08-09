seat=[]


for i in range(65,75+1):
    # print(chr(i),end=" : ")
    for j in range(1,11):
        seat.append(f"{chr(i)}{j}") 
      
print(seat)


book_seat=[]
while True:
    try:
        seats = input("enter you seat : ")
        if seats.lower() == "no":
             for booked in book_seat:
                  print(f"you have booked {booked} seat")
             break
        if seats not in seat:
            raise ValueError("invalid seat")
        if seats in book_seat:
                raise ValueError("seat alrady booked")
        
        book_seat.append(seats)
        print(f"Seat {seats} booked successfully!")
    except ValueError as e:
        print(e)
