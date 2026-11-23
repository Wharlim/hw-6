class Thing:
    def __init__(self, name):
        self.name = name
        self.count = 0

def main():
    first = Thing("yes")
    second = first
    second.count += 1
    third = Thing("no")
    third.count = first.count + 1
    print(first.count, second.count, third.count)  # Expected output: 1 1 2

if __name__ == "__main__":
    main()

