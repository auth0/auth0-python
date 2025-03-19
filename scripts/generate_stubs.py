#!/usr/bin/env python3

import ast
import os

# Directory containing the real .py files
SOURCE_DIR = "auth0/management"
PY_SUFFIX = ".py"
STUB_SUFFIX = ".pyi"


def parse_function_signature(funcdef: ast.FunctionDef) -> tuple[list[str], str]:
    """
    From a FunctionDef node, extract a list of parameter strings (including
    annotation and default) and the return type string (without the leading '->').
    If the function has no return annotation, default to 'Any'.
    """
    params = []
    # Number of positional arguments
    all_args = funcdef.args.args  # e.g. [self, fields, include_fields]
    # Default values for the trailing arguments
    # e.g. if we have "fields: list[str] | None = None, include_fields: bool = True"
    # then funcdef.args.defaults will correspond to [None, True].
    defaults = funcdef.args.defaults

    # Where defaults start (the last N arguments in 'all_args' have defaults)
    defaults_start_index = len(all_args) - len(defaults)

    for i, arg in enumerate(all_args):
        arg_name = arg.arg  # e.g. "fields"
        if arg.annotation:
            # Convert the AST for the annotation to source code
            annotation_str = ast.unparse(arg.annotation)
        else:
            annotation_str = "Any"

        if i >= defaults_start_index:  # argument has a default
            default_idx = i - defaults_start_index
            default_ast = defaults[default_idx]  # e.g. "None", "True", etc.
            default_str = ast.unparse(default_ast)
            param_str = f"{arg_name}: {annotation_str} = {default_str}"
        else:
            param_str = f"{arg_name}: {annotation_str}"

        params.append(param_str)

    # Also handle keyword-only arguments (funcdef.args.kwonlyargs) if you wish
    # ... but for brevity we skip that here.

    # Return annotation
    if funcdef.returns:
        return_str = ast.unparse(funcdef.returns)  # e.g. "dict[str, Any]"
    else:
        return_str = "Any"

    return (params, return_str)


def generate_stub_for_file(py_file_path: str) -> str | None:
    """
    Parse a .py file, find classes and their sync methods, and generate
    a .pyi stub with *async versions* that replicate param/return annotations.
    """
    with open(py_file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code, filename=py_file_path)

    stub_lines = []
    # We can insert a minimal import so that "Any" etc. can be used
    stub_lines.append("from typing import Any\n\n")

    found_any_class = False

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            found_any_class = True
            class_name = node.name
            stub_lines.append(f"class {class_name}:")

            # Collect lines for method stubs inside this class
            method_lines = []
            for class_child in node.body:
                if isinstance(class_child, ast.FunctionDef):
                    orig_name = class_child.name

                    # Skip private/special methods or existing *_async
                    if orig_name.startswith("_") or orig_name.endswith("_async"):
                        continue

                    async_name = orig_name + "_async"
                    params, return_str = parse_function_signature(class_child)
                    # Join the parameters with commas
                    params_str = ", ".join(params)

                    # If there's no "self" param at all, you might want to insert it.
                    # But if the code always has "self" as the first param, it's fine.

                    method_sig = f"def {async_name}({params_str}) -> {return_str}: ..."

                    # Indent inside the class
                    method_lines.append("    " + method_sig)

            if not method_lines:
                # If this class has no generated stubs, put a pass
                method_lines.append("    pass")

            stub_lines.extend(method_lines)
            stub_lines.append("")  # blank line after each class

    if not found_any_class:
        # If there's not even a class definition in this file, skip writing
        return None

    # If the final content only has the "from typing import Any\n" line, skip too
    if len(stub_lines) <= 2:
        return None

    return "\n".join(stub_lines)


def main():
    for root, dirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            if filename.endswith(PY_SUFFIX):
                full_path = os.path.join(root, filename)
                # Optionally skip special files, e.g. "__init__.py" if you want
                # if filename == "__init__.py":
                #     continue

                stub_content = generate_stub_for_file(full_path)
                if stub_content:
                    stub_filename = filename.replace(PY_SUFFIX, STUB_SUFFIX)
                    stub_path = os.path.join(root, stub_filename)
                    with open(stub_path, "w", encoding="utf-8") as stub_file:
                        stub_file.write(stub_content)
                    print(f"Generated stub: {stub_path}")


if __name__ == "__main__":
    main()
