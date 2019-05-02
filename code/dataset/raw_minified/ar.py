B='ar'
import yaku.utils
def A(ctx):A=ctx;C=A.env;A.env['STLINK']=[B];A.env['STLINK_TGT_F']=[];A.env['STLINK_SRC_F']=[];A.env['STLINKFLAGS']=['rcs'];A.env['STATICLIB_FMT']='lib%s.a'
def C(ctx):
	if yaku.utils.find_program(B)is None:return False
	else:return True