import xml.etree.ElementTree as ET
import sys, os
import remi.gui as widget_list

try:
    import lxml.etree as lxml_ET

    USE_LXML = True
except ImportError:
    USE_LXML = False


class RemiXMLTranslator:
    def __init__(self):
        # No longer need widget_map - we'll use dynamic class resolution
        pass

    def translate_xml_to_code_from_root(self, root, file_path=None):
        """Translate XML root element to Remi Python code."""
        code_lines = []
        code_lines.append("from remi import server, gui")
        code_lines.append("")

        # Generate code for root widget
        root_var = self._generate_widget_code(root, code_lines, "root", file_path)
        code_lines.append("")  # Add empty line after root initialization

        # Add return statement
        code_lines.append(f"return {root_var}")

        return "\n".join(code_lines)

    def _generate_widget_code(
        self, element, code_lines: list[str], var_name: str, file_path: str = None
    ):
        """Recursively generate code for a widget and its children."""
        tag = element.tag
        if not hasattr(widget_list, tag):
            line_info = ""
            if USE_LXML and hasattr(element, "sourceline"):
                line_info = (
                    f" at {os.path.abspath(file_path)}, line {element.sourceline}"
                )
            elif file_path:
                line_info = f" in {os.path.abspath(file_path)}"
            raise ValueError(f'Unknown widget type: "{tag}"{line_info}')
        widget_class = tag

        # Collect attributes
        kwargs = {}
        for attr, value in element.attrib.items():
            match attr:
                case "width" | "height":
                    kwargs[attr] = value
                case _:
                    kwargs[attr] = f'"{value}"'

        # Generate instantiation
        args_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        code_lines.append(f"{var_name} = gui.{widget_class}({args_str})")

        # Generate code for children
        child_vars = []
        for i, child in enumerate(element):
            child_var = f"{var_name}_{child.tag}_{i}"
            child_vars.append(child_var)
            self._generate_widget_code(child, code_lines, child_var, file_path)
            key = child.attrib.get("key", "")
            if key:
                code_lines.append(f"{var_name}.append({child_var}, '{key}')")
            else:
                code_lines.append(f"{var_name}.append({child_var})")
            # Add empty line after append/add_tab, except for the last child
            if i < len(element) - 1:
                code_lines.append(
                    ""
                )  # Add empty line for readability after append/add_tab

        return var_name

    def translate_xml_file_to_code(self, xml_file_path: str):
        """Translate XML file to Remi Python code."""
        if USE_LXML:
            tree = lxml_ET.parse(xml_file_path)
            root = tree.getroot()
        else:
            with open(xml_file_path, "r", encoding="utf-8") as f:
                xml_string = f.read()
            root = ET.fromstring(xml_string)
        return self.translate_xml_to_code_from_root(root, xml_file_path)


# Command line usage
def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <xml_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    translator = RemiXMLTranslator()
    code = translator.translate_xml_file_to_code(xml_file)

    # Parse the generated code
    lines = code.split("\n")
    import_line = lines[0]
    code_lines = lines[2:-1]  # Remove import, empty line, and return statement
    ui_code = "\n".join(
        "        " + line if line.strip() else "" for line in code_lines
    )

    base_name = os.path.splitext(xml_file)[0]
    py_file = base_name + ".py"

    full_code = f"""{import_line}

class MyApp(server.App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)
    
    def main(self):
{ui_code}
        # add your code here
        
        return root

if __name__ == "__main__":
    server.start(MyApp)
"""

    with open(py_file, "w", encoding="utf-8") as f:
        f.write(full_code)

    print(f"Generated {py_file}")


if __name__ == "__main__":
    main()
