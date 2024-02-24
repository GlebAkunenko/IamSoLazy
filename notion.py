import requests
import datetime as dt

from config import app_token, page_id

headers = {
    "Authorization": "Bearer " + app_token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def task_name(title):
    return {"title":
        [
            {
                "type": "text",
                "text": {
                    "content": title,
                    "link": None
                },
                "annotations": {
                    "bold": False,
                    "italic": False,
                    "strikethrough": False,
                    "underline": False,
                    "code": False,
                    "color": "default"
                },
                "plain_text": title,
                "href": None
            }
        ]}


def parent():
    return {"parent": {
        "type": "database_id",
        "database_id": "addd85d6-8e36-47eb-8770-0ae5b70d2ec7"
    }}


def push_task(title, due: dt.datetime):
    data = {
        "Task name": task_name(title),
        "Due": {"date": {"start": due.date().isoformat(), "end": None}}
    }
    create_url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": page_id}, "properties": data}
    res = requests.post(create_url, headers=headers, json=payload)
    if res.status_code != 200:
        raise Exception(res.reason)
    return res


