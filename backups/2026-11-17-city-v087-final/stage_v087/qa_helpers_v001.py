import hashlib,json,numpy as np
from mathutils.bvhtree import BVHTree
def fingerprint(o):
 return hashlib.sha256(json.dumps(dict(v=[list(v.co)for v in o.data.vertices],f=[list(p.vertices)for p in o.data.polygons],matrix=[list(v)for v in o.matrix_world],materials=[m.name if m else None for m in o.data.materials],visibility=[o.hide_render,o.hide_viewport,o.hide_get()],COL=o.get('is_collision_geometry')),sort_keys=True).encode()).hexdigest()


def tree(obs):
 v=[];f=[];names=[]
 for o in obs:
  n=len(v);v.extend(o.matrix_world@q.co for q in o.data.vertices)
  for p in o.data.polygons:f.append([n+i for i in p.vertices]);names.append(o.name)
 return BVHTree.FromPolygons(v,f),names



def surface_key(o):
 return hashlib.sha256(repr(sorted(tuple(sorted(tuple(round(float(c),5)for c in o.matrix_world@o.data.vertices[i].co)for i in p.vertices))for p in o.data.polygons)).encode()).hexdigest()
