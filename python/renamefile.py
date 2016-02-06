import os
def renamefile():
    list=os.listdir(r"/home/shekhar/tmp/prank")
    savepath=os.getcwd()
    os.chdir(r"/home/shekhar/tmp/prank")

    for name in list:
        os.rename(name,name.translate(None,"1234567890"))
    os.chdir(savepath)


renamefile()