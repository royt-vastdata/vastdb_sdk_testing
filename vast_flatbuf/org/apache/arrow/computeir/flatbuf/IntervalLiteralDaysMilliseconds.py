# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuf

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class IntervalLiteralDaysMilliseconds(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = IntervalLiteralDaysMilliseconds()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsIntervalLiteralDaysMilliseconds(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # IntervalLiteralDaysMilliseconds
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # IntervalLiteralDaysMilliseconds
    def Days(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # IntervalLiteralDaysMilliseconds
    def Milliseconds(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(2)
def IntervalLiteralDaysMillisecondsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddDays(builder, days): builder.PrependInt32Slot(0, days, 0)
def IntervalLiteralDaysMillisecondsAddDays(builder, days):
    """This method is deprecated. Please switch to AddDays."""
    return AddDays(builder, days)
def AddMilliseconds(builder, milliseconds): builder.PrependInt32Slot(1, milliseconds, 0)
def IntervalLiteralDaysMillisecondsAddMilliseconds(builder, milliseconds):
    """This method is deprecated. Please switch to AddMilliseconds."""
    return AddMilliseconds(builder, milliseconds)
def End(builder): return builder.EndObject()
def IntervalLiteralDaysMillisecondsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)