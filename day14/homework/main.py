#and ოპერაციის გამოყენებისას უპირატესობა ენიჭება False-ს
#or ოპერაციის გამოყენებისას უპირატესობა ენიჭება True-ს

#and
False and False
True and False
False and True
True and True

#or
False or False
True or False
False or True
True or True

# • False or True and True and False-False-ს
# • True and False or False or True-True-ს
# • True or True and False or True or False and True or False-True-ს

max_temp=30
temp2=int(input("Enter House Temp: "))
print(max_temp > temp2 or max_temp < temp2)