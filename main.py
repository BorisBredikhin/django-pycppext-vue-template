import aiohttp
import aiohttp.web
import argparse
import cppcheckers
from readconfig import load_config

from database.database import database, init

parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, help="path to configuration file")

args = parser.parse_args()

config = load_config(open(args.config, 'r'))

init()

database[0].Base.metadata.create_all(bind=database[0].engine)

app = aiohttp.web.Application()

routes = aiohttp.web.RouteTableDef()

@routes.get("/")
async def handle(request):
    return aiohttp.web.Response(text="hello")

app.add_routes(routes)

if __name__ == '__main__':
    cppcheckers.printMessage("kkk")
    aiohttp.web.run_app(app, host=config.addr.host, port=config.addr.port)