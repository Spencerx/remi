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

# importlib.metadata is available in Python 3.8+
useForVersionCheck = None
try:
    import importlib.metadata
    useForVersionCheck = "importlib.metadata"
except ImportError:
    try:
        import pkg_resources
        useForVersionCheck = "pkg_resources"
    except ImportError:
        pass

if useForVersionCheck == "importlib.metadata":
    from importlib.metadata import version, PackageNotFoundError
    try:
        __version__ = version(__name__)
    except PackageNotFoundError:
        # package is not installed
        pass
elif useForVersionCheck == "pkg_resources":
    from pkg_resources import get_distribution, DistributionNotFound
    try:
        __version__ = get_distribution(__name__).version
    except DistributionNotFound:
        # package is not installed
        pass
else:
    # neither importlib.metadata nor pkg_resources is available
    pass