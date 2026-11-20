def main():
    print("This is a demo of exception handling.")
    try: 
        number = int(input("Please enter a number: "))
    except ValueError:
        print("That is not a valid integer")

    print("After the try, except stuff. ")
    
    

if __name__ == "__main__":
    main()