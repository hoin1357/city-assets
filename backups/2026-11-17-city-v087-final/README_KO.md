# 침수 도시 최종 바이너리 조립 백업 v087
이 패킷은 v085 도시 최종 native와 v086 v002 벤치 및 v087 v001 화분 배치의 사용 가능한 최종 바이너리 백업입니다. 과거 모든 작업 이력·실패본·제작 소스 재생성을 포함하거나 보장하지 않습니다. 독립 자산 패키지와는 다릅니다.

1. 모든 파일의 MANIFEST.json SHA256/bytes를 검증합니다. Python으로 `python restore_base.py`를 실행하면 15개 파트를 원래 바이트 순서로 합칩니다. 기존 목적지는 덮어쓰지 않습니다. 약 122MB의 별도 복원 공간이 필요합니다. 복원 도중 실패한 파일은 최종 검증 통과 전 사용하지 마세요.
2. 복원된 `DISTRICT_PUBLIC_FOUNTAIN_v085.blend`를 Blender에서 엽니다. 2,127메시이며 사용하는 파일 이미지 516개가 내장되어 있습니다. 외부 연결 라이브러리/텍스처가 필요하지 않습니다.
3. 자동 조립: `blender -b DISTRICT_PUBLIC_FOUNTAIN_v085.blend --python assemble_in_blender.py`는 검증 후 2,278메시를 메모리에서 조립하고 저장하지 않습니다. GUI에서는 복원 파일을 연 뒤 Blender Text Editor에서 assemble_in_blender.py를 실행하고 필요하면 다른 이름으로 저장하세요.
4. 수동 순서: v086 addon의 B01401R_BENCH_PLACEMENT_V086 컬렉션을 Append한 뒤 v087 addon의 B05001R_PLANTER_PLACEMENT_V087 컬렉션을 Append합니다. 정밀한 visibility 복원과 원본 변경/중복 검사까지 필요하면 자동 loader를 사용하세요. addon의 기본 Scene이 비어 있는 것은 정상입니다.

조립 순서는 v085 → v086 v002 → v087 v001입니다. 원래 비활성 7개를 포함한 기존 메시·표시상태를 유지합니다. 충돌체는 형상 데이터이며 Unity Collider 자동 연결이 아닙니다. 기존 도시의 placeholder/후보 및 검증 제한도 유지됩니다. Unity/PhysX/실제 수영 조작: NOT_RUN. 원본에 덮어쓰지 마세요.
