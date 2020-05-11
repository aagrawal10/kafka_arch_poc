import faust

BROKERS = '192.168.2.105:32775,192.168.2.105:32776'


class Greeting(faust.Record):
    from_name: str
    to_name: str


app = faust.App('hello-app', broker=BROKERS)
topic = app.topic('test_topic_faust', value_type=Greeting)


@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Hello from {greeting.from_name} to {greeting.to_name}')


@app.timer(interval=1.0)
async def example_sender(app):
    await hello.send(
        value=Greeting(from_name='Faust', to_name='you'),
    )

if __name__ == '__main__':
    app.main()
