__version__ = "2.0.13"

from swegym.collect.build_dataset import main as build_dataset
from swegym.collect.get_tasks_pipeline import main as get_tasks_pipeline
from swegym.collect.print_pulls import main as print_pulls

from swegym.harness.constants import (
    KEY_INSTANCE_ID,
    KEY_MODEL,
    KEY_PREDICTION,
    MAP_REPO_VERSION_TO_SPECS,
)

from swegym.harness.docker_build import (
    build_image,
    build_base_images,
    build_env_images,
    build_instance_images,
    build_instance_image,
    close_logger,
    setup_logger,
)

from swegym.harness.docker_utils import (
    cleanup_container,
    remove_image,
    copy_to_container,
    exec_run_with_timeout,
    list_images,
)

from swegym.harness.grading import (
    compute_fail_to_pass,
    compute_pass_to_pass,
    get_logs_eval,
    get_eval_report,
    get_resolution_status,
    ResolvedStatus,
    TestStatus,
)

from swegym.harness.log_parsers import (
    MAP_REPO_TO_PARSER,
)

from swegym.harness.run_evaluation import (
    main as run_evaluation,
)

from swegym.harness.utils import (
    get_environment_yml,
    get_requirements,
)

from swegym.versioning.constants import (
    MAP_REPO_TO_VERSION_PATHS,
    MAP_REPO_TO_VERSION_PATTERNS,
)

from swegym.versioning.get_versions import (
    get_version,
    map_version_to_task_instances,
    get_versions_from_build,
    get_versions_from_web,
)

from swegym.versioning.utils import (
    split_instances,
)
