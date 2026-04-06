from typing import Any


import dagster as dg
import sys
import os

dagster_jobs_dirs = [
    "/app/dagster_jobs",  # named volume (marimo writes here)
    # "/app/dagster_jobs_host",  # host bind mount (local dev)
]

for d in dagster_jobs_dirs:
    if os.path.exists(d):
        sys.path.insert(0, d)

all_assets = []
all_jobs = []
all_schedules = []

loaded_modules = set[Any]()

for dagster_jobs_dir in dagster_jobs_dirs:
    if not os.path.exists(dagster_jobs_dir):
        continue

    for filename in os.listdir(dagster_jobs_dir):
        if filename.endswith(".py") and not filename.startswith("_") and filename != "__init__.py":
            module_name = filename[:-3]

            if module_name in loaded_modules:
                continue

            try:
                module = __import__(module_name)
                loaded_modules.add(module_name)

                for attr_name in dir(module):
                    if attr_name.startswith("_"):
                        continue
                    attr = getattr(module, attr_name)
                    if isinstance(attr, dg.AssetsDefinition):
                        all_assets.append(attr)
                    elif isinstance(attr, dg.JobDefinition) or type(attr).__name__.endswith(
                        "JobDefinition"
                    ):
                        all_jobs.append(attr)
                    elif isinstance(attr, dg.ScheduleDefinition):
                        all_schedules.append(attr)
            except Exception as e:
                print(f"Error loading {module_name}: {e}")

defs = dg.Definitions(
    assets=all_assets,
    jobs=all_jobs,
    schedules=all_schedules,
)
