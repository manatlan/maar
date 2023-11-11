#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-
from app import main
main.FOLDER="/tmp"

from starlette.responses import FileResponse
from htag.runners import DevApp as Runner           # need starlette+uvicorn !!!
app=Runner(main.App)

async def serve(request):
    return FileResponse(request.path_params["path"])
app.add_route("/get/{path:path}", serve )

if __name__=="__main__":
    app.run()
