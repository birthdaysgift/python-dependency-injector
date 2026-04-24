import asyncio
from typing import Annotated

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from faststream import Depends, FastStream
from faststream.redis import RedisBroker, RedisRouter
from pydantic import BaseModel


class Counter:
    def __init__(self):
        self.count = 0

    def next(self) -> int:
        self.count += 1
        return self.count


class Container(containers.DeclarativeContainer):
    counter = providers.Singleton(Counter)

    config = providers.Configuration()

    broker = providers.Singleton(RedisBroker, config.redis_url, logger=None)
    app = providers.Factory(FastStream, broker, logger=None)


class Message(BaseModel):
    user: str
    text: str


router = RedisRouter()


@router.subscriber("messages")
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

    container.config.redis_url.from_env("REDIS_URL")

    broker = container.broker()
    broker.include_router(router)

    app = container.app()
    await app.run()


if __name__ == "__main__":
    asyncio.run(main())

