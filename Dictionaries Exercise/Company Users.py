company_users = {}

while True:
    current_input = str(input())
    if current_input == "End":
        break
    current_input = current_input.split(" -> ")
    current_company = current_input[0]
    current_ID = current_input[1]
    if current_company in company_users.keys():
        current_company_obj = company_users[current_company]
        flag = False
        for id in current_company_obj.keys():
            if current_ID == id:
                flag = True
        if flag == False:
            company_users[current_company][current_ID] = "PowerCell46"
    else:
        company_users[current_company] = {}
        company_users[current_company][current_ID] = "PowerCell46"

for key, obj in company_users.items():
    print(key)
    for id in obj.keys():
        print(f'-- {id}')
        
