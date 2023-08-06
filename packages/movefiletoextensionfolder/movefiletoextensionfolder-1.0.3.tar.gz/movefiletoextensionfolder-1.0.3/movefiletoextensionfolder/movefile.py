import os
import pyttsx3
import logging as log


def setLogger():
    print("logger Set")
    log.basicConfig(level=log.DEBUG, filename='movefile.log', filemode='w',
                    format='%(asctime)s : %(levelname)s :: %(message)s')


def getExtName(file):
    return file.split(".")[-1]


def isDirOrFileExist(filePath):
    return os.path.exists(filePath)


def makeNewPath(filePath):
    log.debug("inside makeNewPath")
    print("given file name= ", filePath)
    log.debug("given file name= " + filePath)
    # abc.jpg >> abc_copy.jpg
    splitWord = filePath.split(".")
    dotExt = '.' + splitWord[-1]
    renamedDotExt = "_copy" + dotExt
    newWord = filePath.replace(dotExt, renamedDotExt)
    print("output file name= ", newWord)
    log.debug("output file name= " + newWord)
    return newWord


def voiceMsg(strVal):
    engine = pyttsx3.init()
    engine.setProperty('rate', 110)
    engine.setProperty('volume', 1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(strVal)
    engine.runAndWait()


def rename(source, destination, file):
    isCopied = True
    try:
        os.rename(source, destination)
        print(file, " copied  Successfully")
        log.debug(file + " copied  Successfully")
    except Exception as e:
        print(file, " copied Failed kindly close the file if Opened")
        log.error(file + " copied Failed kindly close the file if Opened")
        log.error(e)
        print("error Msg:", e)
        isCopied = False
        del e
    print("returning from rename function", isCopied)
    log.debug("returning from rename function "+str(isCopied))

    return isCopied


def moveFile(files, trgFol, pathVar, successvoicemsg):
    for file in files:
        ext = getExtName(file)
        extDirPath = trgFol + "\\" + ext

        filePath = extDirPath + "\\" + file
        src = pathVar + file

        isDirExist1 = isDirOrFileExist(extDirPath)
        print(filePath)
        if isDirExist1:
            if isDirOrFileExist(filePath):
                print(file, "file is already There")
                log.debug(file+" file is already There")
                newFilePath = makeNewPath(filePath)
                renamedFlag = False
                count = 20

                while not renamedFlag and count > 0:
                    count -= 1
                    print("renamed File name= ", newFilePath)
                    log.info("renamed File name= " + newFilePath)
                    renamedFlag = rename(src, newFilePath, file)
                    if not renamedFlag:
                        log.error("error while changing name appending one more _copy")
                        print("error while changing name appending one more _copy ")
                        newFilePath = makeNewPath(newFilePath)
            else:
                print(file, "file not Present wait moving......")
                log.info(file+"file not Present wait moving......")
                rename(src, filePath, file)

        else:
            print("dir not present wait making for you ......")
            log.info("dir not present wait making for you ......")
            try:
                os.mkdir(extDirPath)
                print("dir created")
                log.info("dir created")
                rename(src, filePath, file)
            except Exception as e:
                print(e)
                log.error("making directory ", e)
    size = len(files)

    if size > 0:
        voiceMsg(successvoicemsg)
    else:
        print("No Files To Move  bye bye ")
        log.info("No Files To Move  bye bye ")


def movefilefromsourcetodestination(source, target, successvoicemsg):
    setLogger()
    for path, dir, files in os.walk(source):
        moveFile(files, target, path, successvoicemsg)
        break


