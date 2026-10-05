# Encyclopedia Cutaway

A reusable Codex skill for hand-painted encyclopedia explainers: open a machine, building, or physical system, reveal how its parts work together, and surround it with readable captions.

Fine ink, watercolor and gouache give the page a printed-book feel. Backgrounds follow the subject; small people or animals add everyday life. Language, composition and detail remain configurable.

Ten plates reviewed and packaged with their actual prompts and specific limitations.

![Space telescope, illustrated in English](examples/01-space-telescope.png)

## Ten languages, ten domains

[View all ten plates →](examples/README.md)

| Language | Subject | Background |
|---|---|---|
| English | [A space telescope](examples/01-space-telescope.png) | ink-indigo |
| Bahasa Melayu | [Stesen hidroelektrik](examples/02-hydropower.png) | misty slate-teal |
| Español | [Dentro de una colmena](examples/03-beehive.png) | honey-peach |
| Français | [À l'intérieur d'un orgue](examples/04-pipe-organ.png) | muted burgundy |
| Deutsch | [Eine spiegellose Kamera](examples/05-mirrorless-camera.png) | graphite-blue |
| Italiano | [Un forno a legna](examples/06-bread-oven.png) | brick terracotta |
| 日本語 | [ロボットアームのしくみ](examples/07-robot-arm.png) | smoky cyan |
| 한국어 | [지진계의 원리](examples/08-seismograph.png) | plum-gray |
| Bahasa Indonesia | [Derek peti kemas](examples/09-container-crane.png) | stormy petrol |
| Português | [Cromatografia gasosa](examples/10-gas-chromatography.png) | dusty rose |

These are ten new examples, not translations of one illustration. Exact prompts, captions, primary sources and review findings are in [the manifest](examples/manifest.json). Generation is nondeterministic: reusing a prompt will not reproduce identical pixels.

## Install

Clone or download this repository, then copy the **whole** folder `.agents/skills/encyclopedia-cutaway` into `~/.codex/skills/`.

PowerShell, from the downloaded repository:

```powershell
$skillDestination = Join-Path $env:USERPROFILE '.codex/skills'
New-Item -ItemType Directory -Force -Path $skillDestination | Out-Null
Copy-Item -LiteralPath '.agents/skills/encyclopedia-cutaway' -Destination $skillDestination -Recurse
```

If a skill with this name is already installed, review your existing customizations before replacing it. The [skill entrypoint](.agents/skills/encyclopedia-cutaway/SKILL.md), prompt template and generated style reference work together. The built-in image-generation tool is required for rendering.

## Use

```text
Use $encyclopedia-cutaway to explain a pipe organ in French.
Choose a muted burgundy paper background, slightly stronger hand-painted
brushwork, six concise callouts and a quiet everyday-life scene.
```

繁體中文也可以：

```text
用 $encyclopedia-cutaway 畫一張木造風車的百科剖面圖。
使用繁體中文、麥金色紙張背景、細墨線與水彩筆觸，
在角落加一隻休息的小狗，保留清楚的構造標註。
```

Specify subject, language/script, aspect ratio, background, information density, living accents and painterly intensity when they matter. Defaults favor a landscape conceptual illustration with compact captions.

## Review and limits

Each selected plate is reviewed for framing, lettering, contrast, callout placement and visible component relationships. Specific limitations and edits are recorded in the manifest. Primary-source links support the intended concept; they do not certify every generated line.

These are raster images: the text is not an editable typography layer. They are not construction drawings, calibrated scientific figures, clinical guidance or safe operating instructions. Multilingual copy has a model review, not native-speaker certification. For professional teaching or publication, have a subject expert and fluent reader review the selected plate.

## Contribute

Keep the skill concise and language-neutral. For a new example, record its exact prompt, caption text, primary sources, image filename and observable review findings in the manifest. Inspect the actual image before marking it reviewed; preserve earlier selections when iterating.

After updating images or the manifest, run `python scripts/validate_package.py` to check selected-file hashes, dimensions, review records and relative Markdown links. It does not judge artwork or technical accuracy.

## License

[MIT](LICENSE), © 2026 Gregory Hong. The license covers this package and its included generated examples to the extent the author can grant rights. Linked external sources retain their own rights. Original user-uploaded reference images are not redistributed.
