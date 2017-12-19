import orm_o, asyncio, sys
from models_o import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm_o.create_pool(loop=loop, user='root', password='123456', db='pyblog')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()


# for x in test():
#     pass
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
