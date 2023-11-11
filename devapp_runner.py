#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

"""
This is just a runner DevApp (useful during dev process)
as this runner use starlette+uvicorn, they should be availables
"""

import sys
try:
    import uvicorn,starlette,PIL,mutagen
except:
    print("You will need a py version with: uvicorn,starlette,PIL,mutagen")
    sys.exit(-1)

from app import main
main.FOLDER="/tmp"  # overwrite config folder, for not cluttering my fs ;-)

from starlette.responses import FileResponse
from htag.runners import DevApp as Runner           # need starlette+uvicorn !!!
app=Runner(main.App)

# the original app (maar) needs a tornado handler to answer "/get/<mp3>" paths
# so, as we use starlette, we just add our own route for that

async def serve(request):
    return FileResponse(request.path_params["path"])
app.add_route("/get/{path:path}", serve )

if __name__=="__main__":
    app.run()
