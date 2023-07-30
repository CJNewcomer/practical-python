# bounce.py
#
# Exercise 1.5
starting_height = 100
bounce_count = 1
# bounce_height will need to be reassigned after each bounce
# to reflect height change

while bounce_count < 11:
    bounce_height = (3/5) * starting_height
    print(bounce_count, round(bounce_height, 3))
    starting_height = bounce_height
    bounce_count += 1
