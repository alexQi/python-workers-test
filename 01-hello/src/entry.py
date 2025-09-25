from workers import WorkerEntrypoint, Response
import requests
from requests.models import Response

class Default(WorkerEntrypoint):
    async def fetch(self, request, env):
        url = 'https://upbit.com/'
        resp: Response = requests.get(url, stream=True)
        remote_address = resp.raw._connection.sock.getpeername()
        return Response(remote_address)
