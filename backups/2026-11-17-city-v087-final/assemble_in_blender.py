# Run after opening restored v085 native. Never saves or replaces open scene.
import pathlib,runpy,sys,bpy
root=pathlib.Path(__file__).resolve().parent
sys.modules.pop('qa_helpers_v001',None)
runpy.run_path(str(root/'stage_v086/append_bench_placement.py'),run_name='__main__')
sys.modules.pop('qa_helpers_v001',None)
runpy.run_path(str(root/'stage_v087/append_planter_placement.py'),run_name='__main__')
assert sum(o.type=='MESH' for o in bpy.context.scene.objects)==2278
print('ASSEMBLY PASS: 2278 meshes; not saved. Save As to a new path manually if wanted.')
