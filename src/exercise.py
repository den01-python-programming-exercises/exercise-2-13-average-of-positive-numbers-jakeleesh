def main():
    #write your code below this line
    count = 0
    sum = 0
    while True:
        num = int(input())
        if (num > 0):
            count += 1
            sum += num
        elif (num == 0):
            break
    
    if(sum <= 0):
        print("Cannot calculate the average")
    else:
        print(sum / count)

if __name__ == '__main__':
    main()
