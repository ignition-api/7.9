"""Provides classes that are fundamental to the design of the Java
programming language.
"""

from __future__ import print_function

__all__ = [
    "AutoCloseable",
    "CharSequence",
    "Class",
    "Enum",
    "Exception",
    "IllegalArgumentException",
    "NullPointerException",
    "Object",
    "RuntimeException",
    "String",
    "StringBuffer",
    "Thread",
    "Throwable",
]

import __builtin__ as builtins
import time
from typing import Any, Optional, TypeVar, Union

String = Union[str, unicode]
T = TypeVar("T")
U = TypeVar("U")


class AutoCloseable(object):
    def close(self):
        # type: () -> None
        raise NotImplementedError


class CharSequence(object):
    def charAt(self, index):
        # type: (int) -> str
        raise NotImplementedError

    def chars(self):
        pass

    def codePoints(self):
        pass

    @staticmethod
    def compare(cs1, cs2):
        # type: (CharSequence, CharSequence) -> int
        pass

    def length(self):
        # type: () -> int
        raise NotImplementedError

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        raise NotImplementedError

    def toString(self):
        # type: () -> String
        raise NotImplementedError


class Object(object):
    """Class Object is the root of the class hierarchy.

    Every class has Object as a superclass. All objects, including
    arrays, implement the methods of this class.
    """

    def equals(self, obj):
        # type: (Object) -> bool
        pass

    def getClass(self):
        # type: () -> Class
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def notify(self):
        # type: () -> None
        pass

    def notifyAll(self):
        # type: () -> None
        pass

    def toString(self):
        # type: () -> String
        return repr(self)

    def wait(self, timeoutMillis=0, nanos=0):
        # type: (long, int) -> None
        pass


class Class(Object):
    def asSubClass(self, clazz):
        # type: (Class) -> U
        pass

    def cast(self, obj):
        # type: (Object) -> T
        pass


class Enum(Object):
    def compareTo(self, o):
        pass

    def getDeclaringClass(self):
        pass

    def name(self):
        pass

    def ordinal(self):
        pass

    def valueOf(self, enumType, name):
        pass


class Throwable(Object, builtins.Exception):
    """The Throwable class is the superclass of all errors and
    exceptions in the Java language.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        self._cause = cause
        self._message = message
        builtins.Exception.__init__(self, message)

    @property
    def cause(self):
        # type: () -> Throwable
        return Throwable()

    def addSuppressed(self, exception):
        pass

    def fillInStackTrace(self):
        pass

    def getCause(self):
        return self.cause

    def getLocalizedMessage(self):
        return self.message

    def getMessage(self):
        return self.message

    def getStackTrace(self):
        pass

    def getSuppressed(self):
        pass

    def initCause(self, cause=None):
        # type: (Optional[Throwable]) -> None
        pass

    @property
    def message(self):
        # type: () -> str
        return "message"

    def printStackTrace(self, *args):
        pass

    def setStackTrace(self, stackTrace):
        pass


class Exception(Throwable):
    """The class Exception and its subclasses are a form of Throwable
    that indicates conditions that a reasonable application might want
    to catch.

    The class Exception and any subclasses that are not also subclasses
    of RuntimeException are checked exceptions. Checked exceptions need
    to be declared in a method or constructor's throws clause if they
    can be thrown by the execution of the method or constructor and
    propagate outside the method or constructor boundary.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(Exception, self).__init__(message, cause)


class RuntimeException(Exception):
    """RuntimeException is the superclass of those exceptions that can
    be thrown during the normal operation of the Java Virtual Machine.

    RuntimeException and its subclasses are unchecked exceptions.
    Unchecked exceptions do not need to be declared in a method or
    constructor's throws clause if they can be thrown by the execution
    of the method or constructor and propagate outside the method or
    constructor boundary.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(RuntimeException, self).__init__(message, cause)


class IllegalArgumentException(RuntimeException):
    """Thrown to indicate that a method has been passed an illegal or
    inappropriate argument.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(IllegalArgumentException, self).__init__(message, cause)


class NullPointerException(RuntimeException):
    """Thrown when an application attempts to use null in a case where
    an object is required.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(NullPointerException, self).__init__(message, cause)


class StringBuffer(Object, CharSequence):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def append(self, *args):
        pass

    def appendCodePoint(self, codePoint):
        # type: (int) -> StringBuffer
        pass

    def capacity(self):
        # type: () -> int
        pass

    def charAt(self, index):
        # type: (int) -> str
        pass

    def codePointAt(self, index):
        # type: (int) -> int
        pass

    def codePointBefore(self, index):
        # type: (int) -> int
        pass

    def codePointCount(self, beginIndex, endIndex):
        # type: (int, int) -> int
        pass

    def compareTo(self, another):
        # type: (StringBuffer) -> int
        pass

    def delete(self, start, end):
        # type: (int, int) -> StringBuffer
        pass

    def deleteCharAt(self, index):
        # type: (int) -> StringBuffer
        pass

    def ensureCapacity(self, minimumCapacity):
        # type: (int) -> None
        pass

    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        # type: (int, int, str, int) -> None
        pass

    def indexOf(self, string, fromIndex=0):
        # type: (str, int) -> int
        pass

    def insert(self, *args):
        pass

    def lastIndexOf(self, string, fromIndex=0):
        # type: (str, int) -> int
        pass

    def length(self):
        # type: () -> int
        pass

    def offsetByCodePoints(self, index, codePointOffset):
        # type: (int, int) -> int
        pass

    def replace(self, start, end, string):
        # type: (int, int, str) -> StringBuffer
        pass

    def reverse(self):
        # type: () -> StringBuffer
        pass

    def setCharAt(self, index, ch):
        # type: (int, str) -> None
        pass

    def setLength(self, newLength):
        # type: (int) -> None
        pass

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        pass

    def substring(self, start, end=-1):
        # type: (int, int) -> str
        pass

    def trimToSize(self):
        # type: () -> None
        pass


class Thread(Object):
    """A thread is a thread of execution in a program. The Java Virtual
    Machine allows an application to have multiple threads of execution
    running concurrently.

    Every thread has a name for identification purposes. More than one
    thread may have the same name. If a name is not specified when a
    thread is created, a new name is generated for it.

    Unless otherwise noted, passing a null argument to a constructor or
    method in this class will cause a NullPointerException to be thrown.
    """

    @staticmethod
    def sleep(millis):
        # type: (long) -> None
        time.sleep(millis // 1000)
