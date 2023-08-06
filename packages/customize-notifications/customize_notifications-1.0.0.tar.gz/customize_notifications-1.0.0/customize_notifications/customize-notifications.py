import random
import time
import json
import hashlib
import requests


def generateNonceStr():
    return "".join(random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 16))


# def change_type(byte):
#     if isinstance(byte, bytes):
#         return str(byte, encoding="utf-8")
#     return json.JSONEncoder.default(byte)


def SubmitMessageRequest(sm):
    json_str = json.dumps(sm, sort_keys=True, indent=4, separators=(',', ':')).replace("\n", "").replace(
        " ", "")

    headers = {'content-type': 'application/json'}
    try:
        resp = requests.post("https://api.msg.launch.im/message", data=json_str, headers=headers)
    except ConnectionError as err:
        # handle err
        print(err)

    # examine response
    data = json.loads(resp.content)
    print(data)


class Message:
    msg_dict = {}
    p = {}
    sm = {}

    def __init__(self, title, msg_type, content, group=""):
        self.msg_dict['title'] = title
        self.msg_dict['msg_type'] = msg_type
        self.msg_dict['content'] = content
        if len(group) != 0:
            self.msg_dict['group'] = group

    def check(self):
        if len(self.msg_dict["title"]) > 100 or len(self.msg_dict["title"]) < 1:
            raise Exception("title count error")
        elif len(self.msg_dict["content"]) > 4000 or len(self.msg_dict["content"]) < 1:
            raise Exception("content count error")
        elif "group" in self.msg_dict and len(self.msg_dict["group"]) > 20:
            raise Exception("group count error")
        elif self.msg_dict["msg_type"] < 0 or self.msg_dict["msg_type"] > 4:
            raise Exception("msg type error")

    def sign(self, push_secret):
        signStrTmp = ""
        for k in sorted(self.p.keys()):
            if len(self.p[k]) == 0:
                continue
            else:
                signStrTmp += k + "=" + self.p[k] + "&"

        signStrTmp += "secret=" + push_secret
        return hashlib.sha256(signStrTmp.encode("utf-8")).hexdigest()

    def send_message(self, push_id, push_secret):
        timestamp = int(time.time())
        nonceStr = generateNonceStr()
        self.check()

        msgJson = json.dumps(self.msg_dict, indent=4, separators=(',', ':'), ensure_ascii=False).replace("\n",
                                                                                                         "").replace(
            " ", "")

        self.p = {"push_id": push_id, "nonce": nonceStr, "timestamp": str(timestamp),
                  "message": msgJson}
        signStr = self.sign(push_secret)

        self.sm = {"push_id": push_id, "nonce": nonceStr, "timestamp": timestamp,
                   "message": self.msg_dict, "sign": signStr}

        SubmitMessageRequest(self.sm)


if __name__ == '__main__':
    try:
        m = Message(title="test title", msg_type=0, content="test content", group="test group")
        m.send_message("your_id", "your_secret")
    except Exception as e:
        print(e)
