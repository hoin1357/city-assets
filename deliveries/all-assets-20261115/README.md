# 심해도시 에셋 · Submerged-city assets

## 범위 / Scope

- [완료 432세트 탐색 / Browse 432 accepted sets](CATALOG.md): 기존 공개 366 ID + 이번 신규 완료 66세트, 선택 모델 594개와 지원 PNG 40개. / 594 selected models and 40 support PNGs.
- [보류 및 이전판 / Held and historical versions](held/README.md): 미승인 고유 60 ID와 이후 승인된 NEW614·NEW615의 이전판 9모델. 보류 60종은 290모델로, 합계 299모델이며 완료 수에 더하지 않습니다. / 290 held models + 9 promoted-history models, 299 in total.
- [NEW695 미완성 / Work in progress](in_progress/NEW695/README.md): 선택 후보 9개와 이전 native 5개, 총 14모델 및 PNG 1개. 최종 검사 미완료이며 완료 수에 포함하지 않습니다. / 9 candidate outputs + 5 earlier native models, 14 models and 1 PNG; incomplete.

3 LOD와 BLEND·GLB·FBX는 한 종류의 여러 표현이며 각각 별도 에셋이 아닙니다. 432는 별도 계속 제작 원장 수이며 과거 880 등의 수와 합산할 수 없습니다.
Three LODs and three formats are representations of one asset, not separate designs. The 432-set continuation ledger must not be added to older totals such as 880.

이번 새 게시 범위는 **모델 907개와 지원 PNG 41개**입니다. 594 + 299 + 14 = 907이며 서로 다른 완성 에셋 907종이라는 뜻이 아닙니다.
The new publication contains **907 model files and 41 support PNGs**: 594 + 299 + 14 = 907, not 907 distinct accepted assets.

## 검증과 한계 / Verification and limits

복구본은 보존된 파일의 해시와 압축 무결성을 대조했습니다. 이는 새로운 품질 승인이나 Unity 실행 시험을 뜻하지 않습니다. 각 에셋 README의 형상·UV·재질·포즈 및 과거 소실 한계를 함께 읽으세요. 기존 공개 경로의 ID 매칭은 전 바이트 동일성 증명이 아닙니다.
Recovered bytes were checked against preserved hashes and archive integrity. This is not a new quality approval or a Unity runtime test. Read per-asset geometry, UV, material, pose and historical-loss limitations. Existing path-ID matching is not a full byte-identity proof.

이 문서는 새로운 라이선스를 선언하지 않습니다. 공개 참고 링크는 출처 안내이며 제3자 사진의 재배포 권리를 부여하지 않습니다.
No new license is declared. Public reference links are attribution, not permission to redistribute third-party images.

## 대형 BLEND 파일의 무손실 압축 / Lossless compression

NEW695의 LOD0 및 이전 PBR v001 BLEND 두 파일은 전송 크기 제한 때문에 Blender가 직접 읽는 gzip 압축 BLEND로 저장했습니다. 확장자는 `.blend` 그대로이며 Blender 4.3.2에서 실제 재열기를 확인했습니다. 압축 해제한 내용은 기존 원본과 바이트 단위로 동일합니다. 이는 미완성 모델의 품질 승인이나 기능 개선을 뜻하지 않습니다.

Two large NEW695 BLEND files use Blender-compatible gzip compression. They open directly in Blender; decompression reproduces the original bytes exactly. Actual opening was verified in Blender 4.3.2. Their work-in-progress limitations remain unchanged.

- `in_progress/NEW695/LOD0/NEW695_BasketStar_LOD0.blend`: 13,217,996 → 4,856,725 bytes. Decompressed SHA-256: `6ae9876400a386ffca1f0f68b6888c959f2266489121c84c157d5b0c493e4e73`.
- `in_progress/NEW695/earlier_versions/NEW695_BasketStar_PBR_v001.blend`: 13,217,996 → 4,856,706 bytes. Decompressed SHA-256: `40f1a40566cbf001e1bf18bc41490c7713aec33d27a6547e8781f8b3e5f96e23`.

[Blender 공식 압축 형식 안내 / Blender compression format note](https://archive.blender.org/lists/bf-committers/2021-August/051124.html)
