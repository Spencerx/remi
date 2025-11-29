from .gui import (
    Widget,
    Button,
    TextInput,
    SpinBox,
    Label,
    GenericDialog,
    InputDialog,
    ListView,
    ListItem,
    DropDown,
    DropDownItem,
    Image,
    Table,
    TableRow,
    TableItem,
    TableTitle,
    Input,
    Slider,
    ColorPicker,
    Date,
    GenericObject,
    FileFolderNavigator,
    FileFolderItem,
    FileSelectionDialog,
    Menu,
    MenuItem,
    FileUploader,
    FileDownloader,
    VideoPlayer,
)

from .server import App, Server, start

try:
    from importlib.metadata import version

    __version__ = version(__name__)
except ImportError:
    # Fallback for older Python versions
    pass
