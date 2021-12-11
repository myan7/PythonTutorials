
prompt = "Enter a base : "
prompt_2 = "Enter an exponent : "
user_input_base = float(input(prompt))
user_input_exponent = float(input(prompt_2))
result = user_input_base**user_input_exponent
# result = pow(user_input_base,user_input_exponent)

print(f"{user_input_base} to the power of {user_input_exponent} = {result}")
