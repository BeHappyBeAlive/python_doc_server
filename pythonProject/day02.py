import sys
import ctypes


# normally data cast in python
def data_cast_python():
    # char to num
    char_to_num = ord('A')
    # num to char
    num_to_char = chr(64)
    # str to bytes
    str_to_bytes = str("asdsd").encode()
    # bytes to str
    bytes_to_str = str_to_bytes.decode()
    print(char_to_num, num_to_char, str_to_bytes, bytes_to_str)
    # 当bytes中含有无法解码的字节，则decode会报错
    # b'\xe4\xb8\xad\xff'.decode('utf-8')
    # 如果在bytes中想忽略无效字节则可以通过下方这个语句
    b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')


# python中比较常见的几个计算数据类型和内存大小的接口
def str_or_bytes_len():
    # 获取str字符串的长度是多少
    str_len = len('abcd')
    # 获取某个字符串字节数，可以先将这个数据直接转化为bytes，然后通过len来计算他的字节数
    data_bytes_count = len(str(4).encode())
    data_bytes_count_1 = len(str(456).encode())
    print(str_len, data_bytes_count_1, data_bytes_count)
    # 这里做个知识扩展，如果想知道一个数据的字节数可以采用下面的系统函数，由于每个操作系统上
    # 数据的排列对于32位和64位会有区别，同一个数据可能在不同位数的系统上字节数也会不同
    int_data_bytes_count = sys.getsizeof(4)
    char_data_bytes_count = sys.getsizeof('A')
    print(int_data_bytes_count, char_data_bytes_count)
    # 28 42  但是经过实践，发现这里居然输出了28 42 我电脑是64位的 不是应该是32 8吗
    # 最后经过网上查阅资料，原来不同版本的python版本会将数据类型进行封装，拿到的值实际不是这个类型的数据
    # 在系统中的实际大小，而是python该版本所封装的数据类在内存中的实际大小，我装的是python 3.12
    #
    # 但是在 Python 中，整数（int）的占用字节数并不是固定的，而是会根据整数的值和计算机架构而变化。
    # 在 Python 2 中，整数默认占用的字节数为32位（4字节），但可以通过编译器选项来改变这个值。
    # 而在 Python 3 中，整数占用的字节数根据需要动态分配，最大值取决于系统内存的限制。
    # 最后查阅资料，发现还有这个能够获取类型实际字节数的接口
    real_int_type_data_bytes_count = ctypes.sizeof(ctypes.c_int)
    real_char_type_data_bytes_count = ctypes.sizeof(ctypes.c_char)
    real_bool_type_data_bytes_count = ctypes.sizeof(ctypes.c_bool)
    real_double_type_data_bytes_count = ctypes.sizeof(ctypes.c_double)
    real_float_type_data_bytes_count = ctypes.sizeof(ctypes.c_float)
    real_long_type_data_bytes_count = ctypes.sizeof(ctypes.c_long)
    real_long_long_type_data_bytes_count = ctypes.sizeof(ctypes.c_longlong)
    real_long_double_type_data_bytes_count = ctypes.sizeof(ctypes.c_longdouble)
    # 4 1 1 8 4 4 8 8
    print(real_int_type_data_bytes_count,
          real_char_type_data_bytes_count,
          real_bool_type_data_bytes_count,
          real_double_type_data_bytes_count,
          real_float_type_data_bytes_count,
          real_long_type_data_bytes_count,
          real_long_long_type_data_bytes_count,
          real_long_double_type_data_bytes_count)


# python中如果想输入一些格式站位符，怎么使用，类似于先站位，后面跟上对应参数，这个在一般开发中用的比较多，
# 比如我的名字叫xxx，我今年xx岁，是一名x性，这个时候xxx部分可能是字符串也可能是整数，所以需要先占位置，然后我们拿到真实数据之后
# 才替换上去，见下面的例子
def format_python_str():
    # 占位符	替换内容
    # %d	整数
    # %f	浮点数
    # %s	字符串
    # %x	十六进制整数
    # 格式字符串中间采用%连接参数，如果字符串中有字符%，那么就通过%%来进行转义表示实际的字符%
    # 如'growth rate: %d %%' % 7最终打印结果为growth rate: 7 %
    format_str = '我叫 %s，我今年%d岁，是一名%s性，我知道圆周率小数点后三位%.3f，并且我知道16用16进制表示为%x'
    real_str = format_str % ('sugar', 24, '女', 3.1415926, 16)
    print(real_str)
    # 另外一种格式化字符串的方式为format()方法，其实跟上面的用法一样，只是封装了个接口
    # 但是这样的方法更加麻烦一点，你需要指明当前这个占位符的顺序，如果必要还需要通过:加上对应的数据类型
    # 占位符	替换内容
    # d	整数
    # f	浮点数   想表示省略小数点后几位用.数目f来表示，比如.3f表示小数点后三位
    # s	字符串
    # x	十六进制整数
    format_str_with_method = '我叫 {0:s}，我今年{1:d}岁，是一名{2:s}性，我知道圆周率小数点后三位{3:.3f}，并且我知道16用16进制表示为{4:x}'
    real_method_str = format_str_with_method.format('sugar', 24, '女', 3.1415926, 16)
    print(real_method_str)

    # 还有一种格式化字符串的方式 f-string
    # 该格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的xxx变量替换
    str_name = 'sugar'
    int_name = 24
    str_sex = '女'
    float_pai = 3.142
    hex_str = 10
    print(f'我叫 {str_name}，我今年{int_name}岁，是一名{str_sex}性，我知道圆周率小数点后三位{float_pai}，并且我知道16用16进制表示为{hex_str}')

if __name__ == "__main__":
    data_cast_python()
    str_or_bytes_len()
    format_python_str()
