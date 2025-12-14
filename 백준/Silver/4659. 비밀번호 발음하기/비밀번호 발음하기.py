

def acceptable(password,acceptable):
    if acceptable== True:  
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
        

vowels=['a','e','i','o','u']

while True:
    password= input()

    # 종료
    if password=="end":
        break


    # 조건 1
    has_vowel=False
    for v in vowels:
        if v in password:
            has_vowel = True
            break
    
    # 모두 봤지만 모음이 없다면?
    if has_vowel == False:
        acceptable(password,False)
        continue
    

    # 조건 2
    has_sequence_vowels_or_consonant = False
    for i in range(2,len(password)):
        count = 0
        sub_password = password[i-2:i+1]
        for s in sub_password:
            # 모음인 경우 +1
            if s in vowels:
                count+=1

        # 모음 0개 또는 3개인 경우
        if count == 0 or count == 3:
            has_sequence_vowels_or_consonant=True
            break

    # 부분문자열에서 0번 또는 3번 모음이 등장한 경우
    if has_sequence_vowels_or_consonant==True:
        acceptable(password,False)
        continue

    # 조건 3
    is_double=False
    for i in range(1,len(password)):
        # 같은 글자 두번 비허용
        if password[i-1] == password[i]:
            # "oo", "ee"는 허용
            is_oo_or_ee = password[i] == 'e' or password[i] =='o'

            if not is_oo_or_ee:
                is_double = True
                break

    # oo ee 가 아닌 같은 글자의 연속
    if is_double==True:
        acceptable(password,False)
        continue

    # 모든 조건 통과
    acceptable(password,True)
    
