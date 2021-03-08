import requests

def call_zalo_api(file):
    url = "https://zalo.ai/api/demo/v1/asr"

    payload={}
    files=[
    ('file',(file,open('/mnt/f5d194a1-b929-47ba-99cc-b61f779d871a/ML/Gendata-tools/split_audio/split/' + file,'rb'),'audio/wav'))
    ]
    headers = {
    'authority': 'zalo.ai',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.344',
    'origin': 'https://zalo.ai',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://zalo.ai/experiments/automation-speech-recognition',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'zai_did=8k9uAj3FNiTevcSSryzXoYYo64d1psxAAhOMIJCp; __zi=2000.SSZzejyD0jydXQcYsa00d3xBfxgO71AM8Ddbg8uE7SWhtAtXZ0yHo2dTfQYC3161ATAbgeW26O8u.1; _zlang=vn; _ga=GA1.2.1645617531.1615191759; _gid=GA1.2.701747411.1615191759; fpsend=149554; _gat_gtag_UA_158812682_2=1'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.json()['result']['text']