'''
    @Author: Viney Khaneja
    @Date: 2022-04-11 08:54AM
    @Last Modified by: Viney Khaneja
    @Last Modified time: None
    @Title : Printing UserName String
'''

global name
def validating_user_name():
    '''
    Description: Function to get User Name
    Parameters: None
    Returns: Validated Name
    '''
    while(True):
        name = input("Enter user name: ");
        if len(name)>=3:
            return name
            break;
        else:
            print("Enter at least 3 charcters")
            continue

name = validating_user_name()
print(f"Hello {name},How are you?")

