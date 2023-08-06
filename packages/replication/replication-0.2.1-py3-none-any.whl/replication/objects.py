from uuid import uuid4
from .constants import RP_COMMON

try:
    import _pickle as pickle
except ImportError:
    import pickle

_TYPE_HEADER = b"type"


class BaseObject(object):
    __slots__ = [
        '_sha'
    ]

    def serialize(self):
        """ Convert the object into chunks of bytes
        """
        raise NotImplementedError()

    def deserialize(self, chunks):
        """ Load chunks of to object
        """
        raise NotImplementedError()


class Commit(BaseObject):
    __slots__ = [
    ]
    def __init__(self):
        pass



class Node(BaseObject):
    __slots__ = [
        'uuid',             # uuid used as key      (string)
        'data',             # dcc data ref          (DCC type)
        'instance',         # raw data              (json)
        'dependencies',     # dependencies array    (string)
        'owner',            # Data owner            (string)
        'buffer',           # Serialized local buffer (bytes)
        'state',            # Node state            (int)
        'sender',           # Node sender origin (client uuid)
        'delta'
        ]

    is_root = False


    def __init__(
            self,
            owner=None,
            instance=None,
            uuid=None,
            data=None,
            bytes=None,
            sender=None,
            dependencies=[], 
            state=-1):

        self.uuid = uuid if uuid else str(uuid4())
        self.owner = owner
        self.buffer = None
        self.state = state
        self.data = {}
        self.instance = instance
        self.data = data
        self.delta = bytes
        self.dependencies = dependencies
        self.sender = sender

    def serialize(self):
        chunks = []
        chunks.append(self.uuid.encode())
        chunks.append(self.owner.encode())
        chunks.append(pickle.dumps(self.dependencies, protocol=4))
        chunks.append(pickle.dumps(self.data, protocol=4))

        return chunks

    def deserialize(self, chunks):
        self.uuid = chunks[0].decode()
        self.owner = chunks[1].decode()
        self.dependencies = pickle.loads(chunks[2])
        self.data = pickle.loads(chunks[3])

    def patch(self, patch):
        self.data = self.data + patch

    def add_dependency(self, dependency):
        if not self.dependencies:
            self.dependencies = []
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)


    def __repr__(self):
        return f" {self.uuid} - owner: {self.owner} - deps: {self.dependencies}"
