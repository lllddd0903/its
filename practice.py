# def odd_or_even(number):
#     if not number:
#         number = [0]
#         return "Even"
#     total = sum(number)
#     if total % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(odd_or_even([0]))
# print(odd_or_even([0, 1, 4]))
# print(odd_or_even([0, -1, -5]))

# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#     elif (p1 == "rock" and p2 == "scissors") or \
#        (p1 == "scissors" and p2 == "paper") or \
#        (p1 == "paper" and p2 == "rock"):
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"
# print(rps("scissors", "paper"))  
# print(rps("scissors", "rock"))  
# print(rps("paper", "paper")) 

