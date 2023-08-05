import sys
from enum import Enum

class ForegroundColor(Enum):
    BLACK = ";30"
    RED = ";31"
    GREEN = ";32"
    YELLOW = ";33"
    BLUE = ";34"
    PURPLE = ";35"
    CYAN = ";36"
    WHITE = ";37"
    NONE = ""

class BackgroundColor(Enum):
    BLACK = ";40"
    RED = ";41"
    GREEN = ";42"
    YELLOW = ";43"
    BLUE = ";44"
    PURPLE = ";45"
    CYAN = ";46"
    WHITE = ";47"
    NONE = ""

class DisplayMode(Enum):
    NONE = "0"
    BOLD = "1"
    UNDERLINE = "2"
    NEGATIVE1 = "3"
    NEGATIVE2 = "5"

class MessageType(Enum):
    INFORMATION = "Information"
    ERROR = "Error"
    DEBUG = "Debug"
    VERBOSE = "Verbose"
    WARNING = "Warning"

class MessageWriter:

    __instance = None

    @staticmethod
    def getInstance():
        if MessageWriter.__instance == None:
            MessageWriter.__instance = MessageWriter()
        return MessageWriter.__instance

    def __init__(self, ansicodes: bool=True, debug: bool=False, verbose: bool=False, warning: bool=True):
        self.debug = debug
        self.verbose = verbose
        self.ansicodes = ansicodes
        self.warning = warning

    def __ansicode(self, displaymode: DisplayMode, foregroundcolor: ForegroundColor, backgroundcolor: BackgroundColor) -> str:
        return "\033[" + str(displaymode.value) + str(foregroundcolor.value) + str(backgroundcolor.value) + "m" if self.ansicodes else ""

    def __reset(self) -> str:
        return "\033[00m" if self.ansicodes else ""

    def __display(self, messagetype: MessageType=MessageType.INFORMATION):
        if messagetype == MessageType.WARNING:
            return self.warning
        elif messagetype == MessageType.DEBUG:
            return self.debug
        elif messagetype == MessageType.VERBOSE:
            return self.verbose
        else:
            return True
    
    def setANSICode(self, active: bool=False) -> None:
        self.ansicodes = active

    def setDebug(self, active: bool=False) -> None:
        self.debug = active

    def setVerbose(self, active: bool=False) -> None:
        self.verbose = active

    def setWarning(self, active: bool=False) -> None:
        self.warning = active

    def formatString(self, message: str, displaymode: DisplayMode=DisplayMode.NONE, \
            foregroundcolor: ForegroundColor=ForegroundColor.NONE, \
            backgroundcolor: BackgroundColor=BackgroundColor.NONE) -> str:
        return self.__ansicode(displaymode=displaymode, foregroundcolor=foregroundcolor, backgroundcolor=backgroundcolor) + message + self.__reset()

    def writeMessage(self, message: str, newline: bool=True, \
            messagetype: MessageType=MessageType.INFORMATION,
            displaymode: DisplayMode=DisplayMode.NONE, \
            foregroundcolor: ForegroundColor=ForegroundColor.NONE, \
            backgroundcolor: BackgroundColor=BackgroundColor.NONE) -> None:
        if not self.__display(messagetype=messagetype):
            return
        stream = sys.stderr if messagetype == MessageType.ERROR else sys.stdout
        stream.write(self.formatString(message=message, displaymode=displaymode, foregroundcolor=foregroundcolor, backgroundcolor=backgroundcolor))
        if newline:
            stream.write("\n")