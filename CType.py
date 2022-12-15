import ctypes
import platform
import os
from pkg import MathematicalTypes, VarTypes
from operator import methodcaller
from pkg import VarType2CType, MathematicalTypes2FuncOp, VarTypeCalPriority, VarPriority2Type, get_return_type

cfunction = None
if platform.system().lower() == 'windows':
  if not os.path.exists("c_cal.dll"):
    raise FileNotFoundError()
  else:
    cfunction = ctypes.CDLL("./c_cal.dll")
elif platform.system().lower() == 'linux':
  if not os.path.exists("c_cal.so"):
    raise FileNotFoundError()
  else:
    cfunction = ctypes.CDLL("./c_cal.so")
else:
  raise Exception("Unknow platform")
print("c_cal dll/so load")


class CVal:
  # 从Var_t转换为CType,这里没做范围检查，请确保Var_t输入合法
  def __init__(self, val_obj=None):
    # 私有属性外部莫用
    if val_obj != None:
      # _c_value就是一个普通python值，但是在运算中会严格被_type_name限制
      self._c_value = val_obj.val
      self._type_name = val_obj.type_name

  # 根据type返回一个正确的Var_t的val值
  # 并不确定这一步走c是否是必须的，只是谨慎起见罢了
  def ToValValue(self, val_type: VarTypes):
    if val_type == VarTypes.BOOL or val_type == VarTypes.VOID:
      raise Exception("Why we use such type!")

    actype = getattr(ctypes, VarType2CType[self._type_name])
    a = actype(self._c_value)
    outer_ctype = getattr(ctypes, VarType2CType[val_type])

    cal_func = getattr(cfunction, f"cast_{self._type_name}_T_{val_type}")
    cal_func.argtypes = [actype]
    cal_func.restype = outer_ctype
    val = cal_func(a)
    # print(bin(val))
    return val

  # 探测并处理零值（自增1）
  def DetectZero(self):
    return self._c_value == 0

  def NewAddOneCVal(self):
    result = CVal()
    result._type_name = self._type_name
    result._c_value = self._c_value+1
    return result

  # 与另一个CVal计算并更新一个新的CVal
  def Cal(self, cval_obj, op: MathematicalTypes):
    actype = getattr(ctypes, VarType2CType[self._type_name])
    bctype = getattr(ctypes, VarType2CType[cval_obj._type_name])
    a = actype(self._c_value)
    b = bctype(cval_obj._c_value)

    cal_func = getattr(
        cfunction, f"{self._type_name}_W_{cval_obj._type_name}_{MathematicalTypes2FuncOp[op]}")
    cal_func.argtypes = [actype, bctype]

    # 已经能获得计算完毕后自己的类型了
    new_type_name = get_return_type(self._type_name, cval_obj._type_name)
    cal_func.restype = getattr(ctypes, VarType2CType[new_type_name])
    new_c_value = cal_func(a, b)

    result = CVal()
    result._type_name = new_type_name
    result._c_value = new_c_value
    return result
    # print(self._c_value)


if __name__ == "__main__":
  a = CVal()
  a._type_name = VarTypes.ULONG
  a._c_value = 511111111111111111111111111111111111111111111

  b = CVal()
  b._type_name = VarTypes.SHORT
  b._c_value = 0

  a.Cal(b, MathematicalTypes.ADD)

  print(a._c_value)
  print(a._type_name)
  print(a.ToValValue(VarTypes.UCHAR))
