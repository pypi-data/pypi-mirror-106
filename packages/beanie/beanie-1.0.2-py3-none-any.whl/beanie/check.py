from beanie import Document, PydanticObjectId
from typing import Optional


class Test(Document):
    t: str


async def get_test() -> Optional[Test]:
    return await Test.get(PydanticObjectId())


async def d(t: Test):
    print(t)


async def main():
    t = await get_test()
    await d(t)
