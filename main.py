with open('/home/kareem_ahmed/Documents/Python_Workspace/DNA_Problem/sample.txt', 'r') as file_hand:
    file_content = file_hand.read()
    result_dict = {}
    start = 0
    kemar_len = 5
    while start < len(file_content) - kemar_len + 1:
        sub_str = file_content[start:start+kemar_len]
        if sub_str in result_dict:
            result_dict[sub_str] += 1
        else:
            result_dict[sub_str] = 1
        start += 1
    print(result_dict)