# WMG Documentation

> **Summary:** WMG (Workload Migration Gateway) is a comprehensive Python framework for AWS-based data operations, database migrations, and ELT processing. It provides utilities for S3, SQS, Glue, JDBC connections, and automated SQL conversion from Teradata to PySpark/Redshift.

**Key Capabilities:**
- AWS service integrations (S3, SQS, Glue, Secrets Manager)
- Database connectivity (JDBC, HDFS, Teradata, Redshift, PostgreSQL)
- DDL validation and cross-platform schema comparison
- ELT job orchestration with restart capabilities
- LeapLogic SQL conversion engine

---

## Quick Start

For common tasks and quick answers, see **[QUICK_REFERENCE.md](./QUICK_REFERENCE.md)**

---

## Documentation Structure

The WMG module is organized into several functional packages:

- **[Common Utilities](#common-utilities)** — Core utilities for AWS, Spark, data processing, and framework operations.
- **[Data Access Layer (DAL)](#data-access-layer-dal)** — Executor and database access patterns.
- **[ELT Processing](#elt-processing)** — Extract-Load-Transform job orchestration and execution.
- **[Exception Handling](#exception-handling)** — Exception management and restart mechanisms.
- **[Performance Optimization](#performance-optimization)** — Spark configuration and table caching strategies.

---

## Common Utilities

Core utilities used across the WMG framework for AWS integration, Spark operations, data validation, and framework
initialization.

### AWS & Cloud Services

| Module | Purpose |
|--------|---------|
| [aws_sqs_utils.md](./common/com/impetus/idw/wmg/common/aws_sqs_utils.md) | SQS queue operations: send, receive, delete, purge messages |
| [s3_utils.md](./common/com/impetus/idw/wmg/common/s3_utils.md) | S3 bucket operations: upload, download, copy, merge files |
| [glue_utils.md](./common/com/impetus/idw/wmg/common/glue_utils.md) | AWS Glue job management and execution |
| [download_s3_folder.md](./common/com/impetus/idw/wmg/common/download_s3_folder.md) | Bulk download utilities for S3 folders |
| [utils.md](./common/com/impetus/idw/wmg/common/utils.md) | General utility functions and helpers |

### Database & Data Processing

| Module | Purpose |
|--------|---------|
| [jdbc_utils.md](./common/com/impetus/idw/wmg/common/jdbc_utils.md) | JDBC connections and database queries |
| [hdfs_utils.md](./common/com/impetus/idw/wmg/common/hdfs_utils.md) | Hadoop Distributed File System operations |
| [data_migration.md](./common/com/impetus/idw/wmg/common/data_migration.md) | Data migration utilities and patterns |
| [postgres_cross_account_data_migration.md](./common/com/impetus/idw/wmg/common/postgres_cross_account_data_migration.md) | PostgreSQL data migration across AWS accounts |
| [redshift_cross_account_data_migration.md](./common/com/impetus/idw/wmg/common/redshift_cross_account_data_migration.md) | Amazon Redshift data migration across accounts |

### DDL & Schema Validation

| Module | Purpose |
|--------|---------|
| [ddl_validator.md](./common/com/impetus/idw/wmg/common/ddl_validator.md) | Validate DDL (Data Definition Language) statements |
| [redshift_ddl_validator.md](./common/com/impetus/idw/wmg/common/redshift_ddl_validator.md) | Redshift-specific DDL validation |
| [ddl_comparator.md](./common/com/impetus/idw/wmg/common/ddl_comparator.md) | Compare DDL schemas between source and target systems |
| [td_rs_ddl_comparator.md](./common/com/impetus/idw/wmg/common/td_rs_ddl_comparator.md) | Compare Teradata and Redshift DDL schemas |

---

## Data Access Layer (DAL)

Provides abstraction and factory patterns for database executors and query execution.

| Module | Purpose |
|--------|---------|
| [executor_dal.md](./common/com/impetus/idw/wmg/dal/executor_dal.md) | Executor data access patterns and interfaces |
| [glue_executor_dal.md](./common/com/impetus/idw/wmg/dal/glue_executor_dal.md) | AWS Glue-based executor implementation |

---

## ELT Processing

Core modules for orchestrating Extract-Load-Transform jobs and data pipelines.

| Module | Purpose |
|--------|---------|
| [elt_process.md](./common/com/impetus/idw/wmg/elt/elt_process.md) | Main ELT orchestration and workflow engine |
| [data_processing_step.md](./common/com/impetus/idw/wmg/elt/data_processing_step.md) | Individual data processing step definitions |
| [glue_elt_step.md](./common/com/impetus/idw/wmg/elt/glue_elt_step.md) | AWS Glue-specific ELT step implementations |

---

## Performance Optimization

Configuration management for Spark optimization and intelligent table caching.

| Module | Purpose |
|--------|---------|
| [performance.md](./common/com/impetus/idw/wmg/performance.md) | Spark configuration management and table caching strategies |

---
