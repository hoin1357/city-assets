# Actual planter geometry add-on. Open verified v085 and append verified v086 bench first; never discards or saves a scene.
import bpy,json,hashlib,sys
from pathlib import Path
O=Path(__file__).resolve().parent
sys.path.insert(0,str(O))
from qa_helpers_v001 import fingerprint
q=json.load(open(O/'QA_v087.json'))
C='B05001R_PLANTER_PLACEMENT_V087'
if not bpy.data.filepath or hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest()!=q['source_sha256']:raise RuntimeError('Wrong base SHA: open verified v085. Unsaved work is not discarded.')
if bpy.data.collections.get(C):raise RuntimeError('Planter placement already present; duplicate refused.')
bpy.context.view_layer.update()
meshes={o.name:o for o in bpy.context.scene.objects if o.type=='MESH'}
expected=q['base_mesh_fingerprints']
if set(meshes)!=set(expected) or any(fingerprint(o)!=expected[n] for n,o in meshes.items()):raise RuntimeError('Unsaved base mesh changes: append refused.')
states=json.load(open(O/'ADDON_OBJECT_STATE.json'))
if any(bpy.data.objects.get(n) for n in states) or any(bpy.data.materials.get(n) for n in q['addon_material_names']):raise RuntimeError('Planter object/material namespace occupied; append refused.')
p=O/q['addon_file']
if hashlib.sha256(p.read_bytes()).hexdigest()!=q['addon_sha256']:raise RuntimeError('Add-on SHA mismatch.')
with bpy.data.libraries.load(str(p),link=False) as (a,b):
 if C not in a.collections:raise RuntimeError('Expected collection missing.')
 b.collections=[C]
bpy.context.scene.collection.children.link(b.collections[0])
bpy.context.view_layer.update()
for n,st in states.items():
 o=bpy.data.objects[n];o.hide_render=st['hide_render'];o.hide_viewport=st['hide_viewport'];o.hide_set(st['hide_set'])
bpy.context.view_layer.update()
assert all(fingerprint(bpy.data.objects[n])==f for n,f in q['asset_mesh_fingerprints'].items()),'Appended asset fingerprint mismatch'
assert all(fingerprint(bpy.data.objects[n])==f for n,f in expected.items()),'Base changed'
print('PLANTER_ADDON_PASS: actual geometry appended; original file not saved.')
