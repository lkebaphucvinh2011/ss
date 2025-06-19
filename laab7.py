def quiz1():
    print("1+1 = ?")
    user = int(input("Enter your answer:"))
    return user
def quiz2():
    print("2+2 = ?")
    user = int(input("Enter your answer:"))
    return user
def quiz3():
    print("3+3 = ?")
    user = int(input("Enter your answer:"))
    return user
def true_false():
    if quiz1() == 2:
        print("true")
    if quiz2() == 4:
        print("true")
    if quiz3() == 6:
        print("true")
    else:
        print("false")
    print("game over")
    quit()


def main():
    true_false()
    quiz1()
    quiz2()
    quiz3()
main()


