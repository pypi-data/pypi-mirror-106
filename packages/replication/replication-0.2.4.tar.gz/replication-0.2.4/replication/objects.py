from uuid import uuid4
from .constants import RP_COMMON
from deepdiff import DeepDiff, Delta
import logging
try:
    import _pickle as pickle
except ImportError:
    import pickle

def object_classes(type_id):
    """
    """
    return _TYPE_MAP.get(type_id)


class ReplicationObject(object):
    __slots__ = [
        '_sha'
    ]

    def _serialize(self):
        """ Convert the object into chunks of bytes
        """
        raise NotImplementedError()

    def _deserialize(self, chunks):
        """ Load chunks of to object
        """
        raise NotImplementedError()

    @staticmethod
    def from_raw_chunks(chunks):
        """ Reconstruct a replication object from chunks
        """
        type_num = chunks[0]
        obj = object_classes(type_num)()
        obj._deserialize(chunks)

        return obj

    def as_raw_chunks(self):
        return self._serialize()


class Commit(ReplicationObject):
    __slots__ = [
        'delta'     # deepdiff Delta
    ]

    type_num = 1

    def __init__(self):
        self.delta = None

    def _serialize(self):
        chunks = []
        chunks.append(self.type_num)
        chunks.append(self.delta.dumps())
        return chunks

    def _deserialize(self, chunks):
        self.delta = Delta(chunks[0])




class Node(ReplicationObject):
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
    type_num = 2

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

    def _serialize(self):
        chunks = []
        chunks.append(self.type_num)
        chunks.append(self.uuid.encode())
        chunks.append(self.owner.encode())
        chunks.append(pickle.dumps(self.dependencies, protocol=4))
        chunks.append(pickle.dumps(self.data, protocol=4))

        return chunks

    def _deserialize(self, chunks):
        self.uuid = chunks[1].decode()
        self.owner = chunks[2].decode()
        self.dependencies = pickle.loads(chunks[3])
        self.data = pickle.loads(chunks[4])

    def patch(self, patch):
        self.data = self.data + patch

    def add_dependency(self, dependency):
        if not self.dependencies:
            self.dependencies = []
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)

    def __repr__(self):
        return f" {self.uuid} - owner: {self.owner} - deps: {self.dependencies}"

OBJECT_CLASSES = (
    Commit,
    Node,
)

_TYPE_MAP = {}

for cls in OBJECT_CLASSES:
    _TYPE_MAP[cls.type_num] = cls
