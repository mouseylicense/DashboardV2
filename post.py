import requests
import re
room = input()
problem = input()
request =  	{'formID': '231834486300453', 'submissionID': '5642901395323475910', 'webhookURL': 'https://6352-2a0d-6fc0-826-600-b45f-a151-5701-40e8.ngrok-free.app/jotform', 'ip': '77.127.80.235', 'formTitle': 'Clone of דווח על תקלה לצוות מחשבים', 'pretty': 'שם:d d, תקלה:אין חיבור לרשת, חדר:שקטה, Type a question:ב    על ידי d d, Type a question:Nevobloch@gmail.com', 'username': 'nevobloch', 'rawRequest': '{"slug":"submit\\/231834486300453","q1_input1":{"first":"d","last":"d"},"q2_input2":"'+problem+'","q16_typeA16":"'+room+'","q5_input5":"","q8_typeA":"\\u05d1    \\u05e2\\u05dc \\u05d9\\u05d3\\u05d9 d d","q9_typeA9":"Nevobloch@gmail.com","preview":"true","validatedNewRequiredFieldIDs":"{\\"id_1\\":\\"d\\",\\"id_2\\":\\"ot\\",\\"id_16\\":\\"\\u05e9\\u05e7\\"}","path":"\\/submit\\/231834486300453"}', 'type': 'WEB'}
# room_unicode = input()
# print(str(room_unicode))
requests.post("http://127.0.0.1:5000/jotform",request)