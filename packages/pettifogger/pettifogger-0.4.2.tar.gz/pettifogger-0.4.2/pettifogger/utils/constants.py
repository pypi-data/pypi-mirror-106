# -*- coding: UTF-8 -*-
__author__ = 'Aki Mäkinen'

ENV_VAR_REGEX = r"\$\{{0,1}([a-zA-Z_][a-zA-Z0-9_]*)\}{0,1}"
# SUSPECTED_ENV_VARS_REGEX = r"(?<!\$)\{{0,1}\b([A-Z_][A-Z0-9_]*)\}{0,1}\b"
SUSPECTED_ENV_VARS_REGEX = r"(?<!\$)\b((?:[A-Z_][A-Z0-9_]*)|(?:\{[A-Z_][A-Z0-9_]*\}))\b"
ENV_VAR_DEFINITION_REGEX = r"\{{0,1}(?P<key>[a-zA-Z_][a-zA-Z0-9_]*)\}{0,1}=(?P<value>.*)"

GITHUB_BUILTIN_ENV_VARS = [
    "CI",
    "GITHUB_WORKFLOW",
    "GITHUB_RUN_ID",
    "GITHUB_RUN_NUMBER",
    "GITHUB_JOB",
    "GITHUB_ACTION",
    "GITHUB_ACTIONS",
    "GITHUB_ACTOR",
    "GITHUB_REPOSITORY",
    "GITHUB_EVENT_NAME",
    "GITHUB_EVENT_PATH",
    "GITHUB_WORKSPACE",
    "GITHUB_SHA",
    "GITHUB_REF",
    "GITHUB_HEAD_REF",
    "GITHUB_BASE_REF",
    "GITHUB_SERVER_URL",
    "GITHUB_API_URL",
    "GITHUB_GRAPHQL_URL"
]