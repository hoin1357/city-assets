# NEW624 · Complete man-overboard marker assembly / 완성형 해상 추락자 위치표시 장치

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

9개의 fresh geometry 각각에 exact 전쌍 검사를 실행했다. 합계11,139,798 triangle pairs 전부 계수, 공유변·공유정점 self쌍도 검사했다. degenerate/self/finite-contact 결함0. 각 파일8개 실제 반대normal 유한 면접촉 support, 전체 선분 rational interval union, 연결9/9. 각 파일72 ordered component pair strict-containment 제외. 기존 검증 predicate를 재사용한 독립 실행이며 새 predicate 발명이라고 주장하지 않는다.
72 actual-file PNG와6 context PNG를 합성 contact sheet에 의존하지 않고 각각 직접 열었다. 256/512 color hero의 분리쌍등·높은 목·넓은 원통 몸통·하부 축·느슨한 줄 식별을 확인했다. 낮은 LOD 각진 외곽 및 줄 단면 단순화는 허용 범위다. 정측면의 두 등 겹침은 자연스러운 투영이다. lamp/cord detail은 해당 범위 밖 몸통 crop이 의도된 뷰다. 노출 과다로 형상 소실, 투명도 masking, 유실 부품은 발견하지 않았다. 원사진의 인쇄·일부 색띠·매듭 세부는 재현하지 않은 게임형 단순화이다.
독립 projection72개 모두 양의 depth, 최소16.38999px margin이다. 재사용 checker의 엄격한 metadata 일치 guard0.001px는 최대0.00136533px 차이로 false를 기록했다. 해당 원 결과를 보존하고 검사 기록에 float 회전행렬 계산 차이와 실제 clipping 없음 판정을 별도 기록했다. 모델 수정이나 검사 결과 은폐는 하지 않았다.
## 제한 및 상태
외부 고정 정적 배치 제약을 유지한다. generic plinth context는 실제 자립/장착/안정성 근거가 아니고 제품9개에는 포함되지 않는다. 균일밀도 ground COM proxy도 실제 무게·부력·방수·안전 인증 근거가 아니다. 공칭H375/Ø183의 브래킷 포함 여부, 후면·상단 은색부 깊이 등은 미확인/보수적 추정이다. 전역 geometry 유일성을 주장하지 않는다. 내부·화공품·점화·제조·운용 절차 구현 없음. Unity runtime 미검증. 단일 gray 수정 소진 이후 제품 수정 없이 검사만 수행했고 upload/index/delete/GitHub 작업 없음.
**판정: FAIL. 단일 제한 수정 후 재검토 권고. 승인/완료/업로드 아님.**
- rear: 뒤쪽 회전체 연속성에 큰 임의 브래킷을 추가하지 않았다. 출처에 안 보이는 면은 추정이다.
- lamps detail: 등 받침과 돔이 각각 읽힌다. 실제 사진보다 각진 로우폴리 단순화는 허용 가능하다.
- cord detail: 느슨한 한 줄은 외관 단순화 범위지만 캡 접속과 비틀림 결함은 불허한다.
- color 256/512: 주황 본체/밝은 등/검은 칼라/상단 은색을 통해 출처의 완성형 표지 장치로 읽히며 라벨에 의존하지 않는다. 정확한 명칭의 128px 판정이나 물리적 기능 보장은 하지 않는다.
원사진의 하부 은색 띠/전면 매듭과 상단 둥근 체결점이 단순화되어 있다. 현재 완성품 정체성을 무너뜨리는 추가 수정 요구로 보지는 않는다. 상단 금속부 깊이/뒤면은 미확인 보수적 추정으로 남겨야 한다.
봉인 SHA/크기를 전부 대조하고 Blender에서 원본을 읽기 전용으로 열어 새 좌표를 추출했다. 제작자 geometry와 새 추출값이 일치한다. 기존 검토 predicate와 finite-contact 알고리즘을 명시적으로 재사용했으며, 별도의 새 알고리즘을 발명했다고 주장하지 않는다.
9개 mesh / 2,336 triangle. 전체 2,727,280쌍 = inclusive AABB 제외 2,704,216 + exact integer/Fraction 23,064. 공유 정점/변을 가진 self쌍도 예외 없이 검사했다. degenerate 0, 줄 self 결함 176.
모든 mesh의 2-face manifold/반대 edge winding/원판 vertex-link/양의 체적은 통과하나 자기교차 통과를 뜻하지 않는다. 72 ordered pair 모두 exact 외부 증인이 있어 전체 포함 배제 근거가 있으나 교차 실패 상태에서 완성된 solid containment 통과라고 결론내리지 않는다. 실제 native corner normal 대 기하 normal 최대 0.0049289624°로 0.01° 미만. flat, custom normals 없음, modifiers 없음.
줄과 연결 패드의 접속/프레임을 하나의 제한 수정 범위로 묶는다. 연속 프레임 전달로 단면 부호반전/strip 비틀림을 없애고, 필요한 경우 최소한으로 줄 경로를 단순화하되 느슨한 외부 고리를 유지한다. 패드 뒷면은 본체의 이미 저장된 facet 꼭짓점 좌표를 그대로 공유하고, 패드 앞면과 줄 첫 cap은 같은 축정렬 평면 좌표를 사용한다. 근접/epsilon/표면 겹치기로 접합을 대신하지 않는다. 본체·목·쌍등·상하 축, 상단 추정 금속부를 새 구조로 확장하지 않는다. 단순화 허용은 교차/유한 접촉/지지 검사 면제가 아니다.
## 제한
일반 부표/비콘과 전체 조합은 다르지만 기존 geometry 미확인으로 novelty 확신은 중간이다. 전역 유일성 주장 없음. 비작동 외형 게임 소품만 검토했으며 내부·점화·화공품·제조/운용 절차·안전 인증을 다루지 않았다. 제품 편집, upload, index 변경, 삭제, export는 수행하지 않았다.
9 mesh / 2,336 triangles. 2,727,280쌍 전체 = inclusive AABB 제외 2,704,803 + exact integer/Fraction 검사 22,477. 공유변/공유정점 self쌍도 생략하지 않았다. degenerate0, self0.
기존 검토 알고리즘을 재사용한 독립 실행이며 별도 신규 predicate 구현이라고 주장하지 않는다.
수정본 gray hero256/512, front, rear, side, top, underside, lamps detail, cord detail 및 color256/512 총11뷰를 직접 열어 확인했다. 초기 직접 확인한 Comet9181600 원사진에 비추어 넓은 원통 몸통·높은 목·분리쌍등·하부 축·느슨한 줄 조합이 유지된다. 패드 접속은 조금 넓어졌지만 국소적이며 별도 큰 브래킷이나 새 기능을 발명하지 않았다. 줄은 단순화된 외부 고리로 일관되며 초기의 기술 결함 제거와 무관한 source 변경은 없다. color256/512에서 완성형 해상 위치표지 외관으로 읽히나 정확한128px 명칭식별 또는 실제 기능을 주장하지 않는다. 상단 은색부 뒤면/깊이는 여전히 보수적 추정이다.
## 지면과 제한
실제 최저z coplanar ground faces의 볼록껍질과 균일밀도 proxy COM을 다시 검사 기록). proxy 내부여도 실제 무게/밀도/장착/안정성 근거가 아니므로 external static placement constraint를 유지한다. 부력/방수/해상 안전/인증 보증 없음. 비작동 외형 게임 소품으로만 취급한다. 기존 부표/비콘 geometry 미확인으로 novelty 중간, 전역유일성 주장 없음. 초기 상세 출처/11뷰 기준은 상위 INDEPENDENT_GRAY_REVIEW.md 참고. 제품 편집·upload·index·삭제·export 없음.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
