if N%4 == 0 and N%100 == 0 and N%400==0:
            return 1
        elif N%4 == 0 and (N%100 != 0 or N%400 ==0):
            return 1
        else:
            return 0