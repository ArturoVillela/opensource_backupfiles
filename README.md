# OpenSource Backup Files

A simple desktop application for Linux that helps users select and copy files and folders to another location.

The project is being developed with Python and Qt. Its goal is to provide a clear interface for reviewing copied files, detecting conflicts, and deciding whether existing files should be overwritten or skipped. Updated ui with Stitch.
## Changelog

- **Replaced fake multithreading with native script execution** — Python's GIL prevents true parallelism for CPU-bound I/O; file copying now delegates to a native bash script and captures its output, giving real concurrent file operations.
- **New HTML/CSS/JS file list UI** — Replaced the previous `QScrollArea`-based widget with a clean, responsive web-view-based file listing (rendered via `QWebEngineView` or equivalent), offering a significantly better visual experience and smoother scrolling for large file sets.

## User interface

![Application user interface](docs/images/app-ui.png)

> Replace `docs/images/app-ui.png` with a screenshot of the application while keeping the same filename and folder structure.

## Current features

- Select individual files.
- Select folders.
- Display the selected paths in the interface.
- Store the selected paths for later processing.
- Shorten long paths for easier display.
-- **Happy path working** — End-to-end copy flow is functional when no file conflicts are detected: select source → select destination → copy → summary displayed.   


## Planned features

- Select a destination folder.
- Prevent duplicate paths.
- Remove paths from the selection.
- Compare source and destination files.
- Display copied files and detected conflicts.
- Show information about both files when a conflict occurs.
- Allow users to overwrite or skip existing files.
- Display copy progress and a final summary.
- Run file copying in a secondary thread.
- Package the application for installation on Linux Mint.

## Technologies

- Python
- Qt
- Qt Creator
- Qt Designer
- Bash Scripting
- Html-Js-Css

### Project Status

**~90% complete.** The core file-copying engine is finished and tested.

| Component | Status |
|-----------|--------|
| Native copy script (subprocess) | ✅ Done |
| File list UI (HTML/CSS/JS) | ✅ Done |
| Happy path (no conflicts) | ✅ Done |
| Conflict table UI (overwrite / skip) | 🔧 In progress |
| Conflict resolution logic | 🔧 In progress |

## License

License information will be added later.
