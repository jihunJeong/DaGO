from library import *

def change_html_expression(row):
    '''
        Args:
            row : 변환하고자 하는 dataframe의 row
        
        Returns:
            row : html expression 변환 완료된 row
    '''
    def _change(element):
        element = element.replace("&nbsp;", " ")
        element = element.replace("&lt;", "<")
        element = element.replace("&gt;", ">")
        element = element.replace("&amp;", "&")
        element = element.replace("&quot;", '"')
        element = element.replace("&#035;", "#")
        element = element.replace("&#039;", "'")
        return element
        
    for idx, element in enumerate(row):
        if isinstance(element, str):
            element = _change(element)
        elif isinstance(element, list):
            li = []
            for string in element:
                li.append(_change(string))
            element = li
        row[idx] = element
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

def merge_file(data_dir, result_dir, filename):
    '''
        Note:
            주어진 file name에 대한 여러 나뉜 파일 Merge
    '''
    file_list = os.listdir(data_dir)
    target_list = [file for file in file_list if file.startswith(f"{filename}")]
    pre_df = pd.DataFrame()
    for target in target_list:
        df = pd.read_json(data_dir+f"{target}")
        pre_df = pd.concat([pre_df, df])
    pre_df.index = np.arange(1, len(pre_df)+1)
    pre_df.to_json(result_dir+f"/result_{filename}.json")