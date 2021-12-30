address = input('Please, Enter your IP: ')
mac = input('Please, Enter your MAC: ').upper()
doman = input('Please, Enter your Damain: ').upper()
text = '''IP address: {}
MAC address: {}
Domane name: {}'''.format(address, mac, doman)
print(text)

'''
Output:
Please, Enter your IP: 10.128.52.62
Please, Enter your MAC: ab-00-ca-46-gb
Please, Enter your Damain: mail.ru
IP address: 10.128.52.62    
MAC address: AB-00-CA-46-GB 
Domane name: mail.ru    

///Метод2
text = 'IP address: {}\nMAC address: {}\nDomane name: {}'.format(address, mac, doman)
print(text)

///Метод1
listS = ['Alex', 'Women', 26]
text = 'Hello: {}, Your gender: {}, Age: {}'.format(*listS)
print(text)
'''