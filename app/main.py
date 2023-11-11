# -*- coding: utf-8 -*-

from htag import Tag
import math,os,json,sys

# the folder, where app/apk can save data (parent folder)
FOLDER=os.path.join( os.path.dirname(os.path.abspath(os.path.realpath(sys.argv[0]))), ".." )

#############################################################################
class App(Tag.body):

    def init(self):
        self.cfg= os.path.join(FOLDER,"maar.json")
        self+="MAAR"

        #TODO: it miss all the code for now ;-)

if __name__=="__main__":
    from htag.runners import AndroidApp
    AndroidApp( App ).run()

#=================================================================================
# from htag.runners import DevApp as Runner
# app=Runner(App)
# if __name__=="__main__":
#     app.run()
