# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Limit operation
class Limit(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Limit()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsLimit(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Limit
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # An identifiier for the relation. The identifier should be unique over the
    # entire plan. Optional.
    # Limit
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.RelId import RelId
            obj = RelId()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Child relation
    # Limit
    def Rel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.Relation import Relation
            obj = Relation()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Starting index of rows
    # Limit
    def Offset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # The maximum number of rows of output.
    # Limit
    def Count(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(4)
def LimitStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddId(builder, id): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)
def LimitAddId(builder, id):
    """This method is deprecated. Please switch to AddId."""
    return AddId(builder, id)
def AddRel(builder, rel): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(rel), 0)
def LimitAddRel(builder, rel):
    """This method is deprecated. Please switch to AddRel."""
    return AddRel(builder, rel)
def AddOffset(builder, offset): builder.PrependUint32Slot(2, offset, 0)
def LimitAddOffset(builder, offset):
    """This method is deprecated. Please switch to AddOffset."""
    return AddOffset(builder, offset)
def AddCount(builder, count): builder.PrependUint32Slot(3, count, 0)
def LimitAddCount(builder, count):
    """This method is deprecated. Please switch to AddCount."""
    return AddCount(builder, count)
def End(builder): return builder.EndObject()
def LimitEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)