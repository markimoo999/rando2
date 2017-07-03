import random
print "hey! let's play rock paper scissors!"
options = ["rock", "paper", "scissors"]
cominput = random.choice(options)
myinput = raw_input("rock, paper, scissors,\n")
if myinput=="scissors" and cominput=="rock":
    print "SHOOT! ...HA! I did rock! I win!!!"
elif myinput=="rock" and cominput=="paper":
    print "SHOOT! ...HA! I did paper! I win!!!"
elif myinput=="paper" and cominput=="scissors":
    print "SHOOT! ...HA! I did scissors! I win!!!"
elif myinput=="paper" and cominput=="rock":
    print "SHOOT!...DANG! I did rock. You win."
elif myinput=="scissors" and cominput=="paper":
    print "SHOOT!...DANG! I did paper. You win."
elif myinput=="rock" and cominput=="scissors":
    print "SHOOT!...DANG! I did scissors. You win."
elif myinput=="rock" and cominput=="rock":
    print "SHOOT!...Welp, try the program again. we did the same thing."
elif myinput=="scissors" and cominput=="scissors":
    print "SHOOT!...Welp, try the program again. we did the same thing."
elif myinput=="paper" and cominput=="paper":
    print "SHOOT!...Welp, try the program again. we did the same thing."
