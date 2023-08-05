class MjoolnException(Exception):
    # Core exception
    pass


class PixieInPipeline(MjoolnException):
    pass


class AngryElf(MjoolnException):
    # Raised when elf() is unable to figure out what you are trying to do
    pass


class CryptError(MjoolnException):
    pass


class BadSeed(MjoolnException):
    pass


class DicError(MjoolnException):
    pass


class DocError(MjoolnException):
    pass


class DocumentError(DocError):
    pass


class IdentityError(MjoolnException):
    pass


class BadWord(MjoolnException):
    pass


class NotAnInteger(BadWord):
    pass


class InvalidKey(MjoolnException):
    pass


class ZuluError(MjoolnException):
    pass


class AtomError(MjoolnException):
    pass


class PathError(MjoolnException):
    pass


class FileError(MjoolnException):
    pass


class ArchiveError(MjoolnException):
    pass


class FolderError(MjoolnException):
    pass


class TrunkError(MjoolnException):
    pass


class BrokenTrunk(TrunkError):
    pass


class RootError(MjoolnException):
    pass


class NoRoot(RootError):
    pass


class TreeError(MjoolnException):
    pass


class GroundProblem(RootError):
    pass
