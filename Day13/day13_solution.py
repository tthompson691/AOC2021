from utils import read_input


if __name__ == "__main__":
    inp = read_input("day13_sample_input.txt")

    coords = [i.split(",") for i in inp if "fold" not in i]
    coords = [(int(i[0]), int(i[1])) for i in coords]
    instructions = [i for i in inp if "fold" in i]

    print("d")
