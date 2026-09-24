# Watchless + Frontend Slides 安装完成

安装日期：2026-09-19。

## 已安装

| Skill | 目录 | 来源 |
|---|---|---|
| Watchless | `C:\Users\micro\.codex\skills\watchless` | https://github.com/chenzixin1/watchless |
| Frontend Slides | `C:\Users\micro\.codex\skills\frontend-slides` | https://github.com/zarazhangrui/frontend-slides |

两个 Skill 可在下一轮消息使用。

## 使用示例

把视频文件路径发给 Codex，并说：

> 用 Watchless 和本地 Qwen 完整还原这个视频，生成完整 HTML 图文教程；再用 Frontend Slides 提炼重点，生成单独的 HTML 演示稿，附详细讲稿。保留完整教程里的讲解、案例、推导、数据和操作细节。

## 本地 Qwen 配置

- 默认转写后端：Qwen3-ASR 0.6B INT8，sherpa-onnx CPU。
- 默认参数和 `--provider auto` 均使用本地 Qwen，不自动回退到腾讯云、火山或其他云端 ASR。
- 复用已有目录：`C:\Users\micro\Desktop\ai学习\techvideo2docs`。
- 模型：该目录下的 `models\sherpa-onnx-qwen3-asr-0.6B-int8-2026-03-25`。
- 复用已有 `.venv\Scripts\python.exe`，没有修改原程序，也无需启动 8766 网页。
- 路径配置保存在 Watchless 的 `local-qwen.json`；模型或程序移动后更新此文件。
- Watchless 自身使用独立 `.venv`，依赖与原程序隔离。

## 验证结果

- 54 项自动化测试通过，包括默认后端不选云端、时间精度标记、原始文本保留、分块打包和重叠时间边界处理。
- 用模型自带的 fast1.wav 进行了真实本地 CPU 推理。
- 通过 Watchless 默认转写入口生成 TXT、SRT 和 JSON。
- 合成测试视频完成转写打包、概览抽帧、场景截图、HTML/PDF/ZIP 导出；PDF 已渲染检查。
- 导出审计确认转录按原顺序完整覆盖；唯一提示是没有模型 token 用量，未编造数值。
- Frontend Slides 支持文件完整，PPTX 中文文字和讲稿提取验证通过。
- Python 依赖一致性检查通过。

这些测试验证安装和处理链路可运行，不代表任意课程的识别准确率或完整还原质量已经验证。

## 真实课程测试

已使用用户提供的《1.认识AI.mp4》（约14分36秒）完成真实本地 Qwen 识别，36 个音频块按原顺序覆盖，生成 14 章图文教程和 17 页深色课堂 HTML 演示稿。成品、讲稿、PDF 和原始识别记录位于同目录的“认识AI”文件夹。

## 当前限制

现有 Qwen 引擎约按 25 秒音频块转写，在低能量位置切分并为两侧增加上下文。
时间戳是分块范围，不是精准逐句或逐词对齐；没有内置说话人分离。
边界可能出现重复文字，快速语音、术语、数字等仍需对照原音频核验。
适配器保留原始文字和真实精度标记，未擅自删去重复讲解。

语音识别在本地运行；内容理解、关键画面选择和 HTML 编写由 Codex 完成。

## 维护

Watchless 内的 `LOCAL_SETUP.md` 记录运行方式，`local-patches` 保存上游备份和安装依赖版本。
更新上游 Skill 时，应保留 `local-qwen.json`、本地 Qwen 适配器、Windows 兼容修改与本地使用说明。
FFmpeg/FFprobe、Pandoc 与 video-use 辅助脚本已配置；仅修改运行进程 PATH，没有修改系统全局 PATH。
