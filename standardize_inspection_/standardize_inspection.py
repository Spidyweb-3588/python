import openpyxl
import re

wb = openpyxl.load_workbook('C:/Users/MS/Downloads/스크립트용표준단어사전양식.xlsx')
standard_sheet = wb['표준단어']
new_word_sheet = wb['추가단어']

#전체 금칙어를 불러와 리스트에 저장
def get_prohibit_word(start_cell: str, end_cell: str) -> list:
    prohibit_list = []
    for i in standard_sheet[start_cell+':'+end_cell]:
        if i[0].value != None: #표준 단어의 각 셀의 값이 None이 아닐 때
            prohibit_list.append(str(i[0].value))#그 값을 str 형식으로 리스트에 저장
        else:
            pass
    return prohibit_list

"""def subtract_sp_sym(prohibit_list:list):
       #전체 금칙어 리스트에서 띄어쓰기, 물음표, 온점을 빼내어 리스트에 저장
       prohibit_list_nospace_dot = []
       for i in prohibit_list:
           prohibit_list_nospace_dot.append(i.replace(" ","").replace("?","").replace(".",""))
       return prohibit_list_nospace_dot"""

def split_word(prohibit_list:list):
    #,를 구분자로하여 단어를 분리하여 리스트에 담음
    prohibit_list_seperate = []
    for i in prohibit_list:
        list_split = i.split(",")
        for j in range(len(list_split)):
            prohibit_list_seperate.append(list_split[j])
    return prohibit_list_seperate


def get_standard_word(start_cell:str, end_cell:str) -> list:
    #표준 단어를 담을 리스트
    word_name = standard_sheet[start_cell+':'+end_cell]#튜플 속의 튜플
    word_name_list = []
    for i in word_name:#튜플 속의 각 튜플들 동안
        if i[0].value != None:#튜플 속의 각 튜플들의 첫번 째 인덱스의 셀의 값이 None이 아니라면
            word_name_list.append(i[0].value)#리스트에 셀의 값을 담는다
        else:
            pass
    return word_name_list


def get_new_word(start_cell:str, end_cell:str) -> list:
    #새로운 단어(추가 되어도 될지 검사해야 할 단어)가 들어오면 담을 리스트
    new_word_name = new_word_sheet[start_cell+':'+end_cell]#새로운 단어의 범위를 지정하여 튜플속의 튜플로 저장
    new_word_name_list = []
    for i in new_word_name:
        if i[0].value != None:
            new_word_name_list.append(i[0].value)
        else:
            pass
    return new_word_name_list

def get_pure_new_word(new_word_name_list: list, word_name_list: list, prohibit_list_seperate: list):
    remain_list = []
    # 새로순 단어의 리스트속의 각 단어가 금칙어이거나, 기존의 단어를 담은 리스트에 있다면, 기존의 단어를 담은 리스트에서 제거, 기존의 단어에 없다면 그것들만 모아서 나머지 리스트에 추가
    for i in new_word_name_list:
        if i in word_name_list:
            pass
        elif i in prohibit_list_seperate:
            pass
        else:
            remain_list.append(i)
    return remain_list


#없는 단어들만 엑셀파일로 떨구는 함수 openpyxl 이용하여 바로 저장
def put_pure_new_word(remain_list: list):
    #금칙어에도 속하지 않고, 표준단어에도 없는 단어의 리스트를 매개변수로 받아와 G2부터 입력하여 저장
    for i in range(2,len(remain_list)+2):
        new_word_sheet[f'G{i}'] = remain_list[i-2]
    return wb.save('C:/Users/MS/Downloads/스크립트용표준단어사전양식.xlsx')


def get_stwrd_in_prhwrd(word_name_list: list, prohibit_list_seperate: list):
    contain_list = []
    for i in range(len(word_name_list)):
        if word_name_list[i] in prohibit_list_seperate:
            contain_list.append(word_name_list[i])
    return contain_list

def put_stwrd_in_prhwrd(contain_list: list):
    # 금칙어에도 속하지 않고, 표준단어에도 없는 단어의 리스트를 매개변수로 받아와 G2부터 입력하여 저장
    for i in range(2, len(contain_list) + 2):
        new_word_sheet[f'I{i}'] = contain_list[i-2]
    return wb.save('C:/Users/MS/Downloads/스크립트용표준단어사전양식.xlsx')


def put_prohibit_word(prohibit_list_seperate: list):
    #금칙어에 포함되어 있는 단어들을 리스트에 담아 K2부터 입력하여 저장
    for i in range(2, len(prohibit_list_seperate)+2):
        new_word_sheet[f'K{i}'] = prohibit_list_seperate[i-2]
    return wb.save('C:/Users/MS/Downloads/스크립트용표준단어사전양식.xlsx')


def get_alternative_word(start_cell: str, end_cell: str) -> list:
    #금칙어에 포함되어 있는 단어들의 권장단어(표준단어)를 얻어내는 함수
    prohibit_cell_index_list = []
    for i in standard_sheet[start_cell+':'+end_cell]:#금칙어단어 리스트중에서
        string = str(i).split('.')[1]#.을 기준으로 뒤에있는 문자를 얻어낸다.(M(숫자))
        numbers = re.findall(r'\d+', string)#M(숫자) 형태에서 정규식을 이용하여 숫자만 발췌
        if i[0].value != None:#금칙어 단어가 None이 아니면(미입력이 아니면)
            prohibit_cell_index_list.append(numbers[0])#각 셀의 행번호를 리스트에 저장
        else:
            pass

    alternative_word_list = []
    for i in prohibit_cell_index_list:
        multi_prohibit_word_list = standard_sheet['M' + i].value.split(',')#한 개의 셀에 2개 이상의 금칙어가 지정되었을 경우 ,를 기준으로 분리
        alternative_word = standard_sheet['F' + i].value
        for j in range(len(multi_prohibit_word_list)):#한 개의 셀에 2개 이상의 금칙어가 지정된 경우 권장단어를 한 개의 셀에 지정된 금칙어 수만큼 맵핑
            alternative_word_list.append(alternative_word)
    return alternative_word_list


def put_alternative_word(alternative_word_list: list):
    #금칙어에 포함되어 있는 단어들의 권장단어(표준단어) 리스트를 M2열부터 저장
    for i in range(2, len(alternative_word_list) + 2):
        new_word_sheet[f'M{i}'] = alternative_word_list[i-2]
    return wb.save('C:/Users/MS/Downloads/스크립트용표준단어사전양식.xlsx')


if __name__=='__main__':
    prohibit_word = split_word(get_prohibit_word('M3', 'M2948'))
    standard_word = get_standard_word('F3', 'F2948')
    new_word = get_new_word('E2','E2947')
    alternative_word = get_alternative_word('M3','M2948')
    pure_new_word = get_pure_new_word(new_word, standard_word, prohibit_word)
    stwrds_in_prhwrds = get_stwrd_in_prhwrd(standard_word, prohibit_word)

    print("금칙어 리스트:", prohibit_word)
    print("표준단어 리스트:", standard_word)
    print("추가(검사)할 단어 리스트:", new_word)
    print("추가가능한 단어 리스트:", pure_new_word)
    print("표준단어 리스트이자 금칙어인 단어 리스트(중복이여서 제거 대상):", stwrds_in_prhwrds)
    put_pure_new_word(pure_new_word)
    put_stwrd_in_prhwrd(stwrds_in_prhwrds)
    put_prohibit_word(prohibit_word)
    put_alternative_word(alternative_word)