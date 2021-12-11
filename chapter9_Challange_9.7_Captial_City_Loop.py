import random

capitals_dict = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
}

state_name = random.choice(list(capitals_dict.keys()))

user_input = input(f"Do you know the capital of {state_name}? \n")
flag = False

if user_input.title() != capitals_dict[state_name]:
    while(not flag):
        user_input = input(f"maybe try again, do you know the capital of {state_name}? \n")
        if user_input.title() == capitals_dict[state_name]:
            flag = True
else:
    print(f"Congratulations! your answer is correct!!! capital of {state_name} is {user_input.title()}")

