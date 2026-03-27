import requests
import os

def send_lunch_reminder():
    # 보안을 위해 URL은 직접 적지 않고 환경 변수에서 가져옵니다
    webhook_url = os.environ.get('MM_WEBHOOK_URL')
    
    payload = {
        "text": "@all 🍚 오늘 메뉴 확인하셨나요?\nhttps://bob-ssafy.vercel.app/board"
    }
    
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print("성공적으로 알림을 보냈습니다.")
    except Exception as e:
        print(f"전송 실패: {e}")

if __name__ == "__main__":
    send_lunch_reminder()
