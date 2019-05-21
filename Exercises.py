def maximum(a, b):
    if a > b:
        return a;
    else:
        return b;


def fizz_buzz(a):
    if a%3 == 0 and a%5 == 0:
        return "FizzBuzz";
    elif a%3 == 0:
        return "Fizz";
    elif a%5 == 0:
        return "buzz";
    else:
        return a;


def speed_check(speed):
    if speed < 70:
        print("OK");
    else:
        demerit_points = (speed - 70) / 5;
        if demerit_points >= 12:
            print ("License suspended");
        else:
            print (f'Points: {demerit_points}');


def showNumber(limit):
    for i in range(0,limit+1):
        if i%2 == 0:
            print(f"{i} EVEN");
        else:
            print(f"{i} ODD");


def sum_of_multiples(limit):
    sum = 0;
    for x in range(1,limit+1):
        if x % 3 == 0 or x % 5 == 0:
            sum += x;
    return sum;


def show_stars(rows):
    for i in range(1,rows+1):
        stars = ""
        for x in range(1,i+1):
            stars+="*";
        print(stars);


def prime_number(limit):
    for x in range(1, limit+1):
        if x <= 3:
            print(x);
            continue;
        if x % 3 == 0 or x % 2 == 0:
            continue;
        i = 5;
        while i*i <= x:
            if x % i == 0 or x % (i+2) == 0:
                i = 0;
                break;
            i += 6;
        if i == 0:
            continue;
        print(x);
