# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ShakyFOV RBX Export",
    "author" : "Shaky | Mymyamo47", 
    "description" : "Exports blender camera FOV to Roblox!",
    "blender" : (4, 2, 0),
    "version" : (1, 0, 2),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Animation" 
}


import bpy
import bpy.utils.previews
import os


addon_keymaps = {}
_icons = None
addon = {'sna_new_variable': [], }


def sna_update_sna_activecamera_593D4(self, context):
    sna_updated_prop = self.sna_activecamera
    Validated = bpy.context.scene.sna_cameravalidated
    Cam = bpy.context.scene.sna_activecamera
    IsValidated = None
    print(Cam)
    IsValidated = Cam.sensor_fit == "VERTICAL" and Cam.sensor_height == 100
    bpy.context.scene.sna_cameravalidated = IsValidated


class SNA_PT_SHAKY_FOV_EXPORT_2B8CB(bpy.types.Panel):
    bl_label = 'Shaky FOV Export'
    bl_idname = 'SNA_PT_SHAKY_FOV_EXPORT_2B8CB'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'RBXMonkey'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout
        layout.label(text='', icon_value=177)

    def draw(self, context):
        layout = self.layout
        layout.prop(bpy.context.scene, 'sna_activecamera', text='Target', icon_value=177, emboss=True)
        op = layout.operator('sna.compilecamera_1fb54', text='Copy to clipboard', icon_value=0, emboss=True, depress=False)
        if bpy.context.scene.sna_cameravalidated:
            pass
        else:
            box_9D8BF = layout.box()
            box_9D8BF.alert = False
            box_9D8BF.enabled = True
            box_9D8BF.active = True
            box_9D8BF.use_property_split = False
            box_9D8BF.use_property_decorate = False
            box_9D8BF.alignment = 'Expand'.upper()
            box_9D8BF.scale_x = 1.0
            box_9D8BF.scale_y = 1.0
            if not True: box_9D8BF.operator_context = "EXEC_DEFAULT"
            col_D983B = box_9D8BF.column(heading='', align=False)
            col_D983B.alert = True
            col_D983B.enabled = True
            col_D983B.active = True
            col_D983B.use_property_split = False
            col_D983B.use_property_decorate = False
            col_D983B.scale_x = 1.0
            col_D983B.scale_y = 0.7900000214576721
            col_D983B.alignment = 'Expand'.upper()
            col_D983B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            col_D983B.label(text='Camera has wrong sensor properties', icon_value=0)
            col_D983B.label(text='Fix the camera', icon_value=0)
            row_4F74A = box_9D8BF.row(heading='', align=False)
            row_4F74A.alert = False
            row_4F74A.enabled = True
            row_4F74A.active = True
            row_4F74A.use_property_split = False
            row_4F74A.use_property_decorate = False
            row_4F74A.scale_x = 1.0
            row_4F74A.scale_y = 2.6500000953674316
            row_4F74A.alignment = 'Expand'.upper()
            row_4F74A.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
            op = row_4F74A.operator('sna.validatecamera_31c6c', text='FIX THE CAMERA', icon_value=0, emboss=True, depress=False)
        if bpy.context.scene.sna_completed:
            layout.label(text='Compiled!', icon_value=54)
        row_6791E = layout.row(heading='', align=False)
        row_6791E.alert = False
        row_6791E.enabled = True
        row_6791E.active = True
        row_6791E.use_property_split = False
        row_6791E.use_property_decorate = False
        row_6791E.scale_x = 1.0
        row_6791E.scale_y = 1.0
        row_6791E.alignment = 'Right'.upper()
        row_6791E.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_6791E.label(text='By Mymyamo47', icon_value=0)
        row_6791E.template_icon(icon_value=_icons['chudkyicon.png'].icon_id, scale=2.0)


class SNA_OT_Compilecamera_1Fb54(bpy.types.Operator):
    bl_idname = "sna.compilecamera_1fb54"
    bl_label = "CompileCamera"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        Camera = bpy.context.scene.sna_activecamera
        import math
        scene = bpy.context.scene
        values = []
        CurFrame = bpy.context.scene.frame_current
        for frame in range(scene.frame_start, scene.frame_end + 1):
            scene.frame_set(frame)
            fov = round(Camera.angle*57.273, 2)
            values.append(f"{fov:.6f}")
        scene.frame_set(CurFrame)
        bpy.context.window_manager.clipboard = ", ".join(values)

        def delayed_72461():
            bpy.context.scene.sna_completed = False
        bpy.app.timers.register(delayed_72461, first_interval=0.2200000286102295)
        bpy.context.scene.sna_completed = True
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Validatecamera_31C6C(bpy.types.Operator):
    bl_idname = "sna.validatecamera_31c6c"
    bl_label = "ValidateCamera"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        Cam = bpy.context.scene.sna_activecamera
        Validated = None
        Validated = False
        Cam.sensor_fit = "VERTICAL"
        Cam.sensor_height = 1200
        Validated = True
        bpy.context.scene.sna_cameravalidated = Validated
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_activecamera = bpy.props.PointerProperty(name='ActiveCamera', description='', type=bpy.types.Camera, update=sna_update_sna_activecamera_593D4)
    bpy.types.Scene.sna_cameravalidated = bpy.props.BoolProperty(name='CameraValidated', description='', default=True)
    bpy.types.Scene.sna_completed = bpy.props.BoolProperty(name='Completed', description='', default=False)
    bpy.utils.register_class(SNA_PT_SHAKY_FOV_EXPORT_2B8CB)
    if not 'chudkyicon.png' in _icons: _icons.load('chudkyicon.png', os.path.join(os.path.dirname(__file__), 'icons', 'chudkyicon.png'), "IMAGE")
    bpy.utils.register_class(SNA_OT_Compilecamera_1Fb54)
    bpy.utils.register_class(SNA_OT_Validatecamera_31C6C)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_completed
    del bpy.types.Scene.sna_cameravalidated
    del bpy.types.Scene.sna_activecamera
    bpy.utils.unregister_class(SNA_PT_SHAKY_FOV_EXPORT_2B8CB)
    bpy.utils.unregister_class(SNA_OT_Compilecamera_1Fb54)
    bpy.utils.unregister_class(SNA_OT_Validatecamera_31C6C)
