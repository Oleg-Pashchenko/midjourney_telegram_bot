import requests
import json

url = "https://discord.com/api/v9/interactions"
headers = {
    "Content-Type": "application/json"
}
payload = {
    "type": 2,
    "application_id": "936929561302675456",
    "channel_id": "1078323027248427079",
    "session_id": "f1606e7b320f6802f9b47ce4c7fc5502",
    "data": {
        "version": "1077969938624553050",
        "id": "938956540159881230",
        "name": "imagine",
        "type": 1,
        "options": [
            {
                "type": 3,
                "name": "prompt",
                "value": "test"
            }
        ],
        "application_command": {
            "id": "938956540159881230",
            "application_id": "936929561302675456",
            "version": "1077969938624553050",
            "default_permission": True,
            "default_member_permissions": None,
            "type": 1,
            "nsfw": False,
            "name": "imagine",
            "description": "Create images with Midjourney",
            "dm_permission": True,
            "options": [
                {
                    "type": 3,
                    "name": "prompt",
                    "description": "The prompt to imagine",
                    "required": True
                }
            ]
        },
        "attachments": []
    },
    "nonce": "1079619741611458569"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.text)
