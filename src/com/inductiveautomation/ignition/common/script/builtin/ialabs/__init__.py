from __future__ import print_function

__all__ = [
    "BrowseTag",
    "OPCBrowseTag",
    "TagAlarmDefinition",
    "TagAlarmProperty",
]

from java.lang import Object


class BrowseTag(Object):
    def __init__(
        self,
        name=None,
        path=None,
        fullPath=None,
        type=None,
        valueSource=None,
        dataType=None,
    ):
        super(BrowseTag, self).__init__()
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type
        self.valueSource = valueSource
        self.dataType = dataType

    def getDataType(self):
        return self.dataType

    def getFullPath(self):
        return self.fullPath

    def getPath(self):
        return self.path

    def getTagType(self):
        return self.type

    def getValueSource(self):
        return self.valueSource

    def isDB(self):
        print(self)
        return True

    def isExpression(self):
        print(self)
        return True

    def isFolder(self):
        print(self)
        return True

    def isMemory(self):
        print(self)
        return True

    def isOPC(self):
        print(self)
        return True

    def isQuery(self):
        print(self)
        return True

    def isUDT(self):
        print(self)
        return True

    def toString(self):
        pass


class OPCBrowseTag(Object):
    def __init__(
        self,
        opcServer=None,
        type=None,
        displayName=None,
        displayPath=None,
        dataType=None,
        opcItemPath=None,
    ):
        super(OPCBrowseTag, self).__init__()
        self.opcServer = opcServer
        self.type = type
        self.displayName = displayName
        self.displayPath = displayPath
        self.dataType = dataType
        self.opcItemPath = opcItemPath

    def getDataType(self):
        return self.dataType

    def getDisplayName(self):
        return self.displayName

    def getDisplayPath(self):
        return self.displayPath

    def getOpcItemPath(self):
        return self.opcItemPath

    def getOpcServer(self):
        return self.opcServer

    def getType(self):
        return self.type


class TagAlarmDefinition(Object):
    def __init__(self, alarm, alarmProperties):
        self.alarm = alarm
        self.alarmProperties = alarmProperties

    def getAlarmProperties(self):
        print(self)
        return TagAlarmProperty()


class TagAlarmProperty(Object):
    def __init__(self, property=None, value=None, type=None):
        self.property = property
        self.type = type
        self.value = value
