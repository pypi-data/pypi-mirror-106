def store_data():
    myfile = open('DataStorer_Data.txt','a')
    user_input1 = input('Enter a topic [please do write them in CAPS...] :')
    user_input2 = input('Enter a query : ')
    myfile.writelines('TOPIC --- ' + user_input1 +  '\n ' + 'Query ---'+user_input2 + '\n')
    print('Your data was stored in a file ')
