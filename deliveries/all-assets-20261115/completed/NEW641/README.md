# NEW641 · Complete battery-mounted angle grinder / 완성형 배터리 장착 앵글 그라인더

**상태 / Status:** 승인된 선택본 / accepted selected asset. 3 LOD × BLEND·GLB·FBX = 9 models.

하나의 에셋이며 LOD나 형식은 별도 종류로 세지 않습니다. 텍스처가 제공된 경우 함께 배치하세요.
One asset, not nine designs. Keep supplied textures with the model files.

## 사용 범위 / Scope

게임용 시각 에셋입니다. 제작 당시 파일 검사와 이번 복구의 바이트 검증은 Unity 실행, 물리·충돌·성능·동작 인증을 뜻하지 않습니다. 역사 자료 전체와의 중복 부재도 보장하지 않습니다.
Visual game asset. Authoring-time checks and recovery byte verification are not Unity runtime, physics, collision, performance or operational certification. Global uniqueness is not guaranteed.

## 개별 한계 / Asset-specific limitations

저장 native는 flat이고 커스텀 법선·모디파이어가 없다. 실제 면과 코너 법선 모두 <0.01도이며 최대 유효 코너 오차 0.0007723427960648359도다. 원본 GLB 버퍼의 POSITION/NORMAL/indices를 직접 읽은 최대 오차는 0.004653406483650894도다. 기존 임계값을 바꾸지 않았다. GLB 축변환 후 실제 원본 기하와 정확히 대응한다.
BLEND LOD0에는 0×0 크기의 빈 VIEWER Render Result 데이터블록이 남아 있다. 실제 장면 객체는 13개 모델 메시뿐이며 이번 점검에서는 사용되지 않는 카메라/조명 데이터도 발견되지 않았다. FBX 기본 임포터는 7재질에 Strength 0의 Normal Map 노드를 만든다. 이 사실은 검사 기록에 공개했다. 이미지 노드는 없고 해당 노드로 법선을 보정하지 않았으며 실제 임포트 법선 오차를 그대로 검사했다. GLB에 텍스처/외부 이미지/스킨/애니메이션/카메라는 없다.
각 개별 원본 PNG를 제작자 검토자가 직접 열었다. LOD0 26개와 하위 LOD 52개의 파일별 기록을 별도로 남긴다. 배터리·직각 휠·보조손잡이·가드로 완성 휴대 그라인더를 식별할 수 있다. 각진 배터리/몸통, 단순화 기어헤드, 낮은 LOD 원주 다각화는 알려진 저폴리 한계다. 미세 리브·로고·내부 장치를 포함한 정밀 제품 복제본이 아니다. 그림자/렌더 노이즈를 관통이나 구멍으로 오인하지 않았다. 128 회색 전문명칭 정답률은 게이트로 쓰지 않는다.

제작 중 작성된 제한 설명은 승인된 선택본의 사용 한계를 안내합니다. 그 설명의 과거 검사 대기 상태는 현재 승인 상태를 대체하지 않습니다. / Historical authoring notes describe limitations; their intermediate pending status does not supersede the accepted selected-file status.

## 권리 / Rights

이 문서는 새로운 라이선스를 부여하지 않습니다. 기존 저장소의 권리 안내를 따르세요.
This document grants no new license; consult the repository’s existing rights information.
