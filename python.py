abhinav_input=input()
anjali_input=input()

if anjali_input==abhinav_input:
    print("Tie")
elif anjali_input=="Scissors" and abhinav_input=="Paper":
    print("Anjali Wins")
elif anjali_input=="Paper" and abhinav_input=="Rock":
    print("Anjali Wins")
elif anjali_input=="Rock" and abhinav_input=="Scissors":
    print("Anjali Wins")

elif anjali_input=="Scissors" and abhinav_input=="Paper":
    print("Anjali Wins")
elif anjali_input=="Scissors" and abhinav_input=="Rock":
    print("Abhinav Wins")
elif anjali_input=="Paper" and abhinav_input=="Scissors":
    print("Abhinav Wins")
