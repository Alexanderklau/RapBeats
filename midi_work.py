# coding: utf-8

__author__ = "lau.wenbo"


from music21 import converter, instrument

def Get_midi_msg():
    # 读取midi文件,输出流
    stream = converter.parse("test.mid")

    # 获取所有乐器
    parts = instrument.partitionByInstrument(stream)

    if parts:
        for i in parts.parts:
            print(i.recurse())



if __name__ == "__main__":
    Get_midi_msg()