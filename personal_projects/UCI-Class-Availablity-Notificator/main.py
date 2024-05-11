from bs4 import BeautifulSoup
from twilio.rest import Client
import requests
from typing import List 
import json
from sinch import Client
import schedule
import time
from datetime import datetime

TARGET = [""]

def main():
    with open("records.txt",'a') as file:
        file.write("Current time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8,ko;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.reg.uci.edu',
        'Referer': 'https://www.reg.uci.edu/perl/WebSoc',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'YearTerm': '2024-14',
        'ShowComments': 'on',
        'ShowFinals': 'on',
        'Breadth': 'ANY',
        'Dept': 'COMPSCI',
        'CourseNum': '147',
        'Division': 'ANY',
        'CourseCodes': '',
        'InstrName': '',
        'CourseTitle': '',
        'ClassType': 'ALL',
        'Units': '',
        'Modality': '',
        'Days': '',
        'StartTime': '',
        'EndTime': '',
        'MaxCap': '',
        'FullCourses': 'ANY',
        'FontSize': '100',
        'CancelledCourses': 'Exclude',
        'Bldg': '',
        'Room': '',
        'Submit': 'Display Web Results',
    }

    # Note: You might need to handle cookies manually if required by the website
    response = requests.post('https://www.reg.uci.edu/perl/WebSoc', headers=headers, data=data)

    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all rows with 'valign="top"'
    rows_with_valign_top = soup.find_all('tr', valign="top")
    
    # print(parse_course_name(str(rows_with_valign_top[0].find_all('td')[-1])))

    # for row in rows_with_valign_top[1:]:
    #     # Find the last <td> of each row
    #     first_td = row.find_all('td')[0]
    #     second_td = row.find_all('td')[1]
    #     last_td = row.find_all('td')[-1]
    #     print( first_td.get_text(strip=True) +  '\t' + second_td.get_text(strip=True) + '\t' + last_td.get_text(strip=True))
        
    lecture_available = check_if_it_available(rows_with_valign_top[1].find_all('td')[-1].get_text(strip=True))
    lab_result_list = {}
    for row in rows_with_valign_top[2:]:
        if row.find_all('td')[1].get_text(strip=True).lower() == "lab":
            lab_result_list[row.find_all('td')[0].get_text(strip=True)] = (check_if_it_available(row.find_all('td')[-1].get_text(strip=True)))
    
    course_name = parse_course_name(str(rows_with_valign_top[0].find_all('td')[-1])) 
    lec_code = rows_with_valign_top[1].find_all('td')[0].get_text(strip=True)
    if lecture_available == 1 or lecture_available == 2:
        for key, value in lab_result_list.items():
            if value >= 1:
                body = "Hey, your class " + course_name + " is available to enroll or waitlist, please check \nLec" + ": " + str(lec_code) + "\nLab: " + str(key) + "\n"
                send_msg(TARGET,body)
                print("SEND")
                break


def check_if_it_available(status: str):
    if (status.lower() == "full"):
        return 0
    elif (status.lower() == "waitl"):
        return 1
    else:
        return 2

def parse_course_name(html_snippet:str ) -> str:
    # Parse the HTML
    soup = BeautifulSoup(html_snippet, 'lxml')

    # Find the <td> tag with class "CourseTitle"
    course_title_td = soup.find('td', class_='CourseTitle')

    # Extract and clean the text
    if course_title_td:
        text_parts = []

        # Iterate through elements to separate text and <font> tag content
        for content in course_title_td.contents:
            if content.name == 'font':
                # Get text directly from <font> tag
                text_parts.append(content.get_text(strip=True))
            elif content.string:
                # Get string values and strip spaces
                stripped_text = content.string.strip()
                if stripped_text:
                    text_parts.append(stripped_text)

        # Join the parts to form the full title
        return ' '.join(text_parts)

    else:
        print("Course title not found.")

def send_msg(target: List, body:str):
    sinch_client = Client(
    key_id="",
    key_secret="",
    project_id=""
    )

    send_batch_response = sinch_client.sms.batches.send(
        body= body,
        to=target,
        from_="12085689239",
        delivery_report="none"
    )

    print(send_batch_response)
    # # Endpoint URL from the curl command
    # url = "https://sms.api.sinch.com/xms/v1/97ba53e0a511456fba1c18e5e441fea7/batches"

    # # Headers
    # headers = {
    #     "Authorization": "Bearer e39e44f885724c1d89f2d438c2985196",
    #     "Content-Type": "application/json"
    # }

    # # Data payload
    # data = {
    #     "from": "12085689239",
    #     "to": target,
    #     "body": body
    # }

    # # Making the POST request
    # response = requests.post(url, headers=headers, data=json.dumps(data))

    # # Checking if the request was successful
    # if response.status_code == 200:
    #     print("Message sent successfully")
    # else:
    #     print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")

schedule.every(1).hours.do(main)

while True:
    schedule.run_pending()
    time.sleep(3500)

# if __name__ == "__main__":
#     main()
    # send_msg(["17148242592"],"HELLO WORLD FROM VISAAAAAA PYTHONNNNN")
