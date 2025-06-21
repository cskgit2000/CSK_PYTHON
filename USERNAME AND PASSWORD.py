u_name="CSK"
s_password="12345"
USERNAME=input("ENTER USERNAME =")
PASSWORD=input("ENTER PASSWORD =")
def validate():
    if (u_name==USERNAME and s_password==PASSWORD):
        return True
    else:
        return False
a=validate()
print(a)
