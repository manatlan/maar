#!/usr/local/bin/python3.7 -u
# -*- coding: utf-8 -*-
"""
This is just a runner DevApp/ChromeApp (useful during dev process)
as this runner use starlette+uvicorn, they should be availables
"""
import sys

# MODE="dev" 
MODE="phone"
# MODE="ar"


try:
    import uvicorn,starlette,PIL,mutagen
except:
    print("You will need a py version with: uvicorn,starlette,pillow,mutagen")
    sys.exit(-1)

#---------------------------------
from app import main
main.FOLDER="/tmp"  # overwrite config folder, for not cluttering my fs ;-)
#---------------------------------


if MODE=="phone":
    from htag.runners import ChromeApp as Runner           # need starlette+uvicorn !!!
    size=(400,800)
elif MODE=="ar":
    from htag.runners import ChromeApp as Runner           # need starlette+uvicorn !!!
    size=(1280,480)
else:
    from htag.runners import DevApp as Runner           # need starlette+uvicorn !!!
    size=None

app=Runner(main.App, file="/tmp/maar.aeff")

# the original app (maar) needs a tornado handler to answer "/get/<mp3>" paths
# so, as we use starlette, we just add our own route for that

from starlette.responses import FileResponse
async def serve(request):
    return FileResponse(request.path_params["path"])
app.add_route("/get/{path:path}", serve )

if __name__=="__main__":
    if size:
        app.run(size=size)  #chromeapp
    else:
        app.run()   # devapp
