print(30*'+')
import bpy as A
if not hasattr(A.context.scene,'matlib_categories'):
	class B(A.types.PropertyGroup):0
	A.utils.register_class(B);A.types.Scene.matlib_categories=A.props.CollectionProperty(type=B)
C=A.context.scene.matlib_categories
for D in C:C.remove(0)
A.ops.wm.save_mainfile(filepath='C:\\Users\\Dell\\Downloads\\blender-2.76-301115-win64\\blender-2.76.0-git.3780158-AMD64\\2.76\\scripts\\addons\\matlib_cycles\\car_paint.blend',check_existing=False,compress=True)