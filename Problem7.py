""" This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed."""

message = '123'
string = 'abcdfghijklmnopqrstuvwxyz'

def decode(message):

    code = ''
    # this part will loop through each integer in message and give a letter
    # for i in range(len(message)):
    #     for j in range(len(string)):
    #         if int(message[i]) == j+1: # need to use j+1 because for loop is from 0 to N, but a = 1 not a = 0, therefore need to add 1
    #            code += string[j]
    #            print(j)

# --> use slicing of the string to break the message into 1 23 and 12 3
# can do select in slicing as message[0:1+1][1] which is 2

    for i in range(len(message)):
        # print(message[0:i], message[i:])

        # for k in message[0:i+1]:
        #     print(k)

        for j in range(len(string)):
            # print(message[0:i+1])

            if int(message[0:i+1]) < len(string):
                if int(message[0:i+1]) == j+1:
                    print(string[j])
                    # break
                elif int(message[0:i+1]) > len(string):
                    for q in range(len(message[0:i+1])):
                        for k in range(len(string)):
                         if int(message[0:i+1][q]) == k:
                             # print(True)

                            print(string[k])
                            # break
                            # a=2
        #
        # for k in range(len(string)):
        #     print(message[i+1:])
        #     try:
        #          if int(message[i+1:]) == k+1:
        #              print(string[k])
        #     except:
        #         a=2



    return
            # if int(message[k]) == j + 1:  # need to use j+1 because for loop is from 0 to N, but a = 1 not a = 0, therefore need to add 1
            #            code += string[j]
            #            print(j)

    #return --> if put it after for loop, function will exit after first iteration. if put at the same height of for loop, then it will exit only after doing the whole loop
    # to return values without breaking loop then use yield which yields an item and saves the function state. then you cna just get the values using my_func.next()
decode(message)

