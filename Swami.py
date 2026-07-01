# function definition
def main():


    #display welcome message
    print("Swami Swami Samrth ")

    #cerate a list
    numbers = [10,20,30,40,50]

    #create a tuple
    subjects =("python ", "Java", "C")


    #Display list elements
    print("\n List Elements:")
    for num in numbers:
        print(num)

    #Display tuple elements
    print("\n Tuple Elements:")
    for num in numbers:
        print(subjects)

    #calculate sum of list elements
    total =sum(numbers)

    #Display total
    print("\nSum of List =", total)

#function main call
if __name__=="__main__":
    main()