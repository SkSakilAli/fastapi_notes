
class CustomLoggingMiddleware:
    def __int__(self, app, prefix="LOG"):
        self.app = app
        self.prefix = prefix

    async def __call__(self, scope, receive, send):
        print(f"{self.prefix}: Before processing request (scope: {
            scope['type']})")
        await self.app(scope, receive, send)
        print(f"{self.prefix}: After processing request")

        #scope is a dictionary with incoming request metadata
        #receive is async function that also contains any data with request
        #send an async function that have the response that is send to client