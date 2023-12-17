# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Float16Literal(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Float16Literal()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFloat16Literal(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Float16Literal
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Float16Literal
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(1)
def Float16LiteralStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddValue(builder, value): builder.PrependUint16Slot(0, value, 0)
def Float16LiteralAddValue(builder, value):
    """This method is deprecated. Please switch to AddValue."""
    return AddValue(builder, value)
def End(builder): return builder.EndObject()
def Float16LiteralEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)