# v098 paused-unit resume record — NOT A COMPLETED ASSET

## Current priority and state
User redirected priority to checking all historical assets and finding recovery methods. Finish this unit's safe remote preservation only; do NOT start v099 or continue geometry work. No usable active version exists.
Plan item C039-01: 경사 독서판과 좁아지는 기둥의 목재 연단. New reconstruction candidate, not recovery of an original file and not a size/color/text variation.
Original plan: fixed commit 7ebe442a8127e26db313b28daaa64f3977d07c9a, backups/2026-11-17-final-assets/ORIGINAL_PLAN_KO.md, line 390.

## Explicit path states
source/: original build and independent verification scripts.
failures/v001/: complete copy of the failed candidate native/render GLB/COL/preview/QA, with FAILURE_STATUS.json.
active/: ORIGINAL GENERATION LOCATION ONLY. Its name is historical, not a release status. These files were retained unchanged, not moved or deleted. STATUS_NOT_RELEASED.json explicitly marks them inactive. They are byte-identical to the quarantined copies.
evidence/: duplicate-search evidence, read-only preservation search, candidate-copy hash comparison.
logs/: original build log and failed geometry-validation log.
ACTIVE_STATUS.json: authoritative state registry; active_usable_version = null.

## Failure and verified facts
Candidate v001 generated successfully. Independent geometry QA failed with Top_support_gap: 0.004553216948751215 m between reading-board underside and support wedge. Do not distribute as a finished usable asset. Do not mark geometric QA as passed merely because native reopening succeeds.
Other checks recorded 30 render meshes, 5 collision solids, 3,624 triangles, 12-degree board, taper, manifold/positive-volume meshes and GLB reimport. The failure remains unresolved.
Source, outputs and all failure evidence are preserved. No original asset or prior-environment file was edited, moved or deleted. Failed copies were created in a new path and verified byte-for-byte without replacing originals.

## Reproduction and dependencies
Blender 4.3.2, built-in bpy/bmesh/mathutils and glTF import/export. Python standard library only; no external texture, font or linked library.
Replay only into a NEW EMPTY output directory:
blender -b --factory-startup --python-exit-code 1 --python source/build_v098.py -- --output /NEW/EMPTY/DIRECTORY
Then:
blender -b --factory-startup --python-exit-code 1 --python source/verify_geometry.py -- --asset-dir /NEW/EMPTY/DIRECTORY --version v001
The verifier is expected to fail on the known support gap. The builder refuses a non-empty output directory. This command sequence is documented; no separate clean replay or byte-identical regeneration has been claimed. Canonical bytes are protected by the checkpoint manifest.
Do not repair geometry until the user's recovery priority permits it; use a new version/output path if later authorized.

## Prior-folder preservation investigation
Read-only recursive search of /workspace, /tmp, /home/agent and /mnt found no representative_route_20261116 or resume_new695 through resume_new709 directory names. One permission error: /tmp/codex-daemon-1000. See evidence/PRESERVATION_SEARCH.json for counts and scope.
This is scoped non-discovery, NOT proof of deletion or successful cleanup. Intentional v091/v092 restores, newly made v093+ standalone assets and Git checkouts are distinct from the missing historical whole-work folders. No recovery or environment changes were used for this search.

## Checkpoint gate and next steps
Repository hoin1357/city-assets; latest main checked at ee60c51d51de0dcfac26cb74f2b41f6885d0cf52.
Unique branch checkpoint-v098-lectern-paused-20261117. New remote folder checkpoints/v098/2026-11-17-paused-v001/.
This record precedes upload. Exact checkpoint commit, file-by-file remote hashes and readable-native reopening will be written in a separate append-only verification receipt. Never infer successful preservation from this pre-upload text.
Stop if GitHub upload or remote-integrity verification fails. No same-form retry after an automatic review rejection. Do not delete local files before verification. No force pushes or existing remote-file replacement.
After the gate, keep new asset production paused and prioritize historical asset recovery investigation. v099 has not started.

Unity NOT_RUN. City placement NOT_RUN. Mechanical/functionality validation NOT_RUN. No medical functionality implemented or validated. No Library upload attempted for this failed candidate; GitHub checkpoint is the requested preservation route.
