from ipywidgets import register
from pythreejs import OrbitControls as _OrbitControls
from traitlets import Unicode, validate, CUnicode, Bytes


@register
class OrbitControls(_OrbitControls):
    _view_name = Unicode("OrbitControlsView2").tag(sync=True)
    _model_name = Unicode("OrbitControlsModel2").tag(sync=True)
    _view_module = Unicode("orbitcontrol_patch").tag(sync=True)
    _model_module = Unicode("orbitcontrol_patch").tag(sync=True)
    _view_module_version = Unicode("0.1.0").tag(sync=True)
    _model_module_version = Unicode("0.1.0").tag(sync=True)

    def update(self):
        """Update the controlled object."""
        self.exec_three_obj_method("update")
