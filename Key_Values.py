def create_profile(**kwargs):
    print('User_Profile')
    for key,value in kwargs.items():
        print(f'{key} : {value}')

create_profile(Name='CSK',Age=25,UG='AGRI')