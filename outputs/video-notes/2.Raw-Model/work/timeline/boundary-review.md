# Semantic Boundary Review

Mode: explainer
Conversation profile: n/a
Rule: One complete argument, example, or visual function per scene. Camera cuts alone are not boundaries.

Primary transcript: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\video-use\takes_packed.md`
Word timeline: `C:\Users\micro\Desktop\ai-lesson\outputs\video-notes\2.AI最底层的Raw-Model\work\video-use\transcripts\2.AI最底层的Raw-Model.json`

Read the packed transcript first. Propose boundaries at phrase ends using semantic completion, silence gaps, and speaker handoffs.
For every proposed boundary T, run video-use timeline_view on approximately T-4s to T+4s and inspect the filmstrip, waveform, words, and silence shading.
Do not scan the whole video on a fixed interval. Visuals are used only to confirm or adjust actual decision points.

Write scene-boundaries.json as:
{"mode":"explainer","scenes":[{"end_sec":42.35,"reason":"complete argument and clean pause"}]}
The final end_sec must cover the final cue at 935.700s (video duration 935.667s).
