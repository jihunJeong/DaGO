from library import *

def change_html_expression(row):
    '''
        Args:
            row : 변환하고자 하는 dataframe의 row
        
        Returns:
            row : html expression 변환 완료된 row
    '''
    for column in row:
        for idx, element in enumerate(row[column]):
            element = element.replace("&nbsp;", " ")
            element = element.replace("&lt;", "<")
            element = element.replace("&gt;", ">")
            element = element.replace("&amp;", "&")
            element = element.replace("&quot;", '"')
            element = element.replace("&#035;", "#")
            element = element.replace("&#039;", "'")
            row[column][idx] = element
    return row

def change_date_format(element):
    '''
        Args:
            element : Meta Data에서 date에 있는 값

        Returns:
            element : yyyymmdd 형식에 date
        
        Note:
            값이 존재하지 않는다면 Default Value 20010101
    '''
    mToN = {"January":"01", "February":"02", "March":"03", "April":"04", "May":"05", "June":"06",
            "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12"}

    if element:
        if not isinstance(element, str) or len(element.split()) != 3 or "div" in str(element):
            element = "20010101"
        else :
            m, d, year = element.split()
            if m not in mToN.keys():
                element = "20010101"
            else :
                element = year+mToN[m]+"0"*(3-len(d))+d[:-1]
    else :
        element = "20010101"

    return element

def empty2null(row):
    '''
        Note:
            Dataframe의 row가 들어왔을 때 만약 빈 문자열이라면 None Value로 치환
    '''
    for column in row:
        if not row[column]:
            row[column] = None
    return row