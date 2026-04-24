import json
import time

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from redis import Redis


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    redis = providers.Singleton(Redis, config.redis_host, config.redis_port.as_int())


def main():
    container = Container()
    container.wire(modules=[__name__])

    container.config.redis_host.from_env("REDIS_HOST")
    container.config.redis_port.from_env("REDIS_PORT")

    redis = container.redis()

    for text in (
        "As you can see",
        "messages are counted correctly",
        "by the counter that is injected",
        "into faststream handler",
        "via awesome dependency_injector library.",
    ):
        time.sleep(2)

        message = {"user": "John", "text": text}
        redis.publish("messages", json.dumps(message))


if __name__ == "__main__":
    main()

