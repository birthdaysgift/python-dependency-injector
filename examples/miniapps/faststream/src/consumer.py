import asyncio
from typing import Annotated

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from faststream import Depends, FastStream
from faststream.redis import RedisBroker
from pydantic import BaseModel


class Counter:
    def __init__(self):
        self.count = 0

    def next(self) -> int:
        self.count += 1
        return self.count


class Container(containers.DeclarativeContainer):
    counter = providers.Singleton(Counter)


broker = RedisBroker("redis://redis", logger=None)


class Message(BaseModel):
    user: str
    text: str


@broker.subscriber("messages")
@inject
async def handle_user_message(
    message: Message,
    counter: Annotated[
        Counter,
        Depends(
            Provide[Container.counter],
            cast=False,  # <-- this is the key part
        ),
    ],
) -> None:
    count = counter.next()
    print(f"Message #{count} from {message.user}: '{message.text}'")


async def main() -> None:
    container = Container()
    container.wire(modules=[__name__])

    await FastStream(broker, logger=None).run()


if __name__ == "__main__":
    asyncio.run(main())

