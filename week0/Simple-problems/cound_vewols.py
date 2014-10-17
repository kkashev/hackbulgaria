def count_vewols(s):
    
    count = 0
    vewols = ["a", "e", "i", "o", "u", "y"]
    for i in s:
        for item in vewols:
            if item.find(s) != -1:
                count += 1
                break
    return count


def main():
    print(count_vewols("Python"))

if __name__ == '__main__':
    main()
