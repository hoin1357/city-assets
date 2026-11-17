# v097 execution resume checkpoint

## Unit and active result
Plan C027-06: 긴 경첩 절단 레버와 격자 받침의 재단기. New reconstruction candidate for print-room/office scenes, not recovery of an original model.
Original plan is available at fixed commit 7ebe442a8127e26db313b28daaa64f3977d07c9a, backups/2026-11-17-final-assets/ORIGINAL_PLAN_KO.md, line 373.
Active unit v097; active geometry v003. Final native/render/COL filenames end in _v003. Hero is PREVIEW_PAPER_CUTTER_HERO_v097_v003.png. README_KO.md is active usage documentation. INDEPENDENT_QA_v003.json and verify_v097_v003.py are active validation.

## Fixed deliverable reference
Repository hoin1357/city-assets.
Branch asset-v097-paper-cutter-20261117.
Verified final-use artifact commit 541119fa8dab2525b39663628baa8867327cd75d.
Folder backups/2026-11-17-v097-paper-cutter/.
ZIP SHA256 47895d8687eeec6799a84e12e6be4e57eb31adcd0d5a61750754413022f0da8d, 2,243,371 bytes.
This checkpoint's commit will be recorded in a separate append-only verification receipt after downloading and checking it. Do not infer checkpoint success from this pre-upload record.

## Original, failure and active states
The snapshot retains the entire 40-file v097 working directory with a file-by-file SHA256/size manifest.
v001 is an initial standalone candidate, not an old recovered original. Its exported grip ridges failed degenerate-triangle checks.
v002 preserves the first repair but exported Lever_accent still failed triangle checks.
v003 replaces those thin bevelled details with closed boxes and passes independent checks.
Keep v001/v002 native, GLBs, previews, scripts and logs; do not delete or use them as active exports. Earlier user originals and old-environment failures were not edited or removed.
The scoped read-only search did not find representative_route_20261116 or resume_new695–709. This is not proof of deletion/cleanup. See PRESERVATION_SEARCH_20261117.md. v091/v092 intentional restores, new v093+ outputs and Git checkouts are not those historical work folders.

## Dependencies and reproduction
Blender 4.3.2 with built-in glTF importer/exporter; Blender Python bpy/bmesh/mathutils. System Python 3 standard library for ZIP, SHA256 and subprocess checks. No external font, image, Python package or linked Blender library is required. Cycles CPU render, 48 samples, denoising disabled.
Extract into a NEW directory. The archived scripts contain the original /workspace/v097_paper_cutter output root. For a replay, make NEW script copies in the replay directory and replace that literal output-root string with the replay directory's absolute path. Never run replay against the preserved source directory.
Run copied scripts in this order with blender -b --factory-startup --python-exit-code 1 --python SCRIPT:
1. build_v097.py (initial v001)
2. fix_v002.py (v002 repair)
3. fix_v003.py (active v003 repair)
4. verify_v097_v003.py (independent validation)
5. render_v003.py (preview-only floor; no native resave)
This is the performed construction/repair chain. A separate clean replay has NOT been executed, and byte-identical native/render regeneration is not promised. Canonical verified bytes are the fixed artifact package and this snapshot.

## Verification completed before this checkpoint
Final geometry: 53 render meshes, 3,080 triangles, 6 box proxies, static 30-degree lever. Manifold/positive volume/nondegenerate geometry and GLB actual triangle areas/bounds passed. No external dependencies found.
Artifact commit above: four published files re-downloaded byte-for-byte; ZIP CRC, nine internal manifest SHA256/byte entries and Blender native reopening passed.
Unity NOT_RUN. City placement NOT_RUN. Cutting, motion, clamping, interlocks and mechanical safety NOT_IMPLEMENTED_NOT_VALIDATED. No medical functionality.
Library final-use save succeeded, but Library download path remains blocked by proxy HTTP 403 or returned path absent in this container. Treat GitHub and Library verification separately.

## Gate and next step
Do not start v098 or another work unit until GitHub upload, fixed-commit redownload, every snapshot-file hash/size check, ZIP CRC and active native reopen all pass and a verification receipt exists.
If any GitHub gate operation fails, stop new work and report the exact failure. Do not delete local files before verification. Never force-push or replace previous remote files. Add new paths and commits.
After this gate, wait for the next authorized single-asset unit; historical asset upload/comparison/cleanup remains a separate priority handled elsewhere. Keep the prior environment untouched.
