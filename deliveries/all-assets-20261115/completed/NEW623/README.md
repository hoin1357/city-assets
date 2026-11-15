# NEW623 · Complete portable dive control panel / 완성형 휴대식 잠수 제어 패널

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

전면이 노출된 운용 패널의 정적 게임 소품입니다. 제조사 사진에서 보이는 본체 외관을 참고했습니다. 전체 운반 키트, 별도 뚜껑, 후면/내부의 충실한 복원, 실제 작동·압력·유량·잠수 안전을 주장하지 않습니다. Unity에서 실행하거나 인증하지 않았습니다. 호스·공기통·기능 텍스트·회로도·로고를 추가하지 않았습니다.
.blend는 Z-up/meter 단위, 형상변환 적용 상태입니다. FBX와 GLB는 표준 exporter/importer 좌표변환을 사용하며 9파일 fresh default imports의 world position·UV·normal·PBR fidelity를 별도 검사합니다. 임의의 corrective import 설정을 사용하지 않았습니다. GLB는 외부 texture/image 없이 포함된 buffers/materials만 사용합니다. 제공 UV는 전체 부품을 아우르는 서로 분리된 패딩 삼각형 셀입니다. 재질은 균일색으로, 실사 텍스처나 기능 눈금은 없습니다. 충돌체/애니메이션/실제 밸브 조작이나 압력 가시화는 제공하지 않습니다.
## 치수와 원본 제한
제조사 명시 L527 × W800 × D292 mm를 그대로 재현한 정밀 모델이 아닙니다. 정면 사진 비례를 우선하였고, 292 mm가 운반덮개를 포함하는지 불명입니다. 현재 모델 케이스 폭800 mm, 손잡이 포함 전체 폭852 mm, 탭 포함 높이527 mm, 추정 케이스 깊이174 mm, 계기 포함 전체 깊이227 mm입니다. 손잡이가 명시 W800에 포함되는지 또한 미검증입니다. 과거 계획상의 220 mm는 실제 결과 치수가 아니므로 사용하지 않습니다. 후면은 단순한 닫힌 케이스로 추정했고 내부 밸브·탈착 뚜껑을 발명하지 않았습니다.
## 외부지지 정적 배치 제한
제품은 외부지지를 받는 정적 배경 소품으로 배치하세요. 제공 맥락뷰는 제품 geometry를 바꾸지 않고 뒤판·별도 바닥받침·후면 하부턱을 두어 이 제한을 보여줍니다. 이 세 구조물은 촬영 맥락일 뿐 9개의 제품 파일에 포함되지 않습니다. 동적 rigid-body, 자립/낙하/하중 안전, 잠수 운영훈련 용도로 사용할 수 없습니다. 메쉬 좌표의 최저점은 원본 float 정밀도로 약 -5 nm이며 LOD0 원본배열 보존을 위해 보정하지 않았습니다. 실제 프로젝트 원점/배치는 사용 환경에서 다뤄야 합니다.
판정: **PASS_WITH_LIMITS 권고. 제품 수정이나 재촬영을 요구하지 않는다.** 정적 시각 소품의 제한부 합격이며, 등록/업로드/백업/Unity 실행·물리·가스 안전 승인이 아니다.
제조사 실제 JPG, 연구 REFERENCE_BRIEF_v001.md, 초기 gray 독립검토를 직접 읽었다. 6계기(큰2/작은4), 8노브, 하부4/상부1 레버, 하부10포트, 우측 운반손잡이와 케이스 구성이 사진에 일관된다. 실제 배관인 양 튜브를 발명하지 않았으며 계기 눈금/회로 인쇄/브랜드를 없앤 단순 시각 표현이다. 후면/깊이는 추정이다. 사진에 없는 뚜껑·호스·공기통을 추가하지 않았다.
LOD0는 승인 gray 77부품의 vertex/triangle 배열 전부 정확 보존. LOD1/2 각각 77부품 유지, 24부품은 원본 배열 그대로이며 나머지는 회전형 각분할 감소다. 8,924 /4,892 /3,492 triangles. 낮은 LOD에서도 6계기/10포트/노브/레버/손잡이와 gauge·port recess가 남는다. LOD2 다이얼의 각진 실루엣은 의도된 단순화이며 구멍을 메운 평면 표시로 대체하지 않았다.
- 별도 raw GLB reader에서 77부품 전 oriented world triangles를 native와 일대일 cyclic 매칭. raw UV/PBR 오차0, raw-native normal 방향 최대0.004305095°. raw NORMAL 대 실제 삼각형 면 normal 최대0.004734803°로 0.01° 미만. importer의 정규화로 raw 편차를 숨기지 않았다.
새 native 추출에 이전에 검토된 exact predicate/finite-support 스크립트를 재사용했다. 독립적인 새 수학 구현이라고 과장하지 않는다. 3LOD에서 39,814,426 /11,963,386 /6,095,286 unordered triangle pairs를 모두 계수(합계57,873,098). inclusive AABB 제외와 exact 후보 합계가 정확히 전체와 같다. 공유정점/변 self 후보도 건너뛰지 않았다.
self defect0, degenerate0, finite-contact defect0. opposed finite polygon의 rational interval union으로 전체 접촉선분을 덮고 local separation을 검사했다. 무한평면 허용 또는 object-pair 일괄예외 없음. 각 LOD82 유한 지지 plane, ordered containment 5,852쌍 모두 strict containment 배제, cavity/wall6 controls PASS. positive-area assembly graph77/77 연결. FBX/GLB 새 world geometry가 같은 LOD native와 정확히 동일함을 확인했으므로 이 exact 결과가 모든9 파일에 적용된다. 별도9번 exact 실행을 주장하지 않는다.
72 actual-file PNG(9파일×8뷰)와 외부지지 color context6장 모두 원본을 **개별 직접 열어** 검토했다. 검사 기록에 각각 관찰·hash를 기록했다. 형식별 전면/후면/측면/상부/하부/상세에서 재질 누락, 불투명도 오류, feature 소실 또는 whole-asset 프레임클립 없음. detail은 왼쪽3계기/하부10포트를 선언한 범위이며 그 밖의 주변 부분 crop은 제품 전체뷰 결함으로 세지 않는다.
72개 camera projection을 새 world vertices에서 별도 계산: 모든 선언 대상 양의 depth와 margin, 최소23.470967px. 제작자 기록과 margin 차이 최대0.000412px. PNG78장 hash 유지, 완전 흰 pixel 비율 최대0. 전체 silhouette와 바늘·포트 cavity가 확인된다.
**시각 한계는 남는다.** Cycles48 samples/denoise OFF의 grain이 밝은 panel과 측면에 보이며 은색 lever와 panel 대비가 낮다. 256px에서는 작은 레버/바늘 식별에 제한이 있다. 다만512 상세에서 해당 돌출·오목 형상과 10포트가 보이므로 현재 정적 low-poly 범위를 실패시키는 소실은 아니다. noise-free·실사품질·128px 전문명칭 식별을 주장하지 않는다. 재촬영이나 denoise를 요구하지 않았다.
## 치수·배치 제한
본체W800, 손잡이포함W852, 높이527, 추정caseD174, 전체D227mm. 제조사L527×W800×D292의 정확 재현이 아니며 W800의 손잡이 포함 여부와 D292의 뚜껑 포함 여부는 미확인이다. 220mm는 실제값이 아니다.
최저점은 float precision 약-5nm. fresh import 일반 검사기의 z==0 기반 support 면적0/hull빈값은 실제 바닥 접촉 부재가 아니라 원점 정밀도 진단의 한계다. 실제 최저z에서 별도 support_ground 재실행한 결과를 우선한다. LOD0 균일밀도 COM은 하부3탭의 뒤 경계에서 약11.541175mm 밖이며 자립proxy는 실패한다. 실제 내부 질량·밀도·안정성을 입증하지도 부정하지도 않는다. proxy 통과를 위해 탭을 임의 받침으로 바꾸지 않았다.
외부지지 정적배치만 권고한다. context는 별도 바닥/후면턱/뒤판으로 이 조건을 보여 주며 이 받침은 제품9파일에 포함되지 않는다. assembly 연결은 실제 체결강도나 rigid-body 안정성의 증거가 아니다. 실제 압력·유량·잠수안전·운용훈련·Unity 실행·동역학 미검증. 기존 regulator/manifold geometry를 직접 대조하지 않아 novelty는 중간이고 전역 geometry 유일성 미보증.
판정: **PASS_WITH_LIMITS 권고, 형상 수정 불필요**. 이는 정적 시각 에셋의 초기 gray 검토이며 최종 산출물·export·Unity·압력 장비·물리 검증 승인이 아니다.
검사 디렉터리의 producer_ 접두사 파일은 원본 결과 복사가 아니라 새 native 추출에 대해 재실행한 결과다. 이전에 검토된 exact predicate 및 검사 스크립트 재사용을 명시한다. 별도 구현의 수학적 증명으로 과장하지 않는다.
- 전 39,814,426 unordered triangle pairs 계산. inclusive AABB 제외 39,715,082; exact 후보 99,344. 공유정점/공유변 self 후보도 건너뛰지 않았다. self defect 0, degenerate 0.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
