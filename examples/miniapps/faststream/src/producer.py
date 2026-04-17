import json
import time

import redis


def main():
    client = redis.Redis(host="redis", port=6379)

    for text in (
        "As you can see",
        "messages are counted correctly",
        "by the counter that is injected",
        "into faststream handler",
        "via awesome dependency_injector library.",
    ):
        time.sleep(2)

        message = {"user": "John", "text": text}
        client.publish("messages", json.dumps(message))


if __name__ == "__main__":
    main()

