# ##### BEGIN GPL LICENSE BLOCK #####
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####


import logging
from deepdiff import DeepDiff, Delta
import json
import io
from uuid import uuid4
import sys
import zmq
import math
import logging

try:
    import _pickle as pickle
except ImportError:
    import pickle

import traceback

from .constants import (
    ADDED, COMMITED,
    FETCHED, UP, MODIFIED, DIFF_BINARY, DIFF_JSON)
from .exception import (NetworkFrameError, DataError,
                        StateError, UnsupportedTypeError)
from .utils import get_state_str

CHUNK_SIZE = 2500000000

class ReplicatedCommandFactory(object):
    """
    Manage the data types implementations.

    """

    def __init__(self):
        self.supported_types = []

        self.register_type(RepDeleteCommand, RepDeleteCommand)
        self.register_type(RepRightCommand, RepRightCommand)
        self.register_type(RepConfigCommand, RepConfigCommand)
        self.register_type(RepSnapshotCommand, RepSnapshotCommand)
        self.register_type(RepServerSnapshotCommand, RepServerSnapshotCommand)
        self.register_type(RepAuthCommand, RepAuthCommand)
        self.register_type(RepDisconnectCommand, RepDisconnectCommand)
        self.register_type(RepKickCommand, RepKickCommand)
        self.register_type(RepUpdateClientsState, RepUpdateClientsState)
        self.register_type(RepUpdateUserMetadata, RepUpdateUserMetadata)

    def register_type(
            self,
            source_type,
            implementation):
        """
        Register a new replicated datatype implementation
        """
        self.supported_types.append(
            (source_type, implementation))

    def match_type_by_name(self, type_name):
        for stypes, implementation in self.supported_types:
            if type_name == implementation.__name__:
                return implementation
        logging.error(f"{type_name} not supported for replication")

    def get_implementation_from_object(self, data):
        return self.match_type_by_instance(data)

    def get_implementation_from_net(self, type_name):
        """
        Re_construct a new replicated value from serialized data
        """
        return self.match_type_by_name(type_name)


class ReplicatedCommand():
    def __init__(
            self,
            owner=None,
            data=None):
        assert(owner)

        self.owner = owner
        self.data = data
        self.str_type = type(self).__name__

    def push(self, socket):
        """
        Here send data over the wire:
            - _serialize the data
            - send them as a multipart frame thought the given socket
        """
        data = pickle.dumps(self.data, protocol=4)
        owner = self.owner.encode()
        type = self.str_type.encode()

        socket.send_multipart([owner, type, data])

    @classmethod
    def fetch(cls, socket, factory=None):
        """
        Here we reeceive data from the wire:
            - read data from the socket
            - reconstruct an instance
        """

        owner, str_type, data = socket.recv_multipart(0)

        str_type = str_type.decode()
        owner = owner.decode()
        data = pickle.loads(data)

        implementation = factory.get_implementation_from_net(str_type)

        instance = implementation(owner=owner, data=data)
        return instance

    @classmethod
    def server_fetch(cls, socket, factory=None):
        """
        Here we reeceive data from the wire:
            - read data from the socket
            - reconstruct an instance
        """
        instance = None
        frame = socket.recv_multipart(0)

        if len(frame) != 4:
            logging.error(
                f"Malformed command frame received (len: {len(frame)}/4)")
            raise NetworkFrameError("Error fetching command")
        else:
            str_type = frame[2].decode()
            owner = frame[1].decode()
            data = pickle.loads(frame[3])

            implementation = factory.get_implementation_from_net(str_type)

            instance = implementation(owner=owner, data=data)
            instance.sender = frame[0]

        return instance

    def execute(self, graph):
        raise NotImplementedError()


class RepDeleteCommand(ReplicatedCommand):
    def execute(self, graph):
        assert(self.data)

        if graph and self.data in graph.keys():
            # Clean all reference to this node
            for key, value in graph.items():
                if value.dependencies and self.data in value.dependencies:
                    value.dependencies.remove(self.data)
            # Remove the node itself
            del graph[self.data]


class RepRightCommand(ReplicatedCommand):
    def execute(self, graph):
        assert(self.data)

        if graph and self.data['uuid'] in graph.keys():
            graph[self.data['uuid']].owner = self.data['owner']


class RepConfigCommand(ReplicatedCommand):
    pass


class RepSnapshotCommand(ReplicatedCommand):
    pass


class RepServerSnapshotCommand(ReplicatedCommand):
    pass


class RepAuthCommand(ReplicatedCommand):
    pass


class RepDisconnectCommand(ReplicatedCommand):
    pass


class RepKickCommand(ReplicatedCommand):
    pass


class RepUpdateClientsState(ReplicatedCommand):
    pass


class RepUpdateUserMetadata(ReplicatedCommand):
    pass
