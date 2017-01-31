def print_args_info(*args, **kwargs):
    args_count = len(args)
    print('args count : {}'.format(args_count))
    return args_count

result = print_args_info(3, 5, 10, 'asdf', [])
print(result)
