def show(data):
    key, user, birth, phonehome, phonemobile = data
    result = ''
    print('id name birthdate phone1 phone2')
    for i in key:
        result = str(key[i])+" "+user[i]+" "+str(birth[i]) + \
            " "+str(phonehome[i])+" "+str(phonemobile[i])
        print(result)


#key = [0,1]
#data = ['user0', 'user1']
#birth= [(1968, 6, 3), (1998, 11, 11)]
#phonehome = [9209, 7522]
#phonemobile= [12112122, 87653903]
#show((key, data, birth, phonehome, phonemobile))
