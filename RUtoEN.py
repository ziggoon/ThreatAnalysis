import json
import time
from deep_translator import GoogleTranslator

chatList = []
with open('big.json') as f:
    for jsonObj in f:
        _Dict = json.loads(jsonObj)
        chatList.append(_Dict)

oFile = open('output.json', 'w')
for line in chatList:
    try:
        translation = GoogleTranslator(source='auto', target='en').translate(line["body"])
        line["LANG-EN"] = translation
    except Exception as e:
        line["LANG-EN"] = "Error during Translation"
    oFile.write(json.dumps(line, ensure_ascii = False).encode('utf8').decode())
    print('line written ' + str(time.time()))	
print('conversion complete... ENG translation can be found in output.json')
oFile.close()
