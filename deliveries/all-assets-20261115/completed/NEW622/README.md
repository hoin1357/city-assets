# NEW622 · Complete portable marine pumpout cart / 완성형 이동식 선박 오수 배출 카트

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

Nine final local model files: NEW622_LOD0/1/2 in .blend, .fbx and .glb. Each contains all 38 parts of the complete stationary cart, without text or logos. The source is Edson 28202, not a generic hand truck. LOD0 has 3,544 triangles, LOD1 2,424 and LOD2 1,864. LOD0 preserves approved gray v002 native vertex/index arrays exactly. Lower LODs analytically retain fewer angular samples on circular components and the short hose; the source native is unchanged. No additional geometric repair was made after the one approved lever/grip seam revision.
Meters, Z up in Blender; whole-cart X width .7747, Y depth .8128, Z height 1.2192 m. Tire diameter .3048 m. Those dimensions are manufacturer facts. Other geometry is estimated from visible photographs/drawing. The nominal four-inch access port does not specify external cap diameter. Tank dimensions/rounding, pump and fittings, hose route/radius, rail bends and OD, fasteners, axle/rims and resting-foot geometry are visual estimates. Pump mounting panel is unchanged from approved gray: .23 × .24 × .07 m and tank-colored; its 70 mm thickness is an estimated simplification. Tank, pump, tires and couplings are sealed exterior surrogate solids, not internal machinery/fluid-domain replicas. Tire tread, hose reinforcement, welds, threaded couplings and lower elbow detail are simplified.
Five portable opaque/nonemissive Principled materials: aluminum, pale HDPE tank and mounting plate, dark rubber/pump, yellow connecting hose, red lever grip/valve detail. IOR 1.5, alpha 1, no transmission, no external images or custom-normal masking. Each actual triangle owns one strictly padded distinct UV grid cell; these are collision-free utility UVs, not a hand-painted shared atlas. Geometric flat normals are intentional to keep the requested strict angular agreement.
FBX exported with Y forward/Z up; GLB uses its normal Y-up coordinate convention. Verification reopens all nine actual files with default import settings, compares world-position, cyclic triangle correspondence, UVs, actual normals and material values, and reads raw GLB NORMAL values independently. No corrective import settings or model edits occur during inspections. Native Blender is the reference source for meters and object layout. Unity runtime, collision setup, rigging, pumping, fluid behavior, load stability, watertight plumbing, sanitation/safety or equipment certification are not tested or claimed.
## Visual evidence and limits
72 actual-file inspection images: eight views for each of the nine frozen models, including 256/512px full views, underside and focused pump/top fitting views. Six additional 256/512px contextual source-color renders place the cart on a neutral dock paving slab only in the transient render scene; that ground is not saved in an exported asset. Full-view crop margins and pixel saturation are recorded, while detail views intentionally crop the rest of the cart. Exact 128px isolated noun recognition is not claimed.
Prior-name/source screening found distinct waste-oil collection, drum-pump and hand-truck neighbors but no exact complete pumpout-cart match within the searched scope. Prior meshes were not inspected; bounded novelty confidence is medium, not a universal uniqueness proof.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
