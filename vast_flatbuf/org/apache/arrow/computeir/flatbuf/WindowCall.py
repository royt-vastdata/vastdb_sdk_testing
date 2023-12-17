# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# An expression representing a window function call.
class WindowCall(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = WindowCall()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsWindowCall(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # WindowCall
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # The expression to operate over
    # WindowCall
    def Expression(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.Expression import Expression
            obj = Expression()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # The kind of window frame
    # WindowCall
    def Kind(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Partition keys
    # WindowCall
    def Partitions(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.Expression import Expression
            obj = Expression()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WindowCall
    def PartitionsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WindowCall
    def PartitionsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Sort keys
    # WindowCall
    def Orderings(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from vast_flatbuf.org.apache.arrow.computeir.flatbuf.SortKey import SortKey
            obj = SortKey()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # WindowCall
    def OrderingsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # WindowCall
    def OrderingsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # WindowCall
    def LowerBoundType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Lower window bound
    # WindowCall
    def LowerBound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # WindowCall
    def UpperBoundType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Upper window bound
    # WindowCall
    def UpperBound(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def Start(builder): builder.StartObject(8)
def WindowCallStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddExpression(builder, expression): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(expression), 0)
def WindowCallAddExpression(builder, expression):
    """This method is deprecated. Please switch to AddExpression."""
    return AddExpression(builder, expression)
def AddKind(builder, kind): builder.PrependUint8Slot(1, kind, 0)
def WindowCallAddKind(builder, kind):
    """This method is deprecated. Please switch to AddKind."""
    return AddKind(builder, kind)
def AddPartitions(builder, partitions): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(partitions), 0)
def WindowCallAddPartitions(builder, partitions):
    """This method is deprecated. Please switch to AddPartitions."""
    return AddPartitions(builder, partitions)
def StartPartitionsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WindowCallStartPartitionsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartPartitionsVector(builder, numElems)
def AddOrderings(builder, orderings): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(orderings), 0)
def WindowCallAddOrderings(builder, orderings):
    """This method is deprecated. Please switch to AddOrderings."""
    return AddOrderings(builder, orderings)
def StartOrderingsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def WindowCallStartOrderingsVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOrderingsVector(builder, numElems)
def AddLowerBoundType(builder, lowerBoundType): builder.PrependUint8Slot(4, lowerBoundType, 0)
def WindowCallAddLowerBoundType(builder, lowerBoundType):
    """This method is deprecated. Please switch to AddLowerBoundType."""
    return AddLowerBoundType(builder, lowerBoundType)
def AddLowerBound(builder, lowerBound): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(lowerBound), 0)
def WindowCallAddLowerBound(builder, lowerBound):
    """This method is deprecated. Please switch to AddLowerBound."""
    return AddLowerBound(builder, lowerBound)
def AddUpperBoundType(builder, upperBoundType): builder.PrependUint8Slot(6, upperBoundType, 0)
def WindowCallAddUpperBoundType(builder, upperBoundType):
    """This method is deprecated. Please switch to AddUpperBoundType."""
    return AddUpperBoundType(builder, upperBoundType)
def AddUpperBound(builder, upperBound): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(upperBound), 0)
def WindowCallAddUpperBound(builder, upperBound):
    """This method is deprecated. Please switch to AddUpperBound."""
    return AddUpperBound(builder, upperBound)
def End(builder): return builder.EndObject()
def WindowCallEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)