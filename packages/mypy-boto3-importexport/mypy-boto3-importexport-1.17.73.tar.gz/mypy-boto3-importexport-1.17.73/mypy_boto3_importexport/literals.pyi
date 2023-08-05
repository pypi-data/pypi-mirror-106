"""
Type annotations for importexport service literal definitions.

[Open documentation](./literals.md)

Usage::

    ```python
    from mypy_boto3_importexport.literals import JobTypeType

    data: JobTypeType = "Export"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("JobTypeType", "ListJobsPaginatorName")

JobTypeType = Literal["Export", "Import"]
ListJobsPaginatorName = Literal["list_jobs"]
