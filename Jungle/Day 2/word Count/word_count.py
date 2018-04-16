def words(rob_list):
    # function called word with argument rob_list
    rob_count = {}
    for words in [r for r in rob_list.split()]:
        try:
            rob = int(rob)
            try:
                if rob_count[rob]:
                    rob_count[rob] += 1
            except KeyError:
                rob_count[rob] = 1
        except ValueError:
            try:
                if rob_count[rob]:
                    rob_count[rob] += 1
            except KeyError:
                rob_count[rob] = 1
    return rob_count

def main():
    print(words('testing 1 2 testing'))

if __name__ == '__main__':main()
