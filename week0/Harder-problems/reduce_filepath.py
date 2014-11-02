def reduce_file_path(path):
    path = path.split("/")
    new_path = []
    for element in path:
        if element == "..":
            if new_path:
                new_path.pop()
        if element != "/" and element != ".":
            new_path.append(element)
    print(new_path)


def main():
    reduce_file_path("/etc//wtf/")
    reduce_file_path("/etc/../etc/../etc/../")

if __name__ == '__main__':
    main()
