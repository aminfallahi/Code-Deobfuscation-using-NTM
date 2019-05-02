'Create new objects of various types.  Deprecated.\n\nThis module is no longer required except for backward compatibility.\nObjects of most types can now be created by calling the type object.\n'
from types import ClassType as A,FunctionType as B,InstanceType as C,MethodType as D,ModuleType as E
try:from types import CodeType as F
except ImportError:pass