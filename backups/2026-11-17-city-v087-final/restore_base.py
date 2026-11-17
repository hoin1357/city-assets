import pathlib,json,hashlib,sys
root=pathlib.Path(__file__).resolve().parent
m=json.loads((root/'MANIFEST.json').read_text())
out=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/m['base']['filename']
if out.exists(): raise RuntimeError('Destination exists; refusing overwrite')
h=hashlib.sha256()
with out.open('xb') as dst:
 for name in m['base']['parts']:
  b=(root/name).read_bytes(); expected=next(x for x in m['files'] if x['path']==name)
  if len(b)!=expected['bytes'] or hashlib.sha256(b).hexdigest()!=expected['sha256']:raise RuntimeError('Part mismatch: '+name)
  dst.write(b);h.update(b)
if out.stat().st_size!=m['base']['bytes'] or h.hexdigest()!=m['base']['sha256']:raise RuntimeError('Final native mismatch')
print('Restored byte-identical native:',out)
