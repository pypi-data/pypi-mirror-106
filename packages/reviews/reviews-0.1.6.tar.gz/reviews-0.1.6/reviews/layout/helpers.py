from datetime import datetime
from typing import Dict, List, Tuple

import humanize
from rich import box
from rich.console import RenderGroup
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskID, TextColumn
from rich.table import Table
from rich.tree import Tree

from reviews.config import get_label_colour_map
from reviews.source_control import PullRequest


def _colourise_label(label: str) -> str:
    return get_label_colour_map().get(label.lower(), "[white]") + label


def render_pull_request_table(
    title: str, pull_requests: List[PullRequest], org: str, repository: str
) -> Table:
    """Renders a list of pull requests as a table"""
    table = Table(show_header=True, header_style="bold white")
    table.add_column("#", style="dim", width=5)
    table.add_column(
        f"[link=https://www.github.com/{org}/{repository}]{title}[/link]", width=75
    )
    table.add_column("Labels", width=40)
    table.add_column("Activity", width=15)
    table.add_column("Approved", width=10)
    table.add_column("Mergeable", width=10)

    pull_requests = sorted(pull_requests, key=lambda x: x.updated_at, reverse=True)

    for pr in pull_requests:
        # format and colourize pull request title

        title_colour = ""
        if pr.title.startswith("[Security]"):
            pr.title = pr.title.removeprefix("[Security]")
            title_colour = "[bold red][Security][/]"
        if pr.draft:
            title_colour = "[bold grey][Draft] [/]"

        # format pull request last modified at datetime as a human-readable time
        updated_at = humanize.naturaltime(pr.updated_at)
        colour = ""
        if (datetime.now() - pr.updated_at).days >= 7:
            colour = "[red]"
        elif (datetime.now() - pr.updated_at).days >= 1:
            colour = "[yellow]"
        updated_at = f"{colour}{updated_at}"

        # formats the approval status (approved by me)
        approved = ""
        if pr.approved == "APPROVED":
            approved = "[green]Approved[/]"
        elif pr.approved == "CHANGES_REQUESTED":
            approved = "[red]Changes Requested[/]"

        # format the ready to release status (approved by others)
        approved_by_others = "[green]Ready[/]" if pr.approved_by_others else ""

        labels = ", ".join([_colourise_label(label.name) for label in pr.labels])

        table.add_row(
            f"[white]{pr.number} ",
            (
                f"{title_colour}[white][link=https://www.github.com/"
                f"{org}/{repository}/pull/{pr.number}]{pr.title}[/link][/]"
            ),
            f"{labels}",
            f"{updated_at}",
            f"{approved}",
            f"{approved_by_others}",
        )

    return table


def generate_layout(log: bool = True, footer: bool = True) -> Layout:
    """Define the layout for the terminal UI."""
    layout = Layout(name="root")

    sections = [Layout(name="header", size=3), Layout(name="main", ratio=1)]
    if footer:
        sections.append(Layout(name="footer", size=7))
    layout.split(*sections)

    layout["main"].split_row(
        Layout(name="left_side", size=40),
        Layout(name="body", ratio=2, minimum_size=90),
    )

    nav_sections = [Layout(name="configuration")]
    if log:
        nav_sections.append(Layout(name="log"))

    layout["left_side"].split(*nav_sections)

    return layout


def generate_tree_layout(configuration: List[Tuple[str, str]]) -> RenderGroup:
    """Generates a tree layout for the settings configuration"""
    organization_tree_mapping: Dict[str, Tree] = {}
    for (org, repo) in configuration:
        tree = organization_tree_mapping.get(f"{org}", Tree(f"[white]{org}"))
        tree.add(f"[link=https://www.github.com/{org}/{repo}]{repo}[/link]")
        organization_tree_mapping[org] = tree

    return RenderGroup(*organization_tree_mapping.values())


def generate_log_table(logs: List[Tuple[str, str]]) -> Table:
    """Generetes a table for logging activity"""
    table = Table("Time", "Message", box=box.SIMPLE)

    if logs:
        for log in logs:
            time, message = log
            table.add_row(time, message)

    return table


def generate_progress_tracker() -> Tuple[Progress, Progress, TaskID, Table]:
    """Tracks the progress of background tasks"""
    progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    progress.add_task("[white]Pull Requests", total=100)

    total = sum(task.total for task in progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task(description="All", total=int(total))

    progress_table = Table.grid(expand=True)
    progress_table.add_row(
        Panel(
            renderable=overall_progress,  # type: ignore
            title="Next Refresh",
            border_style="blue",
        ),
        Panel(
            renderable=progress,  # type: ignore
            title="[b]Next fetch for:",
            border_style="blue",
            padding=(1, 2),
        ),
    )

    return progress, overall_progress, overall_task, progress_table
