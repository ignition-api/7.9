# Copyright (C) 2018-2020
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev
"""File Functions
The following functions give you access to read and write to files.
"""

__all__ = [
    "fileExists",
    "getTempFile",
    "openFile",
    "openFiles",
    "readFileAsBytes",
    "readFileAsString",
    "saveFile",
    "writeFile",
]


def fileExists(filepath):
    """Checks to see if a file or folder at a given path exists.

    Args:
        filepath (str): The path of the file or folder to check.

    Returns:
        bool: True (1) if the file/folder exists, False (0) otherwise.
    """
    import os.path

    return os.path.isfile(filepath)


def getTempFile(extension):
    """Creates a new temp file on the host machine with a certain
    extension, returning the path to the file. The file is marked to be
    removed when the Java VM exits.

    Args:
        extension (str): An extension, like ".txt", to append to the end
            of the temporary file.

    Returns:
        str: The path to the newly created temp file.
    """
    import tempfile

    return tempfile.NamedTemporaryFile(suffix="." + extension).name


def openFile(extension=None, defaultLocation=None):
    """Shows an "Open File" dialog box, prompting the user to choose a
    file to open. Returns the path to the file that the user chose, or
    None if the user canceled the dialog box. An extension can
    optionally be passed in that sets the filetype filter to that
    extension.

    Args:
        extension (str): A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation (str): A folder location, like "C:\\MyFiles", to
            use as the starting location for the file chooser. Optional.

    Returns:
        str: The path to the selected file, or None if canceled.
    """
    print(extension, defaultLocation)
    return None


def openFiles(extension=None, defaultLocation=None):
    """Shows an "Open File" dialog box, prompting the user to choose a
    file or files to open. Returns the paths to the files that the user
    chooses, or None if the user canceled the dialog box. An extension
    can optionally be passed in that sets the filetype filter to that
    extension.

    Args:
        extension (str): A file extension, like "pdf", to try to open.
            Optional.
        defaultLocation (str): A folder location, like "C:\\MyFiles", to
            use as the starting location for the file chooser. Optional.

    Returns:
        list[str]: The paths to the selected files, or None if canceled.
    """
    print(extension, defaultLocation)
    return None


def readFileAsBytes(filepath):
    """Opens the file found at path filename, and reads the entire file.
    Returns the file as an array of bytes. Commonly this array of bytes
    is uploaded to a database table with a column of type BLOB (Binary
    Large OBject). This upload would be done through an INSERT or UPDATE
    SQL statement run through the system.db.runPrepUpdate function. You
    could also write the bytes to another file using the
    system.file.writeFile function, or send the bytes as an email
    attachment using system.net.sendEmail.

    Args:
        filepath (str): The path of the file to read.

    Returns:
        bytearray: The contents of the file as an array of bytes.
    """
    with open(filepath, "rb") as f:
        return f.read()


def readFileAsString(filepath, encoding="UTF-8"):
    """Opens the file found at path filename, and reads the entire file.
    Returns the file as a string. Common things to do with this string
    would be to load it into the text property of a component, upload it
    to a database table, or save it to another file using
    system.file.writeFile function.

    Args:
        filepath (str): The path of the file to read.
        encoding (str): The character encoding of the file to be read.
            Will throw an exception if the string does not represent a
            supported encoding. Common encodings are "UTF-8",
            "ISO-8859-1" and "US-ASCII". Optional.

    Returns:
        str: The contents of the file as a string.
    """
    import io

    with io.open(filepath, "r", encoding=encoding) as f:
        return f.read()


def saveFile(filename, extension=None, typeDesc=None):
    """Prompts the user to save a new file named filename. The optional
    extension and typeDesc arguments can be added to be used as a type
    filter. If the user accepts the save, the path to that file will be
    returned. If the user cancels the save, None will be returned.

    Args:
        filename (str): A file name to suggest to the user.
        extension (str): The appropriate file extension, like "jpeg",
            for the file. Optional.
        typeDesc (str): A description of the extension, like "JPEG
            Image". Optional.

    Returns:
        str: The path to the file that the user decided to save to, or
            None if they canceled.
    """
    print(filename, extension, typeDesc)
    return None


def writeFile(filepath, data, append=False):
    """Writes the given data to the file at file path filename. If the
    file exists, the append argument determines whether or not it is
    overwritten (the default) or appended to. The data argument can be
    either a string or an array of bytes (commonly retrieved from a BLOB
    in a database or read from another file using
    system.file.readFileAsBytes).

    Args:
        filepath (str): The path of the file to write to.
        data (object): The character or binary content to write to the
            file.
        append (bool): If True(1), the file will be appended to if it
            already exists. If False(0), the file will be overwritten if
            it exists. The default is False(0). Optional.
    """
    print(filepath, data, append)
