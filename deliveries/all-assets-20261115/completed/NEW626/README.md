# NEW626 · Complete wooden T-handle cargo hook / 완성형 목제 T손잡이 하역 갈고리

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

- 교환 파일은 flat 면과 UV에 따라 정점이 분리 저장된다. 위 정점 수는 기하 좌표를 정확히 묶은 수다. 실제 저장 정점 수는 각 수입 보고서에 별도로 기록했다.
낮은 LOD는 승인 형상의 분석적인 단면 정점 중 명시된 단면들을 선택하고, 그 사이 삼각형을 새로 구성했다. 임의 정점 collapse, Decimate, Boolean 또는 기존 삼각형을 무작정 제거한 방식이 아니다. 관통 탱과 육각 구멍의 좌표, 동일 대각선 접촉 삼각형, 유한 팁, 두 바닥 지지선 정점은 정확히 보존했다. 명시 단면 목록은 검사 기록에 있다. 모든 LOD는 별도로 전수 검사했다.
확정 명목 치수는11인치 날279.4mm와7/16인치 육각 소재11.1125mm다. 날 길이의 측정축이 공개되지 않아 승인 소스의 투영 해석을 그대로 유지했다. 손잡이160mm/명목33mm, 탱8.2mm, 팁0.9mm, 굽힘·테이퍼·전체 외곽은 실측이 아닌 사진 기반 추정이다. 11×4×1인치 표를 확정 전체 크기로 쓰지 않았다. 자세한 동일 모델 사진 근거와 제한은 부모 회색 기술 보고서와 `research/NEW626/REFERENCE_BRIEF_v001.md`에 있다.
- 좌표·UV·실제 유효 법선의 수입 충실도 오차0. 재질값도 허용치 내에서 동일하다.
GLB는 수입 검사와 별도로 파일의 실제 float32 POSITION/NORMAL/indices를 직접 읽었다. 세 LOD 모두 **직렬화된 원시 GLB 법선 최대오차0.009233780386°**다.0.01° 미만이며 보정 후 값이 아니다. 여유가 크지는 않으므로 다른 프로그램에서 재내보내기한 새 파일에 이 판정을 전파하면 안 된다. 파일 버전이 바뀌면 다시 검사해야 한다.
- LOD0: 전체87,990 = AABB 제외84,451 + exact3,539.
- LOD1: 전체49,770 = AABB 제외47,048 + exact2,722.
- LOD2: 전체27,730 = AABB 제외25,594 + exact2,136.
-9파일 총합496,470 = 제외471,279 + exact25,191. 자기교차 결함·퇴화 삼각형·접촉 결함 모두0.
자기/부품 사이의 전체 가능 쌍, broad 제외, exact 후보를 부품별로 구분한 원장은 검사 기록 및 각 검사 기록에 있다.
## 정적 배치 한계
- 각LOD의 BLEND 대비FBX/GLB48개 대응 이미지 중15개는 전체RGBA 픽셀이 정확히 같다. 나머지 차이도 최대8비트 채널1단계, 최대 평균 절대오차0.0000047684다. 모든 파일의 실루엣·재질 표현은 시각적으로 일치한다.
- LOD1/2에서 각이 더 드러나며 LOD2는 근접 표시용이 아니다.256/512에서 목제 T손잡이·긴 자루·열린 되돌림 갈고리·연속 유한 팁은 유지된다. 위쪽 edge-on 투영은 T송곳처럼 보이는 각도 제한을 그대로 남겼다.128픽셀의 정확 명사 맞히기는 검사 조건이 아니다.
Blender 4.3.2에서 9파일을 기본 설정으로 새로 열거나 수입했다. 파일에 저장하거나 모델의 정점·면·법선·수입 옵션을 보정하지 않았다. 실제 corner normal과 재질·UV·좌표를 직접 추출했고, 별도의 Python checker에서 저장된 GLB binary accessor를 struct로 직접 해독했다.
**삼각형 모양의 제한:** 손잡이 관통부 연결에는 최소각 **0.068845540°**의 좁은 삼각형이 존재한다. 승인 회색과 전 LOD/형식에 유지되며 면적·법선·폐곡면·접촉 검사는 통과했다. 이를 퇴화로 취급하거나 임의 재삼각화하지 않았다. 반대로 “길고 가는 삼각형이 하나도 없다”, “등방형 삼각분할 품질을 보장한다”고 주장하지 않는다. 별도 게임 프로젝트가 최소각/종횡비 기준을 요구한다면 추가 검토 대상이다.
- 실제 네이티브 및 기본 수입 corner normal 최대 오차: **0.006326806755°**, 모든 corner가 0.01° 미만.
**제작자 문구 보완:** FBX 기본 수입 재질에는 Blender가 Normal Map 노드를 연결한다. 직접 확인한 6개 재질 모두 Strength=0, Color=(0.5,0.5,1), 입력 링크 없음이다. 효과가 없는 중립 수입 노드이며 원본의 노멀 보정이나 검증 마스킹은 아니다. “모든 수입 노드 트리에 Normal Map 노드 자체가 전혀 없다”는 뜻으로 확대하면 안 된다. 최초 노드 종류 검사에서 나온 보수적 실패는 이 실제 입력값을 확인해 해소했고 초기 결과도 보존했다.
모든 기본 수입 삼각형을 순환 순서의 정확한 좌표 키로 native와 대응시켰다. 반올림한 키를 사용하지 않았다. 위치·면 방향은 정확히 같고 실제 corner normal의 형식 충실도 오차는 0이다. 두 불투명 비발광 재질의 주요 값도 일치한다. 외부 이미지, 사진 텍스처, 숨겨진 쉐이더 보정이 없다.
모든 실제 수입 UV 삼각형은 양의 면적이고 전체 모델에서 서로 다른 격자 셀의 내부에 양의 여백을 둔다. 동일 셀 중복 0이므로 전역 UV 겹침이 없다. **GLB UV 최대 차이는 2.9802322387695312×10^-8**로 측정했다. 허용치 10^-6보다 작지만 제작자의 “UV 오차 0” 문구 대신 이 측정값을 사용한다. 연속 나뭇결 페인팅·등밀도·왜곡 최적화를 검증한 것은 아니다.
AABB 제외는 엄격한 축 간격으로만 하고 나머지는 저장 이진좌표의 정확한 정수/Fraction 판정으로 검사했다. 공통 정점·변을 가진 자기쌍도 먼저 exact intersection을 계산한 뒤 통상 토폴로지 접촉인지 판정했다. 물체 전체 허용목록이나 중점 검사만으로 통과시킨 쌍은 없다.
- LOD0: 87,990 = AABB 제외 84,451 + exact 후보 3,539.
- LOD1: 49,770 = 제외 47,048 + exact 2,722.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
