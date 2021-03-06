# import argparse
import os

from aiohttp import web
import asyncio

from manager import create_app

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('Library uvloop is not available')

# parser = argparse.ArgumentParser(description='Manager project')
# parser.add_argument('--host', help='Host to listen', default='0.0.0.0')
# parser.add_argument('--port', help='Port to accept connections', default=8080)
# parser.add_argument('--reload', action='store_true', help='Autoreload code on change')
# parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='Path to config file')

# parser.add_argument('--noauth_local_webserver', action='store_true', help='')

# args = parser.parse_args()

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

if __name__ == '__main__':
    def run():
        app = create_app()
        web.run_app(app, host=os.environ.get('HOST'), port=os.environ.get('PORT'))

    run()
