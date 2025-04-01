import request

target = input('Please Enter target IP: ')

while True:
    r = request.get(target)
    
    print(r.status_code)