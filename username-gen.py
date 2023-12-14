import sys


def username_gen(first_name, last_name, rules_path, output_file):
    if (rules_path == ''):
        rules_path = './rules/default.txt'
    with open(rules_path) as rules_file:
        for line in rules_file:
            gen = line.replace('{fn}', first_name)
            gen = gen.replace('{ln}', last_name)
            gen = gen.replace('{fi}', first_name[0])
            gen = gen.replace('{li}', last_name[0])
            output_file.write(gen.replace('\n', '') + '\n')
            gen = line.replace('{fn}', first_name.lower())
            gen = gen.replace('{ln}', last_name.lower())
            gen = gen.replace('{fi}', first_name[0].lower())
            gen = gen.replace('{li}', last_name[0].lower())
            output_file.write(gen.replace('\n', '') + '\n')


if __name__ == "__main__":

    args = sys.argv
    if (len(args) == 1 or '-h' in args or '--help' in args or len(args) < 3):
        print("Username generator by shibajutsu v0.1")

        print(
            "Usage: python3 username-gen.py [first_name] [last_name] -r [rules_path]")
        print()
        print("Name format: First name and last name with capital first letter")
        print("Example: John Doe")
        print()
        print("-h|--help    :   Show this help message")
        print("-f           :   Use a file with names")
        print()
        print("-o           :   Output file path")
        print()
        print("-r           :   Rules file path (Optional)")
        print()
        exit(0)

    rules_path = ''
    if ('-r' in args):
        rules_path = args[args.index('-r') + 1]
    output_file = './username_gen.txt'
    if ('-o' in args):
        output_file = args[args.index('-o') + 1]
    with open(output_file, 'w') as output_file:
        if ('-f' in args):
            with open(args[args.index('-f') + 1]) as names_file:
                for line in names_file:
                    first_name = line.split()[0]
                    last_name = line.split()[1]
                    username_gen(first_name, last_name,
                                 rules_path, output_file)
        else:
            first_name = args[1]
            last_name = args[2]
            username_gen(first_name, last_name, rules_path, output_file)
