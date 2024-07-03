def snake_to_camel(snake_str):
    components = snake_str.split('_')
    camel_str = components[0] + ''.join(x.title() for x in components[1:])
    return camel_str
snake_str = "this_is"
camel_str = snake_to_camel(snake_str)
print("Snake case:", snake_str)
print("Camel case:", camel_str)
