# NEW640 · Complete wooden-handle fish scaler / 완성형 목제 손잡이 생선 비늘 제거기

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

모든 실제 부품의 연결 성분1,닫힌 edge manifold,일관 winding,manifold vertex link,양의 signed volume,퇴화면0이 확인되었다. 포맷이 normal/UV seam을 위해 분리한 정점을 정확히 같은 실제 좌표로 묶은 topology 검사를 명시한다. smoothing을 이용해 결함을 감추지 않았으며 native는 flat·custom normal 없음·modifier 없음이다. imported effective corner normal 최대 오차0.001145919도 미만으로0.01도 기준을 통과한다. raw GLB 별도 검사는 다음 단락에 있다.
9파일 좌표·삼각형 cyclic 대응 누락0,최대 위치 오차0,치수 동일이다. UV는 모든 실제 삼각형이 전역 고유 grid cell 내부에 들어가고 양의 면적·여백을 가진다. 따라서 모든 UV 삼각형쌍은 셀 경계로 분리된다. 최소 셀 가장자리 여백0.004285670 이상,최대 왕복 UV 오차2.98023224e-08이다. 이것은 atlas 효율 최적화나 동일 texel density 주장이 아니라 실제 정량 비중첩 증명이다. 재질은 opaque3종이며 texture 의존성 없이 기본 PBR 값의 왕복 fidelity를 통과했다.
회색 승인 때와 마찬가지로 사선 톱니가 겹치면서 슬롯이 여러 짧은 구멍처럼 보일 수 있으나 top/underside에서3개의 긴 구멍이 연결된다. 정상 투영 중첩을 숨기지 않는다. 전문 명칭을128 회색에서 맞히는 것을 요구하지 않는다. 작은256 문맥에서는 손 공구의 전체 구조와 재질 대비를 평가하며 전문명 확정 식별을 보장하지 않는다. 자연스러운 flat facets와 약한 렌더 노이즈가 남는다.
NEW549 U요크 가시 롤러,NEW575 호퍼/회전드럼/크랭크,NEW304 별도손잡이 없는 한줄빗과 완성품 구조가 다르다. ROOT153 및 ID 없는 슬롯 뒤집개/사각강판/헤어브러시는 원형 미확보이며 역사 원문1,149개 미복구 한계를 유지한다. 전체 역사 무중복은 보증하지 않는다.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
