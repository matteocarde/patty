#!/usr/bin/env python3
"""Genera i grafici delle condizioni E2a ed E2b."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


ITERATIONS = 20
OUTPUT_DIR = Path(__file__).resolve().parent


def condition_e2a(iterations: int = ITERATIONS):
    """Calcola x <- x + y, y <- y - x con aggiornamento simultaneo."""
    x, y = 1.0, 0.0
    x_values = [x]
    y_values = [y]

    for _ in range(iterations):
        next_x = x + y
        next_y = y - x
        x, y = next_x, next_y
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values


def condition_e2b(iterations: int = ITERATIONS):
    """Calcola x <- x - 2.5x, partendo da x = 1."""
    x = 1.0
    repetitions = list(range(iterations + 1))
    x_values = [x]

    for _ in range(iterations):
        x = x - 2.5 * x
        x_values.append(x)

    return repetitions, x_values


def build_e2a_figure(iterations: int = ITERATIONS) -> plt.Figure:
    plt.rcParams.update({
        "text.usetex": True,
        "figure.figsize": [12.50, 4],
        "figure.autolayout": True,
        'font.size': 22
    })
    x_values, y_values = condition_e2a(iterations)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(x_values, y_values, marker="o", linewidth=1.5, markersize=4)
    ax.scatter(x_values[0], y_values[0], s=70, zorder=3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.axvline(0, color="gray", linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect("equal", adjustable="datalim")
    fig.tight_layout()
    return fig


def plot_e2a(iterations: int = ITERATIONS) -> Path:
    fig = build_e2a_figure(iterations)

    output_path = OUTPUT_DIR / "condition_e2a.pdf"
    fig.savefig(output_path, bbox_inches='tight', pad_inches=0.01)
    plt.close(fig)
    return output_path


def build_e2b_figure(iterations: int = ITERATIONS) -> plt.Figure:
    plt.rcParams.update({
        "text.usetex": True,
        "figure.autolayout": True,
        'font.size': 22
    })
    repetitions, x_values = condition_e2b(iterations)

    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(repetitions, x_values, marker="o", linewidth=1.5, markersize=4)
    ax.set_xlabel("r")
    ax.set_ylabel("x")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.grid(True, alpha=0.3)
    ax.set_xticks([5,10,15,20])
    fig.tight_layout()
    return fig


def plot_e2b(iterations: int = ITERATIONS) -> Path:
    fig = build_e2b_figure(iterations)

    output_path = OUTPUT_DIR / "condition_e2b.pdf"
    fig.savefig(output_path, bbox_inches='tight', pad_inches=0.01)
    plt.close(fig)
    return output_path



def main() -> None:
    e2a_path = plot_e2a()
    e2b_path = plot_e2b()


if __name__ == "__main__":
    main()
