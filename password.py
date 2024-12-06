user_password=input("Enter new password")
result={}
if len(user_password)>=8:
    result['length']=True
else:
    result['length']=True

digit=False
for i in user_password:
    if i.isdigit():
        digit=True
result['digit']=digit

uppercase=False

for i in user_password:
    if i.isupper():
        uppercase=True
result['upper']=uppercase

if all (result.values()):
    print('Strong password')
else:
    print('Weak ass password')

