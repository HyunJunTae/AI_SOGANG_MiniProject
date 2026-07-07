"""Export normalized LLM evidence vectors to the shared XAI output folders."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from XAI.LLMComparison.common import (  # noqa: E402
    comparison_dir,
    read_jsonl,
    validate_words_scores,
    xai_root,
)


POSITIVE_COLOR = "#d95f5f"
NEGATIVE_COLOR = "#4c78a8"
ZERO_COLOR = "#9aa0a6"
GRID_COLOR = "#d9dee7"


def configure_fonts() -> None:
    """Use a Korean-capable font when one is available."""
    preferred_fonts = [
        "Malgun Gothic",
        "NanumGothic",
        "Noto Sans CJK KR",
        "Noto Sans KR",
        "AppleGothic",
        "DejaVu Sans",
    ]
    available = {font.name for font in font_manager.fontManager.ttflist}
    for font_name in preferred_fonts:
        if font_name in available:
            plt.rcParams["font.family"] = font_name
            break
    plt.rcParams["axes.unicode_minus"] = False


def short_text(value: Any, max_chars: int = 72) -> str:
    """Keep chart captions readable."""
    text = str(value)
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 3] + "..."


def wrap_label(value: str, width: int = 16) -> str:
    """Wrap long eojeol labels for chart axes."""
    if len(value) <= width:
        return value
    chunks = [value[index : index + width] for index in range(0, len(value), width)]
    return "\n".join(chunks[:3])


def safe_filename(value: str) -> str:
    """Make a stable filesystem-safe filename stem."""
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._") or "chart"


def symmetric_limit(scores: list[float]) -> float:
    """Choose a symmetric x-axis limit around zero."""
    max_abs = max((abs(score) for score in scores), default=0.0)
    if max_abs == 0.0:
        return 1.0
    return max_abs * 1.18


def output_item(row: dict[str, Any]) -> dict[str, Any]:
    """Convert one normalized LLM vector row to the shared output JSON schema."""
    sample_id = str(row.get("sample_id", "")).strip()
    words = [str(word) for word in row.get("words", [])]
    scores = [float(score) for score in row.get("llm_vector", [])]
    validate_words_scores(sample_id or "<missing-sample-id>", words, scores)

    return {
        "text": row.get("text", ""),
        "prediction": row.get("llm_sentiment", ""),
        "probability": "",
        "words": words,
        "scores": scores,
        "sample_id": sample_id,
        "llm_evidence_indices": [int(idx) for idx in row.get("llm_evidence_indices", [])],
        "evidence": row.get("evidence", []),
        "brief_reason": row.get("brief_reason", ""),
        "model_id": row.get("model_id", ""),
        "prompt_version": row.get("prompt_version", ""),
        "created_at": row.get("created_at", ""),
    }


def write_json(path: Path, payload: list[dict[str, Any]]) -> None:
    """Write readable UTF-8 JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def draw_bar_chart(item: dict[str, Any], item_index: int, chart_dir: Path) -> Path:
    """Draw one LLM evidence vector as a horizontal bar chart."""
    words = [str(word) for word in item.get("words", [])]
    scores = [float(score) for score in item.get("scores", [])]
    if not words:
        raise ValueError(f"LLM item {item_index} has no plottable words.")

    sample_id = str(item.get("sample_id") or f"sentence_{item_index}")
    out_path = chart_dir / safe_filename(f"sentence_{item_index}.png")
    colors = [
        POSITIVE_COLOR if score > 0 else NEGATIVE_COLOR if score < 0 else ZERO_COLOR
        for score in scores
    ]

    height = max(3.2, 0.48 * len(words) + 1.8)
    fig, ax = plt.subplots(figsize=(10.8, height))
    y_positions = list(range(len(words)))
    ax.barh(y_positions, scores, color=colors, height=0.64)
    ax.set_yticks(y_positions)
    ax.set_yticklabels([wrap_label(word) for word in words])
    ax.invert_yaxis()
    ax.axvline(0.0, color="#20242a", linewidth=0.9)
    ax.grid(axis="x", color=GRID_COLOR, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)

    x_limit = symmetric_limit(scores)
    ax.set_xlim(-x_limit, x_limit)
    ax.set_xlabel("Signed normalized LLM evidence")

    title_bits = ["LLM Evidence", sample_id]
    prediction = item.get("prediction", "")
    if prediction != "":
        title_bits.append(f"pred={prediction}")
    model_id = item.get("model_id", "")
    if model_id != "":
        title_bits.append(str(model_id))
    ax.set_title(" | ".join(title_bits), fontsize=12, pad=12)
    fig.text(0.5, 0.015, short_text(item.get("text", "")), ha="center", fontsize=9)

    label_offset = x_limit * 0.025
    for y_pos, score in zip(y_positions, scores):
        ha = "left" if score >= 0 else "right"
        x_pos = score + label_offset if score >= 0 else score - label_offset
        ax.text(x_pos, y_pos, f"{score:.3f}", va="center", ha=ha, fontsize=8)

    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)

    fig.subplots_adjust(left=0.27, right=0.96, top=0.86, bottom=0.17)
    chart_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=160)
    plt.close(fig)
    return out_path


def relative_to(path: Path, base: Path) -> str:
    """Return a POSIX-style relative path for HTML links."""
    return path.relative_to(base).as_posix()


def write_html_index(out_path: Path, json_path: Path, chart_paths: list[Path]) -> None:
    """Write a browsable HTML index for generated LLM charts."""
    sections: list[str] = [
        "<!doctype html>",
        '<html lang="ko">',
        "<head>",
        '<meta charset="utf-8">',
        "<title>LLM Evidence Output Visualizations</title>",
        "<style>",
        "body{font-family:Arial,'Malgun Gothic',sans-serif;margin:24px;background:#f6f8fb;color:#1f2933}",
        "h1,h2{margin:0 0 14px}",
        "section{margin:26px 0}",
        ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:16px}",
        "figure{margin:0;background:#fff;border:1px solid #dce3ee;border-radius:8px;padding:10px}",
        "img{max-width:100%;height:auto;display:block}",
        "figcaption{font-size:12px;color:#52606d;margin-top:8px;word-break:break-all}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>LLM Evidence Output Visualizations</h1>",
        f"<p>Source JSON: <code>{html.escape(str(json_path))}</code></p>",
        "<section><h2>Evidence Vectors</h2><div class=\"grid\">",
    ]

    for path in chart_paths:
        link = html.escape(relative_to(path, out_path.parent))
        sections.append(
            f'<figure><img src="{link}" alt="{html.escape(path.stem)}">'
            f"<figcaption>{html.escape(path.name)}</figcaption></figure>"
        )

    sections.extend(["</div></section>", "</body>", "</html>"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(sections) + "\n", encoding="utf-8")


def write_summary(
    out_path: Path,
    input_path: Path,
    json_path: Path,
    graph_dir: Path,
    chart_paths: list[Path],
    html_path: Path,
) -> None:
    """Write a machine-readable run summary."""
    payload = {
        "input": str(input_path),
        "json_output": str(json_path),
        "graph_dir": str(graph_dir),
        "sample_chart_count": len(chart_paths),
        "index_html": str(html_path),
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line options."""
    parser = argparse.ArgumentParser(
        description="Export normalized LLM evidence vectors to shared XAI output folders."
    )
    parser.add_argument("--input", type=Path, default=comparison_dir() / "llm_vectors.jsonl")
    parser.add_argument(
        "--json-output",
        type=Path,
        default=xai_root() / "outputs_json" / "output_llm_evidence.json",
    )
    parser.add_argument(
        "--graph-dir",
        type=Path,
        default=xai_root() / "outputs_graph" / "llm_evidence",
    )
    parser.add_argument(
        "--index-output",
        type=Path,
        default=xai_root() / "outputs_graph" / "llm_index.html",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=xai_root() / "outputs_graph" / "llm_visualization_summary.json",
    )
    parser.add_argument("--skip-graphs", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the export."""
    args = parse_args(sys.argv[1:] if argv is None else argv)
    rows = read_jsonl(args.input)
    if not rows:
        raise ValueError(f"No LLM vector rows found in {args.input}")

    payload = [output_item(row) for row in rows]
    write_json(args.json_output, payload)
    print(f"Wrote {args.json_output} ({len(payload)} rows)")

    if args.skip_graphs:
        return 0

    configure_fonts()
    chart_paths = [
        draw_bar_chart(item, item_index, args.graph_dir)
        for item_index, item in enumerate(payload, start=1)
    ]
    write_html_index(args.index_output, args.json_output, chart_paths)
    write_summary(
        args.summary_output,
        args.input,
        args.json_output,
        args.graph_dir,
        chart_paths,
        args.index_output,
    )
    print(f"Wrote {len(chart_paths)} LLM evidence charts")
    print(f"Wrote {args.index_output}")
    print(f"Wrote {args.summary_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
